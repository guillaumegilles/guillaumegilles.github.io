"""
Générateur de données fictives pour le projet intégrateur
Statistiques et Probabilités — Plateforme de livraison locale

Exécution : python generate_delivery_data.py
Sortie : delivery_data.csv (400 observations)
"""

import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# Seed pour reproductibilité
np.random.seed(42)

# Paramètres de génération
n_observations = 400
today = datetime.now()

# ============================================================================
# Structures de dépendance réalistes
# ============================================================================

# 1. Distance (km) ~ U(0.5, 25)
distance = np.random.uniform(0.5, 25, n_observations)

# 2. Montant (€) ~ dépend de la distance (commandes lointaines tendentiellement plus chères)
montant = 15 + 1.5 * distance + np.random.normal(0, 5, n_observations)
montant = np.maximum(montant, 5)  # Au moins 5€

# 3. Délai de préparation (min) ~ dépend du montant (commandes complexes plus longues)
prep_delay = 8 + 0.3 * montant + np.random.exponential(2, n_observations)
prep_delay = np.round(prep_delay).astype(int)

# 4. Délai de livraison (min) ~ dépend de la distance (modèle réaliste)
#    distance_km * 2 min/km + variabilité trafic + temps d'attente
delivery_delay = 5 + 2 * distance + np.random.exponential(3, n_observations)
delivery_delay = np.round(delivery_delay).astype(int)

# 5. Délai total (min)
total_delay = prep_delay + delivery_delay

# 6. Indicateur de retard (1 si > 45 min, 0 sinon)
is_late = (total_delay > 45).astype(int)

# 7. Satisfaction client ~ dépend du délai et du montant
#    Plus de retards <=> moins satisfait
#    Plus le montant est élevé <=> attentes plus grandes
base_satisfaction = 4.5
satisfaction = (
    base_satisfaction
    - 0.4 * is_late  # Forte pénalité en cas de retard
    - 0.05 * (montant > 30)  # Les grosses commandes sont plus exigeantes
    + np.random.normal(0, 0.5, n_observations)
)
satisfaction = np.round(np.clip(satisfaction, 1, 5)).astype(int)

# ============================================================================
# Création du DataFrame
# ============================================================================

df = pd.DataFrame({
    'commande_id': range(1, n_observations + 1),
    'distance_km': np.round(distance, 2),
    'montant_euros': np.round(montant, 2),
    'delai_prep_min': prep_delay,
    'delai_livr_min': delivery_delay,
    'delai_total_min': total_delay,
    'est_retard': is_late,
    'satisfaction': satisfaction
})

# ============================================================================
# Sauvegarde
# ============================================================================

output_file = 'delivery_data.csv'
df.to_csv(output_file, index=False, sep=',', encoding='utf-8')

print(f"✅ Dataset généré : {output_file}")
print(f"   - {n_observations} observations")
print(f"   - colonnes : {', '.join(df.columns)}")
print()
print("Résumé statistique :")
print(df.describe())
print()
print("Taux de retard :", f"{df['est_retard'].mean():.1%}")
print("Satisfaction moyenne :", f"{df['satisfaction'].mean():.2f}")
