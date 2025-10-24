
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
|   ├── plot_sport_multivar_*.png
│   ├── plot_coffee.png
│   └── summary.json
│
├── requirements.txt
├── README.md
└── __init__.py
```

---

## 3. Installation

Windows
```
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

MacOS / Linux
```
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

---

## 4. Exécution et génération des résultats

### Lancer les tests unitaires

Tous les modules sont testés avec **pytest** :

Windows
```bash
.\.venv\Scripts\python -m pytest -q
```

MacOS / Linux
```bash
.venv/bin/python -m pytest -q
```

Résultat attendu :

```
7 passed in X.XXs
```

### Exécuter le pipeline complet

Windows
```bash
.\.venv\Scripts\python -m src.main
```

MacOS / Linux
```bash
.venv/bin/python -m src.main
```

Résultats générés dans `outputs/` :

| Fichier                     | Description                                          |
| --------------------------- | -----------------------------------------------------|
| `plot_sport_*.png`          | Régression calories/durée pour chaque activité       |
| `plot_sport_multivar_*.png` | Régression multivariée pour chaque activité          |
| `plot_coffee.png`           | Régression productivité/tasses de café               |
| `summary.json`              | Corrélations et effets (sport ↔ café ↔ productivité) |

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
  "corr_calories_cafe": 0.01,
  "corr_actif_productif": 0.03,
  "effect_jplus1_cafe_apres_sport_intense": 0.01
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

## 10. Résultats et interprétations

### Corrélations principales

Oui, c’est normal : GitHub/GitLab ne gère pas bien les retours à la ligne et paragraphes longs dans les cellules Markdown des tableaux.
On va le réécrire **sans tableau**, sous une forme lisible, hiérarchique et adaptée à un README académique.
Lisible partout, même en texte brut.

---

### Corrélations principales

#### 1. Calories ↔ Tasses de café

**Corrélation :** environ 0.01
Aucune relation n'est significative, la dépense énergétique n'a pas l'air d'avoir une grande influence du à la consommation de café.

#### 2. Activité ↔ Productivité

**Corrélation :** environ 0.03
Les individus actifs ne sont pas significativement plus productifs dans cet échantillon.

#### 3. Sport intense jour J ↔ Café jour J+1

**Corrélation :** environ 0.01
Aucun effet notable : faire du sport intense ne semble pas augmenter la consommation de café le lendemain.

#### 4. Heures de travail + durée de sport ↔ Productivité

**Relation :**
Aucun équilibre clair observé dans les données simulées.

#### 5. Trop de café (> 5 tasses)

**Effet observé :** productivité stable ou légèremnt décroissante
Au-delà de 3 – 6 tasses, le gain de productivité semble plafonner.

---

### Interprétation générale

* Les modèles de régression fonctionnent bien individuellement (sport vs calories, café vs productivité).
* Cependant, les corrélations croisées entre sport, café et productivité sont quasi nulles (0.01–0.03).
* Cela montre que dans ces données simulées, les comportements sont indépendants :
 - faire du sport n’influence pas la productivité
 - la consommation de café n’est pas liée à l’activité physique

---

### Extrait de sortie JSON typique

```json
{
  "corr_calories_cafe": 0.0119,
  "corr_actif_productif": 0.0317,
  "effect_jplus1_cafe_apres_sport_intense": 0.0142
}
```

---

### Recommandations issues du modèle

* **Sport** : la relation calories vs durée est bien modélisée, les pentes sont cohérentes avec les METs.
* **Café** : 3 à 6 tasses par jour croît légèrement la productivité avant le plateau.
* **Interactions** : aucune corrélation marquée entre sport, café et productivité globale.

---

### Validation expérimentale

Les tendances internes (calories vs durée, café vs productivité) sont cohérentes avec les équations de départ,
mais les corrélations inter-domaines sont trop faibles pour conclure à des relations réelles.
C'est ce qui est attendu dans des données simulées avec bruit aléatoire.

---

## Questions et réponses

**Les jours où les individus font du sport intense, boivent-ils plus de café le lendemain ?**
Non, la corrélation est très faible (~0.01).

**Les individus actifs sont-ils plus productifs ?**
Non, la corrélation est quasi nulle donc pas vraiment plus productif (~0.03).

**Trop de café et trop de sport → baisse de productivité ?**
Ce n'est pas observé de manière significative.

**Y a-t-il un équilibre entre “heures_travail + durée_sport” et la productivité ?**
L'échantillon est trop petit pour pouvoir l'affirmer.

**Y a-t-il une corrélation entre calories et tasses de café ?**
Non, elle est quasi inexistante (~0.01).

**Les individus les plus sportifs consomment-ils en moyenne plus de café ?**
Aucune tendance nette n'a pu être obersvé.

---
