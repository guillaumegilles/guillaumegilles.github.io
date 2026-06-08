#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
04_validate.py — Validation du jeu analytique et rapport de couverture
Exécution : python scripts/04_validate.py

Invariants vérifiés (contrat data-contracts.md §2) :
  - dep_code.nunique() == 96
  - suren_depot_taux.notna().all() → avertissement si false (pas assertion fatale)
  - Couverture ≥ 90 % par variable (sauf gini : ~20 % attendu)
  - Valeurs cohérentes (taux entre 0 et 100, etc.)

Sorties :
  data/processed/coverage_report.csv
"""

import pathlib
import sys

import numpy as np
import pandas as pd

ROOT      = pathlib.Path(__file__).parent.parent
PROCESSED = ROOT / "data" / "processed"


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

# Variables et leurs seuils de couverture acceptable (%)
COVERAGE_THRESHOLDS = {
    "dep_code":           100.0,
    "dep_nom":            100.0,
    "annee":              100.0,
    "suren_depot_nb":      90.0,
    "suren_depot_taux":    90.0,
    "revenu_median_uc":    90.0,
    "taux_pauvrete":       90.0,
    "interdecile_d9d1":    90.0,
    "gini":                 0.0,  # ~20 % attendu — pas d'alerte
    "chomage_taux":        90.0,
    "chomage_taux_t1":     50.0,  # lag : N-1 toujours manquant pour première année
    "rsa_taux":            50.0,  # souvent absent si DREES non disponible
    "prime_activite_taux": 50.0,
    "ass_aspa_taux":       50.0,
    "part_locataires":     90.0,
    "part_hlm":            90.0,
    "taux_surpeuplement":  90.0,
    "part_familles_mono":  90.0,
    "part_menages_1pers":  90.0,
    "part_25_54":          90.0,
    "part_65plus":         90.0,
    "taux_pauvrete_t1":    50.0,
    "score_fragilite":     50.0,
}

# Plages de valeurs cohérentes (min, max)
VALUE_RANGES = {
    "suren_depot_taux":    (0,    200),
    "chomage_taux":        (0,     30),
    "taux_pauvrete":       (0,    100),
    "rsa_taux":            (0,    100),
    "part_locataires":     (0,    100),
    "part_hlm":            (0,    100),
    "part_familles_mono":  (0,    100),
    "revenu_median_uc":    (0, 100000),
    "interdecile_d9d1":    (0,     20),
    "gini":                (0,      1),
}


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    """Retourne 0 si tout est OK, 1 si des avertissements critiques."""
    print("=" * 60)
    print("  04_validate.py — Validation du jeu analytique")
    print("=" * 60)

    # ── Chargement ────────────────────────────────────────────────────────
    dataset_path = PROCESSED / "analytical_dataset.csv"
    if not dataset_path.exists():
        print(f"\n  ✗ FATAL : {dataset_path} introuvable.")
        print("  Exécuter d'abord : python scripts/03_merge.py")
        return 1

    df = pd.read_csv(dataset_path, dtype={"dep_code": str})
    print(f"\n  Dataset chargé : {df.shape[0]} lignes × {df.shape[1]} colonnes")

    warnings_count = 0
    errors_count   = 0

    # ── Invariant 1 : 96 départements ────────────────────────────────────
    print("\n  === Invariants structurels ===")
    n_dep = df["dep_code"].nunique()
    if n_dep == 96:
        print(f"  ✓ dep_code.nunique() == 96")
    elif n_dep < 96:
        print(f"  ✗ ERREUR : seulement {n_dep}/96 départements présents !")
        errors_count += 1
    else:
        print(f"  ⚠️  {n_dep} codes département (> 96 — doublons ou DOM-TOM ?)")
        warnings_count += 1

    # ── Invariant 2 : suren_depot_taux ───────────────────────────────────
    if "suren_depot_taux" in df.columns:
        n_na = df["suren_depot_taux"].isna().sum()
        n_total = len(df)
        if n_na == 0:
            print(f"  ✓ suren_depot_taux : aucune valeur manquante")
        else:
            pct_na = n_na / n_total * 100
            print(f"  ⚠️  suren_depot_taux : {n_na}/{n_total} NaN ({pct_na:.1f}%)")
            if pct_na > 50:
                errors_count += 1
            else:
                warnings_count += 1
        # Valeurs positives
        if df["suren_depot_taux"].dropna().le(0).any():
            n_neg = df["suren_depot_taux"].dropna().le(0).sum()
            print(f"  ⚠️  suren_depot_taux : {n_neg} valeurs ≤ 0")
            warnings_count += 1
        else:
            print(f"  ✓ suren_depot_taux : toutes valeurs > 0 (parmi non-NaN)")
    else:
        print("  ⚠️  suren_depot_taux absente du dataset")
        warnings_count += 1

    # ── Plages de valeurs ─────────────────────────────────────────────────
    print("\n  === Cohérence des valeurs ===")
    for col, (vmin, vmax) in VALUE_RANGES.items():
        if col not in df.columns:
            continue
        series = pd.to_numeric(df[col], errors="coerce").dropna()
        if len(series) == 0:
            continue
        out_range = ((series < vmin) | (series > vmax)).sum()
        if out_range > 0:
            print(
                f"  ⚠️  {col:30s} : {out_range} valeurs hors [{vmin}, {vmax}] "
                f"(min={series.min():.2f}, max={series.max():.2f})"
            )
            warnings_count += 1
        else:
            print(f"  ✓ {col:30s} : valeurs dans [{vmin}, {vmax}]")

    # ── Rapport de couverture ─────────────────────────────────────────────
    print("\n  === Rapport de couverture ===")
    report_rows = []

    for col in df.columns:
        series = df[col]
        n_total  = len(series)
        n_notna  = series.notna().sum()
        coverage = n_notna / n_total * 100 if n_total > 0 else 0.0

        num_series = pd.to_numeric(series, errors="coerce")
        col_min    = float(num_series.min()) if num_series.notna().any() else float("nan")
        col_max    = float(num_series.max()) if num_series.notna().any() else float("nan")
        col_median = float(num_series.median()) if num_series.notna().any() else float("nan")

        threshold = COVERAGE_THRESHOLDS.get(col, 90.0)
        status = "OK" if coverage >= threshold else "WARNING"
        if status == "WARNING" and col == "gini":
            status = "OK (attendu)"

        report_rows.append({
            "variable":        col,
            "n_total":         n_total,
            "n_notna":         n_notna,
            "coverage_pct":    round(coverage, 1),
            "threshold_pct":   threshold,
            "status":          status,
            "min":             round(col_min,    3) if not np.isnan(col_min)    else None,
            "max":             round(col_max,    3) if not np.isnan(col_max)    else None,
            "median":          round(col_median, 3) if not np.isnan(col_median) else None,
        })

        icon = "✓" if status.startswith("OK") else "⚠️ "
        if col in COVERAGE_THRESHOLDS or coverage < 100:
            print(
                f"  {icon} {col:30s}: {coverage:5.1f}% "
                f"(seuil {threshold:.0f}%) — {status}"
            )

        if status == "WARNING":
            warnings_count += 1

    # Export coverage_report.csv
    report_df = pd.DataFrame(report_rows)
    report_path = PROCESSED / "coverage_report.csv"
    report_df.to_csv(report_path, index=False)
    print(f"\n  ✓ coverage_report.csv exporté ({len(report_df)} variables)")

    # ── Résumé ────────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("  Résumé de validation")
    print("=" * 60)
    print(f"  Erreurs   : {errors_count}")
    print(f"  Avertissements : {warnings_count}")

    if errors_count > 0:
        print("\n  ✗ Validation échouée — corriger les erreurs avant analyse")
        return 1
    elif warnings_count > 0:
        print(
            "\n  ⚠️  Validation réussie avec avertissements."
            "\n     Le dataset est utilisable mais certaines variables ont une"
            "\n     couverture insuffisante. Voir coverage_report.csv."
        )
        return 0
    else:
        print("\n  ✓ Validation complète sans erreur ni avertissement !")
        return 0


if __name__ == "__main__":
    sys.exit(main())
