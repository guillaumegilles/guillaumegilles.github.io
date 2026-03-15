#!/usr/bin/env python3
"""
POSSE syndication to LinkedIn.

Usage (called by GitHub Actions):
    python linkedin.py --post posts/my-post/index.qmd --base-url https://guillaumegilles.github.io

Environment variables (GitHub secrets):
    LINKEDIN_ACCESS_TOKEN   – OAuth 2.0 bearer token
    LINKEDIN_REFRESH_TOKEN  – long-lived refresh token (valid ~1 year)
    LINKEDIN_CLIENT_ID      – LinkedIn app client ID
    LINKEDIN_CLIENT_SECRET  – LinkedIn app client secret
    LINKEDIN_PERSON_URN     – urn:li:person:<ID>
    GH_TOKEN                – GitHub token with secrets:write (for auto-refresh)
    GH_REPO                 – owner/repo string (for auto-refresh)
"""

import argparse
import json
import os
import re
import sys
import textwrap

import requests
import yaml


# ── LinkedIn API endpoints ────────────────────────────────────────────────────
API_BASE  = "https://api.linkedin.com/v2"
TOKEN_URL = "https://www.linkedin.com/oauth/v2/accessToken"


# ── Helpers ───────────────────────────────────────────────────────────────────

def load_post_metadata(qmd_path: str) -> dict:
    """Parse YAML front matter from a .qmd file."""
    with open(qmd_path, encoding="utf-8") as f:
        content = f.read()
    m = re.match(r"^---\s*\n(.*?\n)---\s*\n", content, re.DOTALL)
    if not m:
        raise ValueError(f"No YAML front matter found in {qmd_path}")
    return yaml.safe_load(m.group(1))


def post_slug(qmd_path: str) -> str:
    """Derive the URL path segment from the .qmd file location."""
    # posts/my-post/index.qmd  →  posts/my-post/
    parts = qmd_path.replace("\\", "/").split("/")
    if parts[-1] == "index.qmd":
        return "/".join(parts[:-1]) + "/"
    return "/".join(parts[:-1]) + "/" + parts[-1].replace(".qmd", ".html")


def build_post_text(meta: dict, canonical_url: str) -> str:
    """Compose the LinkedIn post body text (max ~3000 chars)."""
    title    = meta.get("title", "New post")
    abstract = meta.get("abstract", "").strip()
    cats     = meta.get("categories", [])

    # Truncate abstract to 280 chars so the link preview has room to breathe
    abstract = textwrap.shorten(abstract, width=280, placeholder="…")

    hashtags = " ".join(
        "#" + re.sub(r"\W+", "", c.title().replace(" ", ""))
        for c in cats
    )

    lines = [f"📝 {title}", "", abstract, "", canonical_url]
    if hashtags:
        lines += ["", hashtags]

    return "\n".join(lines)


# ── Token refresh ─────────────────────────────────────────────────────────────

def refresh_access_token() -> str:
    """Exchange refresh token for a new access token and update GitHub secret."""
    refresh_token  = os.environ["LINKEDIN_REFRESH_TOKEN"]
    client_id      = os.environ["LINKEDIN_CLIENT_ID"]
    client_secret  = os.environ["LINKEDIN_CLIENT_SECRET"]

    resp = requests.post(TOKEN_URL, data={
        "grant_type":    "refresh_token",
        "refresh_token": refresh_token,
        "client_id":     client_id,
        "client_secret": client_secret,
    }, timeout=15)
    resp.raise_for_status()
    data = resp.json()
    new_token = data["access_token"]

    # Persist new token back to GitHub secrets so next run works
    gh_token = os.environ.get("GH_TOKEN")
    gh_repo  = os.environ.get("GH_REPO")
    if gh_token and gh_repo:
        import subprocess
        subprocess.run(
            ["gh", "secret", "set", "LINKEDIN_ACCESS_TOKEN",
             "--body", new_token, "--repo", gh_repo],
            env={**os.environ, "GH_TOKEN": gh_token},
            check=True,
        )
        print("✅ GitHub secret LINKEDIN_ACCESS_TOKEN updated.")

    return new_token


# ── LinkedIn API call ─────────────────────────────────────────────────────────

def post_to_linkedin(text: str, canonical_url: str, title: str,
                     abstract: str, access_token: str, person_urn: str) -> str:
    """Post a UGC article share to LinkedIn. Returns the created post URN."""
    headers = {
        "Authorization":  f"Bearer {access_token}",
        "Content-Type":   "application/json",
        "X-Restli-Protocol-Version": "2.0.0",
    }
    payload = {
        "author":         person_urn,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {"text": text},
                "shareMediaCategory": "ARTICLE",
                "media": [{
                    "status":      "READY",
                    "description": {"text": textwrap.shorten(abstract, 256, placeholder="…")},
                    "originalUrl": canonical_url,
                    "title":       {"text": title},
                }],
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        },
    }
    resp = requests.post(f"{API_BASE}/ugcPosts", headers=headers,
                         json=payload, timeout=15)
    return resp


def syndicate(qmd_path: str, base_url: str) -> None:
    meta  = load_post_metadata(qmd_path)

    # Respect opt-in field: syndicate: [linkedin]
    targets = meta.get("syndicate", [])
    if "linkedin" not in (t.lower() for t in targets):
        print(f"⏭  Skipping {qmd_path} (no 'linkedin' in syndicate field)")
        return

    if meta.get("draft"):
        print(f"⏭  Skipping {qmd_path} (draft)")
        return

    canonical_url = base_url.rstrip("/") + "/" + post_slug(qmd_path)
    title         = meta.get("title", "New post")
    abstract      = meta.get("abstract", "").strip()
    text          = build_post_text(meta, canonical_url)

    access_token = os.environ["LINKEDIN_ACCESS_TOKEN"]
    person_urn   = os.environ["LINKEDIN_PERSON_URN"]

    resp = post_to_linkedin(text, canonical_url, title, abstract,
                            access_token, person_urn)

    if resp.status_code == 401:
        print("🔄 Access token expired — refreshing…")
        access_token = refresh_access_token()
        resp = post_to_linkedin(text, canonical_url, title, abstract,
                                access_token, person_urn)

    if resp.status_code in (200, 201):
        post_urn = resp.headers.get("X-RestLi-Id", resp.json().get("id", "?"))
        print(f"✅ Posted to LinkedIn: {post_urn}")
        print(f"   {canonical_url}")
    else:
        print(f"❌ LinkedIn API error {resp.status_code}: {resp.text}",
              file=sys.stderr)
        sys.exit(1)


# ── CLI ───────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Syndicate a Quarto post to LinkedIn.")
    parser.add_argument("--post",     required=True, help="Path to the .qmd file")
    parser.add_argument("--base-url", required=True, help="Canonical site base URL")
    args = parser.parse_args()
    syndicate(args.post, args.base_url)
