"""
Démarrage rapide — Projet intégrateur "Livraison"
Chargement, exploration et premières statistiques du dataset

Exécutez ce code ligne par ligne pour vous familiariser avec les données.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ============================================================================
# 1. Charger les données
# ============================================================================

df = pd.read_csv('delivery_data.csv')

# Afficher les premières lignes
print("Premières lignes du dataset :")
print(df.head())
print()

# Info générale
print("Dimensions :", df.shape)
print("Colonnes :", df.columns.tolist())
print()

# ============================================================================
# 2. Résumé statistique (univarié)
# ============================================================================

print("Résumé statistique complet :")
print(df.describe())
print()

# Satisfaction
print("Distribution de la satisfaction :")
print(df['satisfaction'].value_counts().sort_index())
print()

print("Taux de retard :", f"{df['est_retard'].mean():.1%}")
print()

# ============================================================================
# 3. Premières visualisations
# ============================================================================

fig, axes = plt.subplots(2, 3, figsize=(14, 8))

# Histogramme : distance
axes[0, 0].hist(df['distance_km'], bins=30, edgecolor='black', alpha=0.7)
axes[0, 0].set_xlabel('Distance (km)')
axes[0, 0].set_ylabel('Fréquence')
axes[0, 0].set_title('Distribution de la distance')

# Histogramme : montant
axes[0, 1].hist(df['montant_euros'], bins=30, edgecolor='black', alpha=0.7)
axes[0, 1].set_xlabel('Montant (€)')
axes[0, 1].set_ylabel('Fréquence')
axes[0, 1].set_title('Distribution du montant')

# Histogramme : délai total
axes[0, 2].hist(df['delai_total_min'], bins=30, edgecolor='black', alpha=0.7)
axes[0, 2].axvline(45, color='red', linestyle='--', linewidth=2, label='Seuil retard (45 min)')
axes[0, 2].set_xlabel('Délai total (min)')
axes[0, 2].set_ylabel('Fréquence')
axes[0, 2].set_title('Distribution du délai total')
axes[0, 2].legend()

# Scatter : distance vs délai
axes[1, 0].scatter(df['distance_km'], df['delai_total_min'], alpha=0.5)
axes[1, 0].set_xlabel('Distance (km)')
axes[1, 0].set_ylabel('Délai total (min)')
axes[1, 0].set_title('Distance vs Délai total')

# Scatter : montant vs satisfaction
axes[1, 1].scatter(df['montant_euros'], df['satisfaction'], alpha=0.5)
axes[1, 1].set_xlabel('Montant (€)')
axes[1, 1].set_ylabel('Satisfaction')
axes[1, 1].set_title('Montant vs Satisfaction')

# Boxplot : satisfaction par retard
retard_labels = {0: 'À l\'heure', 1: 'Retard'}
satisfaction_by_retard = [df[df['est_retard'] == 0]['satisfaction'], 
                           df[df['est_retard'] == 1]['satisfaction']]
axes[1, 2].boxplot(satisfaction_by_retard, labels=['À l\'heure', 'Retard'])
axes[1, 2].set_ylabel('Satisfaction')
axes[1, 2].set_title('Satisfaction par retard')

plt.tight_layout()
plt.savefig('exploration.png', dpi=100, bbox_inches='tight')
print("Exploratory plots saved to exploration.png")
plt.show()

# ============================================================================
# 4. Vérifications et questions de démarrage
# ============================================================================

print("\n" + "="*70)
print("Questions de démarrage pour structurer votre projet :")
print("="*70)

print("\n1. STATISTIQUES DESCRIPTIVES")
print(f"   - Quel est le délai moyen ? {df['delai_total_min'].mean():.2f} min")
print(f"   - Quel est la médiane ? {df['delai_total_min'].median():.2f} min")
print(f"   - Quel est l'écart-type ? {df['delai_total_min'].std():.2f} min")

print("\n2. DÉPENDANCES")
correlation = df[['distance_km', 'montant_euros', 'delai_total_min', 'satisfaction']].corr()
print("   Matrice de corrélation :")
print(correlation.round(3))

print("\n3. MODÉLISATION PROBABILISTE")
print(f"   - La variable 'est_retard' est-elle Bernoulli(p) ? Estimez p.")
print(f"   - La distance suit-elle une loi Uniforme ? Testez visuellement.")
print(f"   - Le délai suit-il une loi Exponentielle ? Comparez.")

print("\n4. CONVERGENCE ET SIMULATION")
print("   - Générez 100 sous-échantillons de taille 20, 50, 100.")
print("   - Tracez comment la moyenne empirique stabilise vers la vraie moyenne.")

print("\n5. ESTIMATION ET INTERVALLES")
print(f"   - Estimez la vraie proportion de retards (intervalle 95%).")
print(f"   - Estimez le vrai délai moyen (intervalle 95%).")

print("\n" + "="*70)
