#!/usr/bin/env python3
"""Générateur du jeu de comptes consolidés FICTIFS du Groupe AUBÉPINE (PCG / CRC 99-02).

Source de vérité unique : dataset-params.py (research.md R3). Ce script dérive
tous les états consolidés N-2..N et émet :
  - fragments markdown -> fr/teaching/financial-analysis/donnees/fragments/
  - aubepine-consolide.xlsx / .pdf -> .../donnees/fichiers/
  - figures.json (chiffres clés pour le corrigé)

Usage :
  python scripts/financial-analysis/generate-dataset.py           # génère tout
  python scripts/financial-analysis/generate-dataset.py --check   # vérifie les invariants (exit 0/1)
  python scripts/financial-analysis/generate-dataset.py --seed ID --out DIR   # variante par étudiant (FR-009)

Conventions (cohérentes avec la Quête 2 du cours) :
  - écart d'acquisition au closing = prix des titres - % x CP filiale au closing
  - produits de participation intragroupe éliminés du CR consolidé (contre réserves)
  - vente intragroupe éliminée en totalité (CA et achats), marge latente en stock
    débitée des réserves consolidées
  - impôt consolidé = figure dérivée pour que le résultat consolidé = somme des RN
    individuels - dividendes intragroupe (élimination sans effet d'impôt, simplifié)
"""
import json
import math
import re
import sys
import zipfile
from pathlib import Path

from openpyxl import Workbook, load_workbook

sys.path.insert(0, str(Path(__file__).parent))
from dataset_params import YEARS, TAUX_IMPOT, GROUPE, ENTITIES, IG_KEYS, INTRA

ROOT = Path(__file__).resolve().parents[2]
FR_DIR = ROOT / "fr" / "teaching" / "financial-analysis" / "donnees"
FRAG_DIR = FR_DIR / "fragments"
FILES_DIR = FR_DIR / "fichiers"

OPENING = 2022  # exercice d'ouverture pour le tableau des flux de N-2
ALL_YEARS = [OPENING] + YEARS


def rhu(x):
    """round half up -> int"""
    return int(math.floor(x + 0.5))


# ---------------------------------------------------------------- entity model
def compute_entities():
    ent = {}
    # TERROIR d'abord (la mère en a besoin pour la quote-part MEE)
    order = ["TERROIR"] + IG_KEYS + ["MERE"]
    for key in order:
        e = dict(ENTITIES[key])
        pct = e["pct"]
        for y in ALL_YEARS:
            p = e["par_year"][y]
            expl = p["ca"] - p["achats"] - p["externes"] - p["salaires"] - p["dap_charge"]
            if key == "MERE":
                quote = rhu(ENTITIES["TERROIR"]["pct"] * ent["TERROIR"][y]["rn"]) if y != OPENING else rhu(0.30 * ent["TERROIR"][y]["rn"])
                div_ig = sum(ENTITIES[f]["pct"] * ENTITIES[f]["par_year"][y]["dividendes"] for f in IG_KEYS)
                prod_fin = rhu(div_ig) + quote
            else:
                quote = 0
                prod_fin = 0
            fin = prod_fin - p["charges_fin"]
            rai = expl + fin
            impot = rhu(TAUX_IMPOT * rai) if rai > 0 else 0
            rn = rai - impot
            ent.setdefault(key, {})[y] = dict(p, expl=expl, fin=fin, rai=rai, impot=impot,
                                              rn=rn, quote_mee=quote, prod_fin=prod_fin)
        # réserves : reserves0 = réserves au 31/12/OPENING ; réserves_y = réserves_{y-1} + RN_{y-1} - div_y
        reserves = {OPENING: e["reserves0"]}
        for y in YEARS:
            reserves[y] = reserves[y - 1] + ent[key][y - 1]["rn"] - e["par_year"][y]["dividendes"]
        # titres MEE de la mère
        if key == "MERE":
            titres_mee = {OPENING: e["titres_MEE0"]}
            for y in YEARS:
                titres_mee[y] = titres_mee[y - 1] + ent[key][y]["quote_mee"]
        else:
            titres_mee = {}
        for y in ALL_YEARS:
            d = ent[key][y]
            d["reserves"] = reserves.get(y)
            d["titres_mee"] = titres_mee.get(y)
            participations = (sum(e["titres_IG"].values()) + d["titres_mee"]) if key == "MERE" else 0
            d["participations"] = participations
            passif = e["capital"] + d["reserves"] + d["rn"] + d["emprunts"] + d["dettes"]
            actif_hors_dispo = d["immo"] - d["dap"] + d["stocks"] + d["creances"] + participations
            d["dispo"] = passif - actif_hors_dispo
            d["passif_total"] = passif
            # flux (à partir de N-2)
            if y != OPENING:
                prev = ent[key][y - 1]
                # la quote-part MEE est un produit non décaissé : déduite de la CAF
                d["caf"] = d["rn"] + (d["dap"] - prev["dap"]) - d.get("quote_mee", 0)
                d["var_bfr"] = (d["stocks"] + d["creances"] - d["dettes"]) - (prev["stocks"] + prev["creances"] - prev["dettes"])
                d["inv"] = -(d["immo"] - prev["immo"])
                d["fin_flux"] = (d["emprunts"] + e["capital"]) - (prev["emprunts"] + e["capital"]) - d["dividendes"]
                d["delta_dispo"] = d["dispo"] - prev["dispo"]
        e["data"] = ent[key]
    return ent


