
---

# Café vs Sport vs Calorie vs Productivité

---

## 1. Présentation du projet

Ce projet étudie la relation entre **activité physique**, **consommation de café** et **productivité** à partir de jeux de données simulés.

**Objectifs principaux :**

* Modéliser la dépense calorique selon la durée et le poids.
* Modéliser l’effet du café sur la productivité (0–6 tasses).
* Visualiser les régressions linéaires (scatter + droite).
* Étudier les corrélations entre sport, café et productivité.

Le rendu inclut un **script Python exécutable (`src/main.py`)** qui génère les **graphiques PNG** et un **résumé JSON (`summary.json`)**.

---

## 2. Structure du projet

```
tp-cafe-sport/
│
├── data/                      # Données d’entrée
│   ├── Sport_raw.csv
│   └── Travail_raw.csv
│
├── src/                       # Code source principal
│   ├── io_tools.py
│   ├── models.py
│   ├── plotting.py
│   ├── analysis.py
│   ├── main.py
│   └── __init__.py
│
├── tests/                     # Tests unitaires (pytest)
│   ├── test_io_tools.py
│   ├── test_models_univariate.py
│   ├── test_models_multivariate.py
│   ├── test_models_coffee.py
│   ├── test_plot_univariate.py
│   ├── test_plot_coffee.py
│   └── test_analysis.py
│
├── outputs/                   # Résultats générés automatiquement
│   ├── plot_sport_*.png
│   ├── plot_coffee.png
│   └── summary.json
│
├── requirements.txt
├── README.md
└── __init__.py
```

---

## 3. Installation

### Étape 1 : Créer un environnement virtuel

```bash
python -m venv .venv
source .venv/bin/activate  # macOS / Linux
# ou
.venv\Scripts\activate      # Windows
```

### Étape 2 : Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## 4. Exécution et génération des résultats

### Lancer les tests unitaires

Tous les modules sont testés avec **pytest** :

```bash
pytest -q
```

Résultat attendu :

```
7 passed in X.XXs
```

### Exécuter le pipeline complet

```bash
python -m src.main
```

Résultats générés dans `outputs/` :

| Fichier            | Description                                          |
| ------------------ | ---------------------------------------------------- |
| `plot_sport_*.png` | Régression calories/durée pour chaque activité       |
| `plot_coffee.png`  | Régression productivité/tasses de café               |
| `summary.json`     | Corrélations et effets (sport ↔ café ↔ productivité) |

---

## 5. Relations modélisées

### 5.1 Sport

```
calories ≈ MET(activité) * 3.5 * poids_kg / 200 * durée_min + bruit
```

avec MET(course)=9.8, MET(vélo)=7.5, MET(natation)=8.0.

### 5.2 Café

```
productivité ≈ 45 + 4.5 * tasses_café + bruit
```

Effet décroissant observé après 4–5 tasses.

---

## 6. Questions explorées

* Les jours de sport intense, boit-on plus de café le lendemain ?
* Les individus actifs sont-ils plus productifs ?
* Trop de sport et trop de café entraînent-ils une baisse de productivité ?
* Existe-t-il un équilibre entre heures de travail + durée de sport et la productivité ?
* Y a-t-il une corrélation entre calories dépensées et tasses de café ?
* Les individus les plus sportifs consomment-ils plus de café ?

---

## 7. Exemple de sortie (`summary.json`)

```json
{
  "corr_calories_cafe": 0.23,
  "corr_actif_productif": 0.41,
  "effect_jplus1_cafe_apres_sport_intense": 0.18
}
```

---

## 8. Méthodologie de développement

Le projet suit rigoureusement la méthode **TDD (Test Driven Development)** :

1. Écriture d’un **test rouge minimal**.
2. Implémentation du **patch minimal** pour le rendre vert.
3. Refactorisation uniquement quand tous les tests sont verts.

Cette approche garantit :

* un code clair et justifié,
* aucune abstraction prématurée,
* une validation métier avant tout.

---

## 9. Spécifications techniques

* Python ≥ 3.10
* Dépendances principales : `pandas`, `numpy`, `matplotlib`, `pytest`
* Compatible Windows / macOS / Linux
* Architecture modulaire et claire :

  * **io_tools.py** → chargement et normalisation des données
  * **models.py** → régressions linéaires (sport, café)
  * **plotting.py** → visualisations
  * **analysis.py** → corrélations et effets croisés
  * **main.py** → exécution complète du pipeline

---
