#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
01_download.py — Téléchargement de toutes les sources de données
Exécution : python scripts/01_download.py

Sources :
  - Banque de France : surendettement départemental via API WebStat (ODS)
  - INSEE FiLoSoFi 2021 + SUPRA 2019
  - INSEE Chômage localisé (TCRD)
  - INSEE RP 2022 (populations de référence + bases infracommunales logement/ménages/population)
  - DREES / France Travail : minimas sociaux (RSA, prime d'activité)
  - GeoJSON départements (gregoiredavid/france-geojson)
"""

import requests
import urllib.parse
import zipfile
import io
import pathlib

ROOT = pathlib.Path(__file__).parent.parent
RAW  = ROOT / "data" / "raw"
GEO  = ROOT / "data" / "geo"

# ---------------------------------------------------------------------------
# BdF WebStat API — clé publique intégrée dans le bundle JavaScript WebStat
# ---------------------------------------------------------------------------
BDF_APIKEY = "a78150367a35332580ae1651b4023f0c333e99b6653821d6ac445af9"

# ---------------------------------------------------------------------------
# Headers anti-bot pour INSEE
# ---------------------------------------------------------------------------
HEADERS_INSEE = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0"
    ),
    "Referer":    "https://www.insee.fr/fr/statistiques/2012804",
    "Accept":     (
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,*/*"
    ),
}

RESULTS: dict[str, bool] = {}   # label → succès


# ---------------------------------------------------------------------------
# Fonctions utilitaires
# ---------------------------------------------------------------------------

def download_file(url: str, dest, headers: dict | None = None, label: str = "") -> bool:
    """Télécharge un fichier si non déjà présent. Retourne True si succès."""
    dest = pathlib.Path(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists():
        print(f"  ✓ Déjà présent : {dest.name}")
        RESULTS[label or dest.name] = True
        return True
    print(f"  ↓ Téléchargement {label or dest.name} …")
    try:
        resp = requests.get(url, headers=headers, timeout=60, stream=True)
        resp.raise_for_status()
        with open(dest, "wb") as f:
            for chunk in resp.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"  ✓ {dest.name} ({dest.stat().st_size // 1024} Ko)")
        RESULTS[label or dest.name] = True
        return True
    except Exception as exc:
        print(f"  ✗ ERREUR {label or dest.name} : {exc}")
        RESULTS[label or dest.name] = False
        return False


def download_zip(
    url: str, dest_dir, label: str = "", headers: dict | None = None,
    retries: int = 3
) -> bool:
    """Télécharge et décompresse un ZIP via curl (robuste SSL). Retourne True si succès."""
    import time
    import subprocess
    import tempfile
    dest_dir = pathlib.Path(dest_dir)
    dest_dir.mkdir(parents=True, exist_ok=True)
    print(f"  ↓ Téléchargement ZIP {label} …")

    tmp_path = None
    for attempt in range(1, retries + 1):
        try:
            with tempfile.NamedTemporaryFile(suffix=".zip", delete=False) as tmp:
                tmp_path = pathlib.Path(tmp.name)

            cmd = [
                "curl", "-L", "--fail", "--retry", "2", "--retry-delay", "3",
                "--connect-timeout", "30", "--max-time", "300",
                "-o", str(tmp_path), "--silent", "--show-error",
            ]
            if headers:
                for k, v in headers.items():
                    cmd += ["-H", f"{k}: {v}"]
            cmd.append(url)

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=360)
            if result.returncode != 0:
                raise RuntimeError(result.stderr.strip() or f"curl exit {result.returncode}")

            with zipfile.ZipFile(tmp_path) as z:
                z.extractall(dest_dir)
            tmp_path.unlink(missing_ok=True)
            print(f"  ✓ ZIP extrait dans {dest_dir}")
            RESULTS[label] = True
            return True
        except Exception as exc:
            if tmp_path and tmp_path.exists():
                tmp_path.unlink(missing_ok=True)
            if attempt < retries:
                wait = 2 ** attempt
                print(f"  ⚠️  Tentative {attempt}/{retries} échouée ({exc}). Nouvelle tentative dans {wait}s…")
                time.sleep(wait)
            else:
                print(f"  ✗ ERREUR ZIP {label} : {exc}")
                RESULTS[label] = False
                return False


# ---------------------------------------------------------------------------
# T005 — Bloc BdF : API WebStat (OpenDataSoft) — surendettement mensuel
# ---------------------------------------------------------------------------

def download_bdf():
    """Télécharge les dépôts de dossiers de surendettement BdF via l'API WebStat.

    Utilise l'endpoint ODS export/csv du dataset ``observations`` avec une
    clé API publique intégrée dans le bundle JavaScript de webstat.banque-france.fr.
    Couvre 96 départements métropolitains, données mensuelles depuis 2019-01.
    Résultat : data/raw/bdf/surendettement_api.csv (délimiteur ;).
    """
    print("\n=== BdF — Surendettement WebStat API ===")
    dest = RAW / "bdf" / "surendettement_api.csv"
    dest.parent.mkdir(parents=True, exist_ok=True)

    if dest.exists():
        print(f"  ✓ Déjà présent : {dest.name}")
        RESULTS["BdF surendettement API"] = True
        return

    # 96 codes départementaux métropolitains (hors DOM, hors total national)
    dep_codes = (
        [f"{n:02d}" for n in range(1, 20)]   # D01–D19
        + ["2A", "2B"]                         # Corse
        + [f"{n:02d}" for n in range(21, 96)]  # D21–D95
    )
    series_keys = [f"IFI.M.D{c}.SUREN.DEPOT" for c in dep_codes]
    keys_sql = ", ".join(f'"{k}"' for k in series_keys)
    where = f"series_key IN ({keys_sql})"

    params = urllib.parse.urlencode({
        "where":    where,
        "select":   "series_key,time_period,obs_value",
        "order_by": "series_key,time_period",
        "delimiter": ";",
    })
    url = (
        "https://webstat.banque-france.fr/api/explore/v2.1/catalog/datasets/"
        f"observations/exports/csv/?{params}"
    )
    headers = {
        "Authorization": f"Apikey {BDF_APIKEY}",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:120.0) Gecko/20100101 Firefox/120.0",
    }

    print(f"  ↓ API WebStat BdF ({len(series_keys)} séries) …")
    try:
        resp = requests.get(url, headers=headers, timeout=120)
        resp.raise_for_status()
        with open(dest, "wb") as f:
            f.write(resp.content)
        lines = resp.text.count("\n")
        print(f"  ✓ {dest.name} ({dest.stat().st_size // 1024} Ko, ~{lines} lignes)")
        RESULTS["BdF surendettement API"] = True
    except Exception as exc:
        print(f"  ✗ ERREUR API BdF : {exc}")
        RESULTS["BdF surendettement API"] = False


# ---------------------------------------------------------------------------
# T006 — Bloc FiLoSoFi : revenus et inégalités départementales
# ---------------------------------------------------------------------------

def download_filosofi():
    """Télécharge les fichiers FiLoSoFi 2023 (format long, tous niveaux géographiques)."""
    print("\n=== INSEE — FiLoSoFi ===")
    dest_dir = RAW / "filosofi"

    # Passer si le fichier 2023 est déjà présent
    already = list(dest_dir.glob("DS_FILOSOFI_CC_2023_data.csv"))
    if already:
        print(f"  ✓ Déjà présent : {already[0].name}")
        RESULTS["FiLoSoFi 2023"] = True
    else:
        download_zip(
            "https://www.insee.fr/fr/statistiques/fichier/8984752/FILOSOFI_CC_csv.zip",
            dest_dir,
            label="FiLoSoFi 2023",
            headers=HEADERS_INSEE,
        )


# ---------------------------------------------------------------------------
# T007 — Bloc chômage localisé INSEE (TCRD)
# ---------------------------------------------------------------------------

def download_chomage():
    """Télécharge les fichiers chômage localisé INSEE (TCRD).
    Affiche un avertissement et l'URL manuelle si le téléchargement échoue.
    """
    print("\n=== INSEE — Chômage localisé (TCRD) ===")
    dest_dir = RAW / "chomage"

    urls_tcrd = [
        "https://www.insee.fr/fr/statistiques/fichier/2012804/TCRD_025.zip",
        "https://www.insee.fr/fr/statistiques/fichier/2012804/TCRD_025.xls",
    ]

    success = False
    for url in urls_tcrd:
        filename = pathlib.Path(url).name
        dest = dest_dir / filename
        if dest.exists():
            print(f"  ✓ Déjà présent : {dest.name}")
            RESULTS["Chômage TCRD"] = True
            success = True
            break
        print(f"  ↓ Tentative : {url}")
        try:
            resp = requests.get(url, headers=HEADERS_INSEE, timeout=60, stream=True)
            resp.raise_for_status()
            # Si c'est un ZIP, décompresser
            if url.endswith(".zip"):
                with zipfile.ZipFile(io.BytesIO(resp.content)) as z:
                    z.extractall(dest_dir)
                print(f"  ✓ ZIP extrait dans {dest_dir}")
            else:
                dest_dir.mkdir(parents=True, exist_ok=True)
                with open(dest, "wb") as f:
                    for chunk in resp.iter_content(chunk_size=8192):
                        f.write(chunk)
                print(f"  ✓ {dest.name} ({dest.stat().st_size // 1024} Ko)")
            RESULTS["Chômage TCRD"] = True
            success = True
            break
        except Exception as exc:
            print(f"  ✗ Échec ({exc})")

    if not success:
        print(
            "\n  ⚠️  Téléchargement TCRD bloqué (protection anti-bot INSEE)."
            "\n  Télécharger manuellement depuis :"
            "\n    https://www.insee.fr/fr/statistiques/2012804"
            "\n  et placer le fichier Excel dans : data/raw/chomage/"
        )
        RESULTS["Chômage TCRD"] = False


# ---------------------------------------------------------------------------
# T008 — Bloc RP 2022 : populations de référence + bases infracommunales
# Bases infracommunales publiées en octobre 2025.
# Sources :
#   - Pop. de référence : https://www.insee.fr/fr/statistiques/8290607?sommaire=8290669
#   - Logement          : https://www.insee.fr/fr/statistiques/8647012
#   - Ménages/Familles  : https://www.insee.fr/fr/statistiques/8647008
#   - Population        : https://www.insee.fr/fr/statistiques/8647014
# ---------------------------------------------------------------------------

def download_rp():
    """Télécharge les populations de référence RP 2022 et les bases infracommunales."""
    print("\n=== INSEE — RP 2022 (populations de référence + bases infracommunales) ===")
    dest_dir = RAW / "rp"
    dest_dir.mkdir(parents=True, exist_ok=True)

    # Populations de référence (agrégat départemental)
    url = "https://www.insee.fr/fr/statistiques/fichier/8290591/ensemble.zip"
    already = list(dest_dir.glob("donnees_departements.csv"))
    if already:
        print(f"  ✓ Déjà présent : {already[0].name}")
        RESULTS["RP pop ref 2022"] = True
    else:
        download_zip(url, dest_dir, label="RP pop ref 2022", headers=HEADERS_INSEE)

    # Bases infracommunales (IRIS) — format CSV dans ZIP, ~30-50 Mo chacune
    infra_bases = [
        (
            "base-ic-logement-2022_csv.zip",
            "https://www.insee.fr/fr/statistiques/fichier/8647012/base-ic-logement-2022_csv.zip",
            "RP 2022 logement",
        ),
        (
            "base-ic-couples-familles-menages-2022_csv.zip",
            "https://www.insee.fr/fr/statistiques/fichier/8647008/"
            "base-ic-couples-familles-menages-2022_csv.zip",
            "RP 2022 ménages",
        ),
        (
            "base-ic-evol-struct-pop-2022_csv.zip",
            "https://www.insee.fr/fr/statistiques/fichier/8647014/"
            "base-ic-evol-struct-pop-2022_csv.zip",
            "RP 2022 population",
        ),
    ]
    for fname, url_infra, label in infra_bases:
        dest = dest_dir / fname
        download_file(url_infra, dest, headers=HEADERS_INSEE, label=label)


# ---------------------------------------------------------------------------
# T009 — Bloc minimas sociaux (DREES open data)
# Source : https://data.drees.solidarites-sante.gouv.fr/explore/dataset/
#          donnees-mensuelles-sur-les-prestations-de-solidarite/information/
# ---------------------------------------------------------------------------

def download_minimas():
    """Télécharge le suivi mensuel des prestations de solidarité DREES (RSA, ASS, prime d'activité)."""
    print("\n=== DREES — Prestations de solidarité (RSA, ASS, prime d'activité) ===")
    dest_dir = RAW / "minimas"
    dest_dir.mkdir(parents=True, exist_ok=True)

    dest = dest_dir / "drees_prestations_solidarite.xlsx"
    if dest.exists():
        print(f"  ✓ Déjà présent : {dest.name}")
        RESULTS["DREES minimas sociaux"] = True
        return

    # L'API OpenDataSoft expose le fichier comme pièce jointe
    url = (
        "https://data.drees.solidarites-sante.gouv.fr/api/explore/v2.1/catalog/"
        "datasets/donnees-mensuelles-sur-les-prestations-de-solidarite/attachments/"
        "donnees_mensuelles_prestations_solidarite_fevrier26_xlsx"
    )
    try:
        resp = requests.get(url, timeout=120, stream=True, headers=HEADERS_INSEE)
        resp.raise_for_status()
        with open(dest, "wb") as f:
            for chunk in resp.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"  ✓ {dest.name} ({dest.stat().st_size // 1024} Ko)")
        RESULTS["DREES minimas sociaux"] = True
    except Exception as exc:
        print(f"  ✗ Téléchargement DREES : {exc}")
        print(
            "\n  ⚠️  Téléchargement échoué."
            "\n  Télécharger manuellement depuis :"
            "\n    https://data.drees.solidarites-sante.gouv.fr/explore/dataset/"
            "donnees-mensuelles-sur-les-prestations-de-solidarite/"
            "\n  Placer le fichier dans : data/raw/minimas/"
        )
        RESULTS["DREES minimas sociaux"] = False


# ---------------------------------------------------------------------------
# T010 — Bloc GeoJSON : contours départements
# ---------------------------------------------------------------------------

def download_geo():
    """Télécharge le GeoJSON des départements métropolitains (version simplifiée)."""
    print("\n=== GeoJSON — Départements France métropolitaine ===")

    GEO_URL = (
        "https://raw.githubusercontent.com/gregoiredavid/france-geojson/"
        "master/departements-version-simplifiee.geojson"
    )
    download_file(GEO_URL, GEO / "departements.geojson", label="GeoJSON départements")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("=" * 60)
    print("  01_download.py — Téléchargement des sources de données")
    print("=" * 60)

    download_bdf()
    download_filosofi()
    download_chomage()
    download_rp()
    download_minimas()
    download_geo()

    # ── Rapport de synthèse ──────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("  Rapport de synthèse")
    print("=" * 60)
    success = [k for k, v in RESULTS.items() if v]
    failed  = [k for k, v in RESULTS.items() if not v]

    print(f"\n  ✓ Réussis  ({len(success)}) : {', '.join(success) if success else '—'}")
    print(f"  ✗ Échoués ({len(failed)}) : {', '.join(failed) if failed else '—'}")

    if failed:
        print(
            "\n  ⚠️  Des sources ont échoué. Le pipeline de nettoyage (02_clean.py)"
            "\n     ignorera gracieusement les fichiers manquants."
        )
    else:
        print("\n  🎉 Tous les téléchargements ont réussi !")

    print()


if __name__ == "__main__":
    main()