# ------------------------------------------------------------- consolidated
def compute_consolidated(ent):
    cons = {}
    for y in ALL_YEARS:  # 2022 sert d'ouverture pour le flux de 2023 ; seules YEARS sont publiées
        m = ent["MERE"][y]
        fils = [ent[k][y] for k in IG_KEYS]
        sum_all = {k: m[k] + sum(f[k] for f in fils) for k in
                   ["immo", "dap", "stocks", "creances", "dispo", "emprunts", "dettes",
                    "ca", "achats", "externes", "salaires", "dap_charge", "charges_fin", "rn"]}
        prix = {k: ENTITIES["MERE"]["titres_IG"][k] for k in IG_KEYS}
        cp_f = {k: ENTITIES[k]["capital"] + ent[k][y]["reserves"] + ent[k][y]["rn"] for k in IG_KEYS}
        mino = {k: rhu((1 - ENTITIES[k]["pct"]) * cp_f[k]) for k in IG_KEYS}
        eaq = {k: prix[k] + mino[k] - cp_f[k] for k in IG_KEYS}  # = prix - % x CP (arrondi entier)
        pct_cp = {k: cp_f[k] - mino[k] for k in IG_KEYS}
        marge = rhu(INTRA["stock_ig_nord"] * INTRA["marge_taux"])
        div_ig = rhu(sum(ENTITIES[k]["pct"] * ENTITIES[k]["par_year"][y]["dividendes"] for k in IG_KEYS))
        # div_ext dérivé de div_ig (et non arrondi indépendamment) pour que
        # div_ig + div_ext = dividendes totaux, sinon l'identité des flux casse
        div_ext = m["dividendes"] + sum(ENTITIES[k]["par_year"][y]["dividendes"] for k in IG_KEYS) - div_ig

        ca = sum_all["ca"] - INTRA["vente_mere_nord"]
        achats = sum_all["achats"] - INTRA["vente_mere_nord"]
        expl = ca - achats - sum_all["externes"] - sum_all["salaires"] - sum_all["dap_charge"]
        prod_fin = m["quote_mee"]
        fin = prod_fin - sum_all["charges_fin"]
        rai = expl + fin
        rn_total = sum_all["rn"] - div_ig  # élimination des dividendes IG (sans effet d'impôt, simplifié)
        impot = rai - rn_total
        mino_result = sum((1 - ENTITIES[k]["pct"]) * ent[k][y]["rn"] for k in IG_KEYS)
        mino_result = rhu(mino_result)
        rn_pg = rn_total - mino_result
        reserves_cons = m["reserves"] + m["rn"] - rn_pg - marge

        bilan_actif = {
            "Immobilisations brutes": sum_all["immo"],
            "Amortissements et dépréciations": -sum_all["dap"],
            "Titres mis en équivalence (TERROIR 30 %)": m["titres_mee"],
            "Écarts d'acquisition": sum(eaq.values()),
            "Stocks": sum_all["stocks"] - marge,
            "Créances clients et comptes rattachés": sum_all["creances"] - INTRA["pret_mere_verger"],
            "Disponibilités": sum_all["dispo"],
        }
        bilan_passif = {
            "Capital social": ENTITIES["MERE"]["capital"],
            "Réserves consolidées": reserves_cons,
            "Résultat net — part du groupe": rn_pg,
            "Intérêts minoritaires": sum(mino.values()),
            "Emprunts et dettes financières": sum_all["emprunts"],
            "Dettes fournisseurs et comptes rattachés": sum_all["dettes"] - INTRA["pret_mere_verger"],
        }
        cr = {
            "Chiffre d'affaires": ca,
            "Achats consommés": -achats,
            "Charges externes": -sum_all["externes"],
            "Salaires et traitements": -sum_all["salaires"],
            "Dotations aux amortissements": -sum_all["dap_charge"],
            "RÉSULTAT D'EXPLOITATION": expl,
            "Quote-part MEE (TERROIR)": prod_fin,
            "Charges financières nettes": -sum_all["charges_fin"],
            "RÉSULTAT AVANT IMPÔT": rai,
            "Impôt sur les bénéfices": -impot,
            "RÉSULTAT NET CONSOLIDÉ": rn_total,
            "dont intérêts minoritaires": mino_result,
            "dont part du groupe": rn_pg,
        }
        cons[y] = dict(
            bilan_actif=bilan_actif, bilan_passif=bilan_passif, cr=cr,
            cp_f=cp_f, mino=mino, eaq=eaq, pct_cp=pct_cp, prix=prix,
            marge=marge, div_ig=div_ig, div_ext=div_ext, rn_total=rn_total,
            mino_result=mino_result, rn_pg=rn_pg, reserves_cons=reserves_cons,
            quote_mee=m["quote_mee"], titres_mee=m["titres_mee"],
            immo_brut=sum_all["immo"], dap=sum_all["dap"],
        )
        # flux consolidé (à partir de N-2 = 2023, l'ouverture étant 2022)
        if y != OPENING:
            prev = cons[y - 1]
            caf = sum(ent[k][y].get("caf", 0) for k in ["MERE"] + IG_KEYS) - div_ig
            bfr = (bilan_actif["Stocks"] + bilan_actif["Créances clients et comptes rattachés"]
                   - bilan_passif["Dettes fournisseurs et comptes rattachés"])
            bfr_prev = (prev["bilan_actif"]["Stocks"] + prev["bilan_actif"]["Créances clients et comptes rattachés"]
                        - prev["bilan_passif"]["Dettes fournisseurs et comptes rattachés"])
            inv = -(sum_all["immo"] - prev["immo_brut"])
            fin_flux = ((sum_all["emprunts"] + ENTITIES["MERE"]["capital"])
                        - (prev["bilan_passif"]["Emprunts et dettes financières"] + ENTITIES["MERE"]["capital"])
                        - div_ext)
            delta_dispo = bilan_actif["Disponibilités"] - prev["bilan_actif"]["Disponibilités"]
            cons[y]["flux"] = {
                "Capacité d'autofinancement (CAF)": caf,
                "Variation du BFR": -(bfr - bfr_prev),
                "Flux d'investissement": inv,
                "Flux de financement": fin_flux,
                "VARIATION DE TRÉSORERIE": caf - (bfr - bfr_prev) + inv + fin_flux,
                "Δ disponibilités du bilan": delta_dispo,
            }
    return cons


