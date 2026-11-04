"""Paramètres du Groupe AUBÉPINE — jeu de comptes consolidés FICTIFS (PCG / CRC 99-02).

Source de vérité unique (research.md R3, R4) : tous les états publiés
(Excel, PDF, fragments markdown, corrigé) sont dérivés de ce fichier par
generate-dataset.py. Ne jamais éditer les sorties à la main.

Montants en k€. Exercices publiés : N-2=2023, N-1=2024, N=2025.
SIREN fictif 999 888 777 : recherche web du 2026-11-04, aucune société
immatriculée trouvée sous ce numéro.
"""

YEARS = [2023, 2024, 2025]  # N-2, N-1, N
TAUX_IMPOT = 0.25  # IS simplifié : 25 % du résultat avant impôt si positif

GROUPE = {
    "nom": "Groupe AUBÉPINE",
    "mere": "AUBÉPINE SA",
    "siren": "999 888 777",
    "forme": "SA au capital de 2 000 k€",
    "siege": "Fictif — France",
    "secteur": "Agro-industrie (transformation de fruits)",
    "cote": False,
}

# Entités. "par_year" = postes d'entrée par exercice ; le reste est calculé.
# Bilan par entité (k€) : actif = immo_brut - dap + stocks + creances
#   (+ participations pour la mère) + disponibilites (figure d'équilibre)
# Passif = capital + reserves + resultat_net + emprunts + dettes
# CR : resultat_exploitation = ca - achats - externes - salaires - dap_charge
ENTITIES = {
    "MERE": {
        "nom": "AUBÉPINE SA", "forme": "SA", "methode": None, "pct": None,
        "capital": 2000, "reserves0": 1000,
        "titres_IG": {"NORD": 1400, "SUD": 1000, "VERGER": 900},  # prix d'acquisition (goodwill positif)
        "titres_MEE0": 90,  # TERROIR à l'acquisition (30 % x 300)
        "par_year": {
            2022: dict(immo=2600, dap=650, stocks=550, creances=750, emprunts=2700,
                       dettes=650, ca=2800, achats=1120, externes=380, salaires=560,
                       dap_charge=250, charges_fin=105, dividendes=100),
            2023: dict(immo=3000, dap=900, stocks=600, creances=800, emprunts=2500,
                       dettes=700, ca=3000, achats=1200, externes=400, salaires=600,
                       dap_charge=250, charges_fin=100, dividendes=100),
            2024: dict(immo=3400, dap=1150, stocks=650, creances=850, emprunts=2300,
                       dettes=750, ca=3200, achats=1280, externes=420, salaires=640,
                       dap_charge=250, charges_fin=95, dividendes=100),
            2025: dict(immo=3800, dap=1400, stocks=700, creances=900, emprunts=2100,
                       dettes=800, ca=3400, achats=1360, externes=440, salaires=680,
                       dap_charge=250, charges_fin=90, dividendes=100),
        },
    },
    "NORD": {
        "nom": "AUBÉPINE NORD SAS", "forme": "SAS", "methode": "IG", "pct": 0.75,
        "capital": 500, "reserves0": 300, "cp_acq": 600,  # CP au 31/12/2022
        "par_year": {
            2022: dict(immo=700, dap=140, stocks=280, creances=240, emprunts=450,
                       dettes=190, ca=1400, achats=660, externes=140, salaires=240,
                       dap_charge=60, charges_fin=22, dividendes=80),
            2023: dict(immo=800, dap=200, stocks=300, creances=250, emprunts=400,
                       dettes=200, ca=1500, achats=700, externes=150, salaires=250,
                       dap_charge=60, charges_fin=20, dividendes=80),
            2024: dict(immo=900, dap=260, stocks=320, creances=270, emprunts=350,
                       dettes=210, ca=1600, achats=740, externes=160, salaires=260,
                       dap_charge=60, charges_fin=18, dividendes=80),
            2025: dict(immo=1000, dap=320, stocks=340, creances=290, emprunts=300,
                       dettes=220, ca=1700, achats=780, externes=170, salaires=270,
                       dap_charge=60, charges_fin=16, dividendes=80),
        },
    },
    "SUD": {
        "nom": "AUBÉPINE SUD SAS", "forme": "SAS", "methode": "IG", "pct": 0.80,
        "capital": 400, "reserves0": 250, "cp_acq": 400,
        "par_year": {
            2022: dict(immo=450, dap=90, stocks=190, creances=170, emprunts=320,
                       dettes=140, ca=950, achats=480, externes=95, salaires=170,
                       dap_charge=30, charges_fin=12, dividendes=60),
            2023: dict(immo=500, dap=120, stocks=200, creances=180, emprunts=300,
                       dettes=150, ca=1000, achats=500, externes=100, salaires=180,
                       dap_charge=30, charges_fin=10, dividendes=60),
            2024: dict(immo=550, dap=150, stocks=220, creances=190, emprunts=280,
                       dettes=160, ca=1100, achats=550, externes=110, salaires=190,
                       dap_charge=30, charges_fin=10, dividendes=60),
            2025: dict(immo=600, dap=180, stocks=240, creances=200, emprunts=260,
                       dettes=170, ca=1200, achats=600, externes=120, salaires=200,
                       dap_charge=30, charges_fin=10, dividendes=60),
        },
    },
    "VERGER": {
        "nom": "VERGER Export SARL", "forme": "SARL", "methode": "IG", "pct": 0.60,
        "capital": 300, "reserves0": 200, "cp_acq": 350,
        "par_year": {
            2022: dict(immo=280, dap=70, stocks=140, creances=190, emprunts=250,
                       dettes=330, ca=750, achats=380, externes=75, salaires=110,
                       dap_charge=20, charges_fin=14, dividendes=40),  # dettes = 130 fournisseurs + 200 prêt mère
            2023: dict(immo=300, dap=90, stocks=150, creances=200, emprunts=230,
                       dettes=340, ca=800, achats=400, externes=80, salaires=120,
                       dap_charge=20, charges_fin=13, dividendes=40),  # dettes = 140 fournisseurs + 200 prêt mère
            2024: dict(immo=330, dap=110, stocks=160, creances=220, emprunts=230,
                       dettes=340, ca=900, achats=450, externes=90, salaires=130,
                       dap_charge=20, charges_fin=11, dividendes=40),
            2025: dict(immo=360, dap=130, stocks=170, creances=240, emprunts=210,
                       dettes=340, ca=1000, achats=500, externes=100, salaires=140,
                       dap_charge=20, charges_fin=10, dividendes=40),
        },
    },
    "TERROIR": {  # mise en équivalence : jamais consolidée ligne à ligne
        "nom": "TERROIR PARTENAIRES SA", "forme": "SA", "methode": "MEE", "pct": 0.30,
        "capital": 200, "reserves0": 100, "cp_acq": 300,
        "par_year": {
            2022: dict(immo=230, dap=40, stocks=90, creances=110, emprunts=100,
                       dettes=75, ca=380, achats=170, externes=50, salaires=65,
                       dap_charge=20, charges_fin=5, dividendes=0),
            2023: dict(immo=250, dap=60, stocks=100, creances=120, emprunts=100,
                       dettes=80, ca=400, achats=180, externes=50, salaires=70,
                       dap_charge=20, charges_fin=5, dividendes=0),
            2024: dict(immo=270, dap=80, stocks=110, creances=130, emprunts=100,
                       dettes=85, ca=420, achats=190, externes=55, salaires=75,
                       dap_charge=20, charges_fin=5, dividendes=0),
            2025: dict(immo=300, dap=100, stocks=120, creances=140, emprunts=100,
                       dettes=90, ca=450, achats=200, externes=60, salaires=80,
                       dap_charge=20, charges_fin=5, dividendes=0),
        },
    },
}

IG_KEYS = ["NORD", "SUD", "VERGER"]  # filiales en intégration globale

# Opérations intragroupe (constantes sur les 3 exercices, documentées en annexe)
INTRA = {
    "vente_mere_nord": 200,      # vente de marchandises mère -> NORD (dans le CA mère et les achats NORD)
    "marge_taux": 0.25,          # marge de la mère sur prix de vente
    "stock_ig_nord": 60,         # stock NORD provenant de la vente IG, à la clôture
    "pret_mere_verger": 200,     # prêt mère -> VERGER (créance mère / dette VERGER)
    "dividendes": {"NORD": 80, "SUD": 60, "VERGER": 40},  # dividendes versés par les filiales
}
