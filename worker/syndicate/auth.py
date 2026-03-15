#!/usr/bin/env python3
"""
One-time LinkedIn OAuth helper.

Run this locally to obtain your access + refresh tokens, then store them as
GitHub Actions secrets.

Usage:
    pip install requests
    python auth.py --client-id <ID> --client-secret <SECRET>

The script opens your browser to the LinkedIn authorization page, waits for
you to paste back the redirected URL, then exchanges the code for tokens and
prints everything you need to store as GitHub secrets.
"""

import argparse
import sys
import webbrowser
from urllib.parse import urlencode, urlparse, parse_qs

import requests

AUTH_URL  = "https://www.linkedin.com/oauth/v2/authorization"
TOKEN_URL = "https://www.linkedin.com/oauth/v2/accessToken"
REDIRECT  = "http://localhost:8080/callback"   # must match your LinkedIn app settings
SCOPES    = ["openid", "profile", "w_member_social"]


def get_auth_url(client_id: str) -> str:
    params = {
        "response_type": "code",
        "client_id":     client_id,
        "redirect_uri":  REDIRECT,
        "scope":         " ".join(SCOPES),
        "state":         "posse-quarto",
    }
    return AUTH_URL + "?" + urlencode(params)


def exchange_code(code: str, client_id: str, client_secret: str) -> dict:
    resp = requests.post(TOKEN_URL, data={
        "grant_type":    "authorization_code",
        "code":          code,
        "redirect_uri":  REDIRECT,
        "client_id":     client_id,
        "client_secret": client_secret,
    }, timeout=15)
    resp.raise_for_status()
    return resp.json()


def get_person_urn(access_token: str) -> str:
    resp = requests.get(
        "https://api.linkedin.com/v2/userinfo",
        headers={"Authorization": f"Bearer {access_token}"},
        timeout=10,
    )
    resp.raise_for_status()
    sub = resp.json().get("sub", "")
    return f"urn:li:person:{sub}"


def main():
    parser = argparse.ArgumentParser(description="LinkedIn OAuth helper for POSSE setup.")
    parser.add_argument("--client-id",     required=True)
    parser.add_argument("--client-secret", required=True)
    args = parser.parse_args()

    url = get_auth_url(args.client_id)
    print("\n🔗 Opening LinkedIn authorization page in your browser…")
    print(f"   If it doesn't open automatically, visit:\n   {url}\n")
    webbrowser.open(url)

    print("After authorizing, LinkedIn will redirect to a localhost URL that")
    print("won't load (that's fine). Copy the full URL from your browser and")
    print("paste it here.\n")
    redirected = input("Paste the redirect URL: ").strip()

    qs   = parse_qs(urlparse(redirected).query)
    code = qs.get("code", [None])[0]
    if not code:
        print("❌ Could not find 'code' in the URL.", file=sys.stderr)
        sys.exit(1)

    print("\n⏳ Exchanging authorization code for tokens…")
    tokens = exchange_code(code, args.client_id, args.client_secret)
    access_token  = tokens.get("access_token")
    refresh_token = tokens.get("refresh_token")

    print("\n⏳ Fetching your LinkedIn person URN…")
    person_urn = get_person_urn(access_token)

    print("\n" + "═" * 60)
    print("✅  OAuth complete! Add these as GitHub Actions secrets:")
    print("═" * 60)
    print(f"\n  LINKEDIN_ACCESS_TOKEN   = {access_token}")
    print(f"  LINKEDIN_REFRESH_TOKEN  = {refresh_token or '(not returned — check app settings)'}")
    print(f"  LINKEDIN_CLIENT_ID      = {args.client_id}")
    print(f"  LINKEDIN_CLIENT_SECRET  = {args.client_secret}")
    print(f"  LINKEDIN_PERSON_URN     = {person_urn}")
    print("\nStore them with:")
    print("  gh secret set LINKEDIN_ACCESS_TOKEN  --body '<value>'")
    print("  gh secret set LINKEDIN_REFRESH_TOKEN --body '<value>'")
    print("  gh secret set LINKEDIN_CLIENT_ID     --body '<value>'")
    print("  gh secret set LINKEDIN_CLIENT_SECRET --body '<value>'")
    print("  gh secret set LINKEDIN_PERSON_URN    --body '<value>'")
    print("═" * 60 + "\n")


if __name__ == "__main__":
    main()