# ------------------------------------------------------------------- checks
def check(ent, cons):
    errors = []
    for key in ENTITIES:
        for y in ALL_YEARS:
            d = ent[key][y]
            actif = d["immo"] - d["dap"] + d["stocks"] + d["creances"] + d.get("participations", 0) + d["dispo"]
            if actif != d["passif_total"]:
                errors.append(f"{key} {y}: bilan déséquilibré ({actif} vs {d['passif_total']})")
            if y != OPENING and d["caf"] - d["var_bfr"] + d["inv"] + d["fin_flux"] != d["delta_dispo"]:
                errors.append(f"{key} {y}: flux ne tie pas ({d['caf']-d['var_bfr']+d['inv']+d['fin_flux']} vs {d['delta_dispo']})")
    for y in YEARS:
        c = cons[y]
        if sum(c["bilan_actif"].values()) != sum(c["bilan_passif"].values()):
            errors.append(f"{y}: bilan consolidé déséquilibré ({sum(c['bilan_actif'].values())} vs {sum(c['bilan_passif'].values())})")
        if c["cr"]["RÉSULTAT NET CONSOLIDÉ"] != c["cr"]["dont intérêts minoritaires"] + c["cr"]["dont part du groupe"]:
            errors.append(f"{y}: RN consolidé != mino + part groupe")
        for k in IG_KEYS:
            if c["cp_f"][k] + c["eaq"][k] != c["prix"][k] + c["mino"][k]:
                errors.append(f"{y} {k}: CP + EAQ != prix + mino (écriture d'élimination déséquilibrée)")
        if y != OPENING and "flux" in c and c["flux"]["VARIATION DE TRÉSORERIE"] != c["flux"]["Δ disponibilités du bilan"]:
            errors.append(f"{y}: flux consolidé ne tie pas")
    return errors


# ------------------------------------------------------------------ markdown
def md_table(headers, rows):
    out = ["| " + " | ".join(headers) + " |",
           "|" + "|".join(["---"] * len(headers)) + "|"]
    for r in rows:
        out.append("| " + " | ".join(str(x) for x in r) + " |")
    return "\n".join(out) + "\n"


def fmt(n):
    return f"{n:,}".replace(",", " ")


