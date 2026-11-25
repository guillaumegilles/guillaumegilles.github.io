#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
03_merge.py — Fusion et construction du jeu analytique
Exécution : python scripts/03_merge.py

Étapes :
  1. Chargement de tous les fichiers intermédiaires (data/processed/*.csv)
  2. Jointure sur (dep_code, annee) — base : surendettement.csv
  3. Construction des lags t-1 EN UNITÉS BRUTES (avant normalisation)
  4. Calcul du score_fragilite (z-scores pondérés)
  5. Export → data/processed/analytical_dataset.csv

Schéma de sortie (25 colonnes minimum) :
  dep_code, dep_nom, reg_code, annee,
  suren_depot_nb, suren_depot_taux,
  revenu_median_uc, taux_pauvrete, interdecile_d9d1, gini,
  chomage_taux, chomage_taux_t1,
  rsa_taux, prime_activite_taux, ass_aspa_taux,
  part_locataires, part_hlm, taux_surpeuplement,
  part_familles_mono, part_menages_1pers,
  part_25_54, part_65plus,
  population_mun,
  taux_pauvrete_t1,
  score_fragilite,
  source_suren, source_filosofi, source_chomage, source_rp
"""

import pathlib
import warnings

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

ROOT      = pathlib.Path(__file__).parent.parent
PROCESSED = ROOT / "data" / "processed"


# ---------------------------------------------------------------------------
# Utilitaires
# ---------------------------------------------------------------------------

def safe_load(fname: str, **kwargs) -> pd.DataFrame:
    """Charge un CSV avec gestion des fichiers manquants ou vides."""
    path = PROCESSED / fname
    if not path.exists():
        print(f"  ⚠️  {fname} non trouvé — ignoré")
        return pd.DataFrame()
    try:
        df = pd.read_csv(path, dtype={"dep_code": str}, **kwargs)
        if df.empty:
            print(f"  ⚠️  {fname} vide — ignoré")
        return df
    except Exception as exc:
        print(f"  ✗ Erreur chargement {fname} : {exc}")
        return pd.DataFrame()


def zscore_col(series: pd.Series) -> pd.Series:
    """Calcule le z-score d'une série, en ignorant les NaN."""
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        vals = series.values.reshape(-1, 1)
        mask = ~np.isnan(vals.flatten())
        result = np.full(len(vals), np.nan)
        if mask.sum() > 1:
            scaler = StandardScaler()
            result[mask] = scaler.fit_transform(vals[mask].reshape(-1, 1)).flatten()
    return pd.Series(result, index=series.index)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("=" * 60)
    print("  03_merge.py — Fusion du jeu analytique")
    print("=" * 60)

    # ── 1. Chargement des sources intermédiaires ─────────────────────────
    print("\n  1. Chargement des fichiers intermédiaires …")

    dep_ref = safe_load("dep_ref.csv")
    suren   = safe_load("surendettement.csv")
    filos   = safe_load("filosofi.csv")
    gini    = safe_load("filosofi_gini.csv")
    chomage = safe_load("chomage.csv")
    pop_ref = safe_load("rp_pop_ref.csv")
    rp_infra = safe_load("rp_infracommunal.csv")
    minimas = safe_load("minimas_sociaux.csv")

    # ── 2. Construction de la base ───────────────────────────────────────
    print("\n  2. Construction de la base …")

    # Si surendettement.csv est vide, construire un squelette 96×années
    if suren.empty or "dep_code" not in suren.columns:
        print("  ⚠️  surendettement.csv vide — construction d'un squelette 96×2021")
        if not dep_ref.empty:
            base = dep_ref[["dep_code", "dep_nom", "reg_code"]].copy()
            base["annee"] = 2021
            base["suren_depot_nb"] = np.nan
        else:
            # Dernier recours
            base = pd.DataFrame({
                "dep_code": [str(i).zfill(2) for i in range(1, 96)],
                "annee":    2021,
                "suren_depot_nb": np.nan,
            })
    else:
        base = suren.copy()
        if not dep_ref.empty and "dep_nom" not in base.columns:
            base = base.merge(
                dep_ref[["dep_code", "dep_nom", "reg_code"]], on="dep_code", how="left"
            )
        elif not dep_ref.empty and "reg_code" not in base.columns:
            base = base.merge(
                dep_ref[["dep_code", "reg_code"]], on="dep_code", how="left"
            )

    print(f"  Base : {len(base)} lignes × {len(base.columns)} colonnes")

    # ── 3. Jointures ─────────────────────────────────────────────────────
    print("\n  3. Jointures sur (dep_code, annee) …")

    def left_join(df: pd.DataFrame, right: pd.DataFrame, cols: list[str],
                  label: str) -> pd.DataFrame:
        if right.empty or "dep_code" not in right.columns:
            print(f"  ⚠️  {label} absent — colonnes NaN")
            for col in cols:
                df[col] = np.nan
            return df
        # Vérifier si la jointure inclut annee
        join_keys = ["dep_code"]
        if "annee" in right.columns and "annee" in df.columns:
            join_keys.append("annee")
        right_keep = join_keys + [c for c in cols if c in right.columns]
        right_sub = right[right_keep].drop_duplicates(subset=join_keys)
        df = df.merge(right_sub, on=join_keys, how="left")
        matched = df[cols[0]].notna().sum() if cols and cols[0] in df.columns else 0
        print(f"  ✓ {label} — {matched}/{len(df)} départements couverts")
        return df

    # FiLoSoFi
    filosofi_cols = [c for c in ["revenu_median_uc", "taux_pauvrete", "interdecile_d9d1"]
                     if not filos.empty and c in filos.columns]
    base = left_join(base, filos, filosofi_cols, "FiLoSoFi 2021")

    # Gini (millésime 2019 — jointure sans annee)
    if not gini.empty and "gini" in gini.columns and "dep_code" in gini.columns:
        gini_sub = gini[["dep_code", "gini"]].drop_duplicates("dep_code")
        base = base.merge(gini_sub, on="dep_code", how="left")
        print(f"  ✓ Gini 2019 — {base['gini'].notna().sum()}/{len(base)} dép. couverts")
    else:
        base["gini"] = np.nan

    # Chômage
    chomage_cols = [c for c in ["chomage_taux"] if not chomage.empty and c in chomage.columns]
    base = left_join(base, chomage, chomage_cols, "Chômage")

    # RP 2022 populations de référence → population_mun
    pop_ref_cols = [c for c in ["population_mun"]
                    if not pop_ref.empty and c in pop_ref.columns]
    base = left_join(base, pop_ref, pop_ref_cols, "RP 2022 pop. référence")

    # RP 2022 bases infracommunales → part_locataires, part_hlm, etc.
    infra_cols = [c for c in ["part_locataires", "part_hlm", "taux_surpeuplement",
                               "part_familles_mono", "part_menages_1pers",
                               "part_25_54", "part_65plus"]
                  if not rp_infra.empty and c in rp_infra.columns]
    if infra_cols:
        base = left_join(base, rp_infra, infra_cols, "RP 2022 infracommunal")
    else:
        for col in ["part_locataires", "part_hlm", "taux_surpeuplement",
                    "part_familles_mono", "part_menages_1pers", "part_25_54", "part_65plus"]:
            if col not in base.columns:
                base[col] = np.nan

    # Minimas sociaux
    min_cols = [c for c in ["rsa_taux", "prime_activite_taux", "ass_aspa_taux"]
                if not minimas.empty and c in minimas.columns]
    base = left_join(base, minimas, min_cols, "Minimas sociaux")

    # ── 4. Dérivations ───────────────────────────────────────────────────
    print("\n  4. Dérivations …")

    # Taux de surendettement pour 10 000 habitants (RP 2022 PMUN comme dénominateur)
    if "suren_depot_nb" in base.columns and "suren_depot_taux" not in base.columns:
        if "population_mun" in base.columns and base["population_mun"].notna().any():
            base["suren_depot_taux"] = (
                base["suren_depot_nb"] / base["population_mun"] * 10_000
            ).round(3)
            print("  ↳ suren_depot_taux = dossiers / 10 000 habitants (RP 2022 PMUN)")
        else:
            base["suren_depot_taux"] = base["suren_depot_nb"]

    # Lags t-1 (EN UNITÉS BRUTES avant normalisation)
    print("  ↳ Construction des lags t-1 …")
    base = base.sort_values(["dep_code", "annee"])
    for lag_col in ["chomage_taux", "taux_pauvrete"]:
        new_col = f"{lag_col}_t1"
        if lag_col in base.columns:
            base[new_col] = base.groupby("dep_code")[lag_col].shift(1)
        else:
            base[new_col] = np.nan

    # ── 5. Score de fragilité ─────────────────────────────────────────────
    print("  ↳ Calcul du score_fragilite …")
    score_components = {
        "chomage_taux":    0.3,
        "taux_pauvrete":   0.3,
        "rsa_taux":        0.2,
        "part_locataires": 0.2,
    }
    z_scores = {}
    for col, weight in score_components.items():
        if col in base.columns:
            z_col = f"{col}_z"
            base[z_col] = zscore_col(base[col].astype(float))
            z_scores[col] = weight
        else:
            base[col] = np.nan
            z_col = f"{col}_z"
            base[z_col] = np.nan

    # Calculer le score (pondéré, avec normalisation si composantes manquantes)
    if z_scores:
        total_weight = sum(z_scores.values())
        score_series = pd.Series(np.zeros(len(base)), index=base.index)
        weight_applied = pd.Series(np.zeros(len(base)), index=base.index)
        for col, weight in z_scores.items():
            z_col = f"{col}_z"
            mask_valid = base[z_col].notna()
            score_series[mask_valid] += base.loc[mask_valid, z_col] * weight
            weight_applied[mask_valid] += weight
        # Normaliser par le poids total effectif
        mask_nonzero = weight_applied > 0
        base["score_fragilite"] = np.nan
        base.loc[mask_nonzero, "score_fragilite"] = (
            score_series[mask_nonzero] / weight_applied[mask_nonzero] * total_weight
        ).round(4)
        print(f"  ✓ score_fragilite calculé pour {base['score_fragilite'].notna().sum()} lignes")
    else:
        base["score_fragilite"] = np.nan

    # Nettoyer les colonnes z-score auxiliaires du dataset final
    z_cols_to_drop = [f"{col}_z" for col in score_components]
    base = base.drop(columns=[c for c in z_cols_to_drop if c in base.columns])

    # ── 6. Export ────────────────────────────────────────────────────────
    print("\n  5. Export …")

    # Assurer que les colonnes essentielles sont présentes (avec NaN si manquantes)
    required_cols = [
        "dep_code", "dep_nom", "reg_code", "annee",
        "suren_depot_nb", "suren_depot_taux",
        "revenu_median_uc", "taux_pauvrete", "interdecile_d9d1", "gini",
        "chomage_taux", "chomage_taux_t1",
        "rsa_taux", "prime_activite_taux", "ass_aspa_taux",
        "population_mun",
        "part_locataires", "part_hlm", "taux_surpeuplement",
        "part_familles_mono", "part_menages_1pers",
        "part_25_54", "part_65plus",
        "taux_pauvrete_t1",
        "score_fragilite",
    ]
    for col in required_cols:
        if col not in base.columns:
            base[col] = np.nan

    # Réordonner les colonnes (required_cols en premier, reste en fin)
    extra_cols = [c for c in base.columns if c not in required_cols]
    final_cols = required_cols + extra_cols
    base = base[[c for c in final_cols if c in base.columns]]

    out_path = PROCESSED / "analytical_dataset.csv"
    base.to_csv(out_path, index=False)

    print(f"\n  ✓ analytical_dataset.csv exporté")
    print(f"    Dimensions : {base.shape[0]} lignes × {base.shape[1]} colonnes")
    print(f"    Départements uniques : {base['dep_code'].nunique()}")
    print(f"    Années : {sorted(base['annee'].unique().tolist())}")

    # Couverture par variable
    print("\n  Couverture par variable :")
    for col in required_cols:
        if col in base.columns:
            pct = base[col].notna().mean() * 100
            status = "✓" if pct >= 90 else ("⚠" if pct >= 20 else "✗")
            print(f"    {status} {col:30s}: {pct:5.1f}%")


if __name__ == "__main__":
    main()