def emit_fragments(ent, cons):
    FRAG_DIR.mkdir(parents=True, exist_ok=True)
    years = YEARS
    # périmètre
    rows = []
    for k in ["MERE"] + IG_KEYS + ["TERROIR"]:
        e = ENTITIES[k]
        rows.append([e["nom"], e["forme"], "—" if k == "MERE" else f"{int(e['pct']*100)} %",
                     "Mère" if k == "MERE" else e["methode"],
                     "—" if k == "MERE" else fmt(e.get("cp_acq", 0))])
    (FRAG_DIR / "perimetre.md").write_text(
        md_table(["Entité", "Forme", "% d'intérêt", "Méthode", "CP à l'acquisition (k€)"], rows))
    # bilan
    keys_a = list(cons[years[0]]["bilan_actif"].keys())
    keys_p = list(cons[years[0]]["bilan_passif"].keys())
    rows_a = [[k] + [fmt(cons[y]["bilan_actif"][k]) for y in years] for k in keys_a]
    rows_a.append(["**Total actif**"] + [fmt(sum(cons[y]["bilan_actif"].values())) for y in years])
    rows_p = [[k] + [fmt(cons[y]["bilan_passif"][k]) for y in years] for k in keys_p]
    rows_p.append(["**Total passif**"] + [fmt(sum(cons[y]["bilan_passif"].values())) for y in years])
    (FRAG_DIR / "bilan.md").write_text(
        "**Actif (k€)**\n\n" + md_table(["Poste"] + [str(y) for y in years], rows_a)
        + "\n**Passif (k€)**\n\n" + md_table(["Poste"] + [str(y) for y in years], rows_p))
    # CR
    keys = list(cons[years[0]]["cr"].keys())
    rows = [[k] + [fmt(cons[y]["cr"][k]) for y in years] for k in keys]
    (FRAG_DIR / "compte-de-resultat.md").write_text(
        md_table(["Poste (k€)"] + [str(y) for y in years], rows))
    # annexe
    rows = []
    for k in IG_KEYS:
        rows.append([ENTITIES[k]["nom"], f"{int(ENTITIES[k]['pct']*100)} %",
                     fmt(cons[years[0]]["prix"][k]),
                     *[fmt(cons[y]["eaq"][k]) for y in years],
                     *[fmt(cons[y]["mino"][k]) for y in years]])
    (FRAG_DIR / "annexe.md").write_text(
        "### Écarts d'acquisition et intérêts minoritaires (k€)\n\n"
        + md_table(["Filiale", "%", "Prix des titres"] + [f"EAQ {y}" for y in years] + [f"Mino {y}" for y in years], rows)
        + "\n### Opérations intragroupe (constantes, k€)\n\n"
        + md_table(["Opération", "Montant"],
                   [["Vente de marchandises AUBÉPINE SA → AUBÉPINE NORD (dans CA mère / achats NORD)", fmt(INTRA["vente_mere_nord"])],
                    ["Marge de la mère sur la vente intragroupe (25 % du prix de vente)", fmt(rhu(INTRA["vente_mere_nord"] * INTRA["marge_taux"]))],
                    ["Stock NORD provenant de la vente intragroupe à la clôture", fmt(INTRA["stock_ig_nord"])],
                    ["Marge latente en stock à éliminer", fmt(cons[years[0]]["marge"])],
                    ["Prêt AUBÉPINE SA → VERGER Export (créance / dette éliminées)", fmt(INTRA["pret_mere_verger"])],
                    ["Dividendes versés par NORD / SUD / VERGER (dont part mère éliminée)",
                     f"{INTRA['dividendes']['NORD']} / {INTRA['dividendes']['SUD']} / {INTRA['dividendes']['VERGER']} (mère : {fmt(cons[years[0]]['div_ig'])})"],
                    ["Quote-part de résultat TERROIR (30 %, MEE) — gardée au CR consolidé",
                     " / ".join(fmt(cons[y]["quote_mee"]) for y in years)]])
        + "\n### Intérêts minoritaires au résultat (k€)\n\n"
        + md_table(["Filiale", "%"] + [str(y) for y in years],
                   [[ENTITIES[k]["nom"], f"{int(ENTITIES[k]['pct']*100)} %"]
                    + [fmt(rhu((1 - ENTITIES[k]["pct"]) * ent[k][y]["rn"])) for y in years]
                    for k in IG_KEYS]
                   + [["**Total (CR consolidé)**", "—"] + [fmt(cons[y]["mino_result"]) for y in years]]))
    # flux
    flux_years_md = [y for y in years if "flux" in cons[y]]
    if flux_years_md:
        keys = list(cons[flux_years_md[0]]["flux"].keys())
        rows = [[k] + [fmt(cons[y]["flux"][k]) for y in flux_years_md] for k in keys]
        (FRAG_DIR / "flux.md").write_text(
            md_table(["Poste (k€)"] + [str(y) for y in flux_years_md], rows))
    else:
        (FRAG_DIR / "flux.md").write_text("(tableau des flux disponible à partir de N-1)\n")


# ------------------------------------------------------------------ ratios
def compute_ratios(cons):
    """Ratios BdF du cours calculés depuis les états consolidés publiés (SC-003)."""
    out = {}
    for y in YEARS:
        c = cons[y]
        a, p, cr = c["bilan_actif"], c["bilan_passif"], c["cr"]
        f = c.get("flux", {})
        cp_groupe = p["Capital social"] + p["Réserves consolidées"] + p["Résultat net — part du groupe"]
        cp_total = cp_groupe + p["Intérêts minoritaires"]
        immo_net = (a["Immobilisations brutes"] + a["Amortissements et dépréciations"]
                    + a["Écarts d'acquisition"] + a["Titres mis en équivalence (TERROIR 30 %)"])
        cap_engages = cp_total + p["Emprunts et dettes financières"] - a["Disponibilités"]
        bfr = a["Stocks"] + a["Créances clients et comptes rattachés"] - p["Dettes fournisseurs et comptes rattachés"]
        frng = cp_total + p["Emprunts et dettes financières"] - immo_net
        out[y] = {
            "CAF (k€)": f.get("Capacité d'autofinancement (CAF)"),
            "Marge d'exploitation (%)": round(cr["RÉSULTAT D'EXPLOITATION"] / cr["Chiffre d'affaires"] * 100, 2),
            "Marge nette (%)": round(cr["RÉSULTAT NET CONSOLIDÉ"] / cr["Chiffre d'affaires"] * 100, 2),
            "ROE (%)": round(cr["dont part du groupe"] / cp_groupe * 100, 2),
            "ROCE (%)": round(cr["RÉSULTAT D'EXPLOITATION"] / cap_engages * 100, 2),
            "Taux d'endettement (%)": round(p["Emprunts et dettes financières"] / cp_total * 100, 2),
            "Autonomie financière (%)": round(cp_total / sum(p.values()) * 100, 2),
            "FRNG (k€)": frng,
            "BFR (k€)": bfr,
            "Trésorerie nette (k€)": a["Disponibilités"],
        }
    return out


# ------------------------------------------------------------------ corrigé
def emit_corrige(ent, cons, ratios):
    path = ROOT / "fr" / "teaching" / "financial-analysis" / "enseignant" / "corrige-aubepine.qmd"
    path.parent.mkdir(parents=True, exist_ok=True)
    years = YEARS
    L = []
    a = L.append
    a("---")
    a('title: "Corrigé — Groupe AUBÉPINE (page enseignant)"')
    a("date-modified: 2026-11-04")
    a("abstract: |")
    a("  Corrigé complet du fil rouge : éliminations intragroupe, écarts")
    a("  d'acquisition, intérêts minoritaires, états consolidés et ratios")
    a("  Banque de France pour 2023-2025. Données fictives.")
    a("---")
    a("")
    a("> **Données fictives — usage pédagogique uniquement.** Page réservée aux")
    a("> enseignants. Générée par `scripts/financial-analysis/generate-dataset.py`")
    a("> — ne pas éditer à la main.")
    a("")
    a("## Éliminations intragroupe (constantes, k€)")
    a("")
    a(md_table(["Opération", "Montant (k€)"], [
        ["Vente de marchandises AUBÉPINE SA → AUBÉPINE NORD (CA et achats éliminés)", fmt(INTRA["vente_mere_nord"])],
        ["Marge latente en stock éliminée (réserves consolidées)", fmt(cons[years[0]]["marge"])],
        ["Prêt AUBÉPINE SA → VERGER Export (créance / dette éliminées)", fmt(INTRA["pret_mere_verger"])],
        ["Dividendes intragroupe reçus par la mère (éliminés du CR)", fmt(cons[years[0]]["div_ig"])],
    ]))
    a("")
    a("## Écarts d'acquisition et intérêts minoritaires au bilan (k€)")
    a("")
    rows = [[ENTITIES[k]["nom"], f"{int(ENTITIES[k]['pct']*100)} %", fmt(cons[years[0]]["prix"][k])]
            + [fmt(cons[y]["eaq"][k]) for y in years]
            + [fmt(cons[y]["mino"][k]) for y in years] for k in IG_KEYS]
    a(md_table(["Filiale", "%", "Prix des titres"] + [f"EAQ {y}" for y in years] + [f"Mino {y}" for y in years], rows))
    a("")
    a("## Intérêts minoritaires au résultat (k€)")
    a("")
    rows = [[ENTITIES[k]["nom"]] + [fmt(rhu((1 - ENTITIES[k]["pct"]) * ent[k][y]["rn"])) for y in years] for k in IG_KEYS]
    rows.append(["**Total (CR consolidé)**"] + [fmt(cons[y]["mino_result"]) for y in years])
    a(md_table(["Filiale"] + [str(y) for y in years], rows))
    a("")
    a("## Bilan consolidé (k€)")
    a("")
    a("**Actif**")
    a("")
    keys = list(cons[years[0]]["bilan_actif"].keys())
    a(md_table(["Poste"] + [str(y) for y in years],
               [[k] + [fmt(cons[y]["bilan_actif"][k]) for y in years] for k in keys]
               + [["**Total actif**"] + [fmt(sum(cons[y]["bilan_actif"].values())) for y in years]]))
    a("")
    a("**Passif**")
    a("")
    keys = list(cons[years[0]]["bilan_passif"].keys())
    a(md_table(["Poste"] + [str(y) for y in years],
               [[k] + [fmt(cons[y]["bilan_passif"][k]) for y in years] for k in keys]
               + [["**Total passif**"] + [fmt(sum(cons[y]["bilan_passif"].values())) for y in years]]))
    a("")
    a("## Compte de résultat consolidé (k€)")
    a("")
    keys = list(cons[years[0]]["cr"].keys())
    a(md_table(["Poste"] + [str(y) for y in years],
               [[k] + [fmt(cons[y]["cr"][k]) for y in years] for k in keys]))
    a("")
    a("## Tableau des flux de trésorerie (méthode indirecte, k€)")
    a("")
    fy = [y for y in years if "flux" in cons[y]]
    keys = list(cons[fy[0]]["flux"].keys())
    a(md_table(["Poste"] + [str(y) for y in fy],
               [[k] + [fmt(cons[y]["flux"][k]) for y in fy] for k in keys]))
    a("")
    a("## Ratios Banque de France par exercice")
    a("")
    rkeys = list(ratios[years[0]].keys())
    a(md_table(["Ratio"] + [str(y) for y in years],
               [[k] + [f"{ratios[y][k]:,}".replace(",", " ") for y in years] for k in rkeys]))
    a("")
    a("Vérification : `python scripts/financial-analysis/generate-dataset.py --check`")
    a("recalcule tous ces chiffres depuis `dataset_params.py` et doit afficher OK (exit 0).")
    a("")
    path.write_text("\n".join(L) + "\n")
    return path


# ---------------------------------------------------------------------- xlsx
def emit_xlsx(cons, path=None, variant_label=""):
    FILES_DIR.mkdir(parents=True, exist_ok=True)
    wb = Workbook()
    years = YEARS
    disclaimer = "GROUPE AUBÉPINE — DONNÉES FICTIVES — USAGE PÉDAGOGIQUE UNIQUEMENT"
    if variant_label:
        disclaimer += f" — VARIANTE {variant_label}"

    ws = wb.active
    ws.title = "Périmètre"
    ws.append([disclaimer])
    ws.append(["Entité", "Forme", "% d'intérêt", "Méthode", "CP acquisition (k€)"])
    for k in ["MERE"] + IG_KEYS + ["TERROIR"]:
        e = ENTITIES[k]
        ws.append([e["nom"], e["forme"], "—" if k == "MERE" else e["pct"],
                   "Mère" if k == "MERE" else e["methode"], e.get("cp_acq", "")])

    def sheet(name, postes, years_cols):
        ws = wb.create_sheet(name)
        ws.append([disclaimer])
        ws.append(["Poste (k€)"] + [str(y) for y in years_cols])
        for k in postes:
            ws.append([k] + [postes[k][y] if isinstance(postes, dict) and y in postes.get(k, {}) else None for y in years_cols])
        return ws

    # Bilan : postes dict of dict
    ws = wb.create_sheet("Bilan")
    ws.append([disclaimer])
    ws.append(["ACTIF (k€)"] + [str(y) for y in years])
    for k, v in cons[years[0]]["bilan_actif"].items():
        ws.append([k] + [cons[y]["bilan_actif"][k] for y in years])
    ws.append(["Total actif"] + [sum(cons[y]["bilan_actif"].values()) for y in years])
    ws.append([])
    ws.append(["PASSIF (k€)"] + [str(y) for y in years])
    for k in cons[years[0]]["bilan_passif"]:
        ws.append([k] + [cons[y]["bilan_passif"][k] for y in years])
    ws.append(["Total passif"] + [sum(cons[y]["bilan_passif"].values()) for y in years])

    ws = wb.create_sheet("Compte de résultat")
    ws.append([disclaimer])
    ws.append(["Poste (k€)"] + [str(y) for y in years])
    for k in cons[years[0]]["cr"]:
        ws.append([k] + [cons[y]["cr"][k] for y in years])

    ws = wb.create_sheet("Annexe")
    ws.append([disclaimer])
    ws.append(["Filiale", "%", "Prix titres", "EAQ " + str(years[0]), "EAQ " + str(years[1]), "EAQ " + str(years[2]),
               "Mino " + str(years[0]), "Mino " + str(years[1]), "Mino " + str(years[2])])
    for k in IG_KEYS:
        ws.append([ENTITIES[k]["nom"], ENTITIES[k]["pct"], cons[years[0]]["prix"][k]]
                  + [cons[y]["eaq"][k] for y in years] + [cons[y]["mino"][k] for y in years])
    ws.append([])
    ws.append(["Opérations intragroupe (constantes)", "Montant (k€)"])
    ws.append(["Vente mère → NORD", INTRA["vente_mere_nord"]])
    ws.append(["Marge latente en stock", cons[years[0]]["marge"]])
    ws.append(["Prêt mère → VERGER", INTRA["pret_mere_verger"]])
    ws.append(["Dividendes IG reçus par la mère (éliminés)", cons[years[0]]["div_ig"]])

    ws = wb.create_sheet("Flux")
    ws.append([disclaimer])
    flux_years = [y for y in years if "flux" in cons[y]]
    ws.append(["Poste (k€)"] + [str(y) for y in flux_years])
    for k in cons[flux_years[0]]["flux"]:
        ws.append([k] + [cons[y]["flux"][k] for y in flux_years])

    if path is None:
        path = FILES_DIR / "aubepine-consolide.xlsx"
    import datetime
    wb.properties.created = datetime.datetime(2026, 1, 1)
    wb.properties.modified = datetime.datetime(2026, 1, 1)
    wb.properties.creator = "generate-dataset.py"
    wb.save(path)
    # zip déterministe (timestamps normalisés)
    tmp = path.with_suffix(".tmp.xlsx")
    with zipfile.ZipFile(path) as zin, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == "docProps/core.xml":
                # openpyxl écrit l'heure courante dans dcterms:modified au save
                data = re.sub(
                    rb"<dcterms:modified[^>]*>[^<]*</dcterms:modified>",
                    b'<dcterms:modified xmlns:dcterms="http://purl.org/dc/terms/" '
                    b'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" '
                    b'xsi:type="dcterms:W3CDTF">2026-01-01T00:00:00Z</dcterms:modified>',
                    data)
            zi = zipfile.ZipInfo(item.filename, date_time=(1980, 1, 1, 0, 0, 0))
            zi.compress_type = zipfile.ZIP_DEFLATED
            zout.writestr(zi, data)
    tmp.replace(path)
    return path


# ----------------------------------------------------------------------- pdf
def emit_pdf(cons):
    """PDF texte minimal déterministe (police cœur Helvetica, pas d'embed)."""
    FILES_DIR.mkdir(parents=True, exist_ok=True)
    lines = ["GROUPE AUBÉPINE — COMPTES CONSOLIDÉS FICTIFS (PCG / CRC 99-02)",
             "DONNÉES FICTIVES — USAGE PÉDAGOGIQUE UNIQUEMENT", ""]
    years = YEARS
    lines.append("BILAN CONSOLIDÉ (k€)")
    lines.append("Poste | " + " | ".join(str(y) for y in years))
    for k in cons[years[0]]["bilan_actif"]:
        lines.append(k + " | " + " | ".join(fmt(cons[y]["bilan_actif"][k]) for y in years))
    lines.append("Total actif | " + " | ".join(fmt(sum(cons[y]["bilan_actif"].values())) for y in years))
    for k in cons[years[0]]["bilan_passif"]:
        lines.append(k + " | " + " | ".join(fmt(cons[y]["bilan_passif"][k]) for y in years))
    lines.append("Total passif | " + " | ".join(fmt(sum(cons[y]["bilan_passif"].values())) for y in years))
    lines += ["", "COMPTE DE RÉSULTAT CONSOLIDÉ (k€)", "Poste | " + " | ".join(str(y) for y in years)]
    for k in cons[years[0]]["cr"]:
        lines.append(k + " | " + " | ".join(fmt(cons[y]["cr"][k]) for y in years))
    flux_years = [y for y in years if "flux" in cons[y]]
    if flux_years:
        lines += ["", "TABLEAU DES FLUX DE TRÉSORERIE (k€)", "Poste | " + " | ".join(str(y) for y in flux_years)]
        for k in cons[flux_years[0]]["flux"]:
            lines.append(k + " | " + " | ".join(fmt(cons[y]["flux"][k]) for y in flux_years))

    def esc(s):
        return s.replace("\\", r"\\").replace("(", r"\(").replace(")", r"\)")

    # pagination : 48 lignes par page
    pages, cur = [], []
    for ln in lines:
        if len(cur) >= 48:
            pages.append(cur)
            cur = []
        cur.append(ln)
    pages.append(cur)

    objs = []
    n_pages = len(pages)
    kids = " ".join(f"{3 + 2*i} 0 R" for i in range(n_pages))
    objs.append("<< /Type /Catalog /Pages 2 0 R >>")
    objs.append(f"<< /Type /Pages /Kids [{kids}] /Count {n_pages} >>")
    font_id = 3 + 2 * n_pages
    objs.append("<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>")
    for i, pg in enumerate(pages):
        content_id = 4 + 2 * i
        page_id = 3 + 2 * i
        stream = "BT /F1 9 Tf 40 800 Td 12 TL\n" + "".join(f"({esc(l)}) Tj T*\n" for l in pg) + "ET"
        objs.append(f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 595 842] /Resources << /Font << /F1 {font_id} 0 R >> >> /Contents {content_id} 0 R >>")
        objs.append(f"<< /Length {len(stream)} >>\nstream\n{stream}\nendstream")

    out = bytearray(b"%PDF-1.4\n")
    offsets = [0]
    for i, body in enumerate(objs, start=1):
        offsets.append(len(out))
        out += f"{i} 0 obj\n{body}\nendobj\n".encode()
    xref_pos = len(out)
    out += f"xref\n0 {len(objs)+1}\n0000000000 65535 f \n".encode()
    for off in offsets[1:]:
        out += f"{off:010d} 00000 n \n".encode()
    out += f"trailer\n<< /Size {len(objs)+1} /Root 1 0 R >>\nstartxref\n{xref_pos}\n%%EOF\n".encode()
    path = FILES_DIR / "aubepine-consolide.pdf"
    path.write_bytes(bytes(out))
    return path


# ------------------------------------------------------------------ check xlsx
def check_xlsx(path=None):
    if path is None:
        path = FILES_DIR / "aubepine-consolide.xlsx"
    if not path.exists():
        return [f"{path} absent — lancer le générateur d'abord"]
    wb = load_workbook(path)
    errors = []
    years = YEARS
    ws = wb["Bilan"]
    rows = {r[0].value: [c.value for c in r[1:]] for r in ws.iter_rows(min_row=3) if r[0].value}
    for i, y in enumerate(years):
        ta = rows.get("Total actif")
        tp = rows.get("Total passif")
        if ta is None or tp is None:
            errors.append("lignes Total actif/Total passif manquantes")
        elif ta[i] != tp[i]:
            errors.append(f"bilan {y}: total actif {ta[i]} != total passif {tp[i]}")
    ws = wb["Flux"]
    frows = {r[0].value: [c.value for c in r[1:]] for r in ws.iter_rows(min_row=3) if r[0].value}
    for i, y in enumerate(years):
        var = frows.get("VARIATION DE TRÉSORERIE")
        dd = frows.get("Δ disponibilités du bilan")
        if var and dd and var[i] != dd[i]:
            errors.append(f"flux {y}: variation {var[i]} != Δ dispo {dd[i]}")
    return errors


def apply_seed(seed):
    """Shifts documentés (R5), déterministes depuis le seed : CA VERGER,
    stock AUBÉPINE NORD, taux de marge intragroupe, dividende NORD."""
    import hashlib
    h = hashlib.sha256(seed.encode("utf-8")).digest()
    ca_pct = (h[0] % 9) - 4               # -4..+4 % sur le CA de VERGER
    stock_shift = (h[1] % 21) - 10         # -10..+10 k€ sur le stock de NORD
    marge_shift = ((h[2] % 5) - 2) * 0.01  # -2..+2 points de marge intragroupe
    div_shift = (h[3] % 21) - 10           # -10..+10 k€ sur le dividende de NORD
    INTRA["marge_taux"] = round(0.25 + marge_shift, 4)
    for y in ALL_YEARS:
        v = ENTITIES["VERGER"]["par_year"][y]
        v["ca"] = rhu(rhu(v["ca"] * (1 + ca_pct / 100)) / 10) * 10
        ENTITIES["NORD"]["par_year"][y]["stocks"] += stock_shift
        ENTITIES["NORD"]["par_year"][y]["dividendes"] += div_shift


def main():
    args = sys.argv[1:]
    if "--check" in args:
        ent = compute_entities()
        cons = compute_consolidated(ent)
        errors = check(ent, cons) + check_xlsx()
        if errors:
            for e in errors:
                print("FAIL:", e)
            sys.exit(1)
        print(f"OK: {len(ALL_YEARS)} exercices x {len(ENTITIES)} entités, tous les invariants passent "
              f"(bilans équilibrés, flux ties, EAQ+mino=prix, RN=mino+part groupe)")
        sys.exit(0)
    if "--seed" in args:
        seed = args[args.index("--seed") + 1]
        out = Path(args[args.index("--out") + 1]) if "--out" in args else Path(".")
        out.mkdir(parents=True, exist_ok=True)
        apply_seed(seed)
        ent = compute_entities()
        cons = compute_consolidated(ent)
        errors = check(ent, cons)
        if errors:
            for e in errors:
                print("FAIL:", e)
            sys.exit(1)
        xlsx = emit_xlsx(cons, path=out / f"aubepine-variante-{seed}.xlsx", variant_label=seed)
        errors = check_xlsx(xlsx)
        if errors:
            for e in errors:
                print("FAIL:", e)
            sys.exit(1)
        print(f"OK variante seed={seed} : tous les invariants passent -> {xlsx}")
        sys.exit(0)
    ent = compute_entities()
    cons = compute_consolidated(ent)
    errors = check(ent, cons)
    if errors:
        for e in errors:
            print("FAIL:", e)
        sys.exit(1)
    ratios = compute_ratios(cons)
    emit_fragments(ent, cons)
    xlsx = emit_xlsx(cons)
    pdf = emit_pdf(cons)
    corrige = emit_corrige(ent, cons, ratios)
    figures = {}
    for y in YEARS:
        figures[str(y)] = dict(cons[y])
        figures[str(y)]["ratios"] = ratios[y]
    (FRAG_DIR / "figures.json").write_text(json.dumps(figures, ensure_ascii=False, indent=1, default=str))
    print(f"Généré: {xlsx.relative_to(ROOT)}")
    print(f"Généré: {pdf.relative_to(ROOT)}")
    print(f"Généré: {corrige.relative_to(ROOT)}")
    print(f"Fragments: {FRAG_DIR.relative_to(ROOT)}/*.md + figures.json")


if __name__ == "__main__":
    main()
