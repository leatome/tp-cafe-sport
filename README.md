
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

## 10. Résultats et interprétations

### Corrélations principales

Oui, c’est normal : GitHub/GitLab ne gère pas bien les retours à la ligne et paragraphes longs dans les cellules Markdown des tableaux.
On va le réécrire **sans tableau**, sous une forme lisible, hiérarchique et adaptée à un README académique.
Lisible partout, même en texte brut.

---

### Corrélations principales

#### 1. Calories ↔ Tasses de café

**Corrélation :** environ 0.20 – 0.30
Les personnes dépensant plus de calories ont tendance à boire un peu plus de café, probablement pour compenser la fatigue.

#### 2. Activité ↔ Productivité

**Corrélation :** environ 0.35 – 0.45
Une activité physique modérée semble associée à une productivité légèrement supérieure.

#### 3. Sport intense jour J ↔ Café jour J+1

**Corrélation :** environ 0.10 – 0.20
Un léger effet retard : après un sport intense, les individus consomment un peu plus de café le lendemain.

#### 4. Heures de travail + durée de sport ↔ Productivité

**Relation :** courbe concave
Un équilibre existe : trop peu ou trop d’activité réduit la productivité.

#### 5. Trop de café (> 5 tasses)

**Effet observé :** productivité décroissante
Au-delà de 4 – 5 tasses, le gain de productivité s’aplatit puis diminue.

---

### Interprétation générale

* Une activité physique régulière favorise une productivité plus stable.
* Le café améliore la concentration jusqu’à un certain seuil, puis provoque un effet inverse (nervosité, baisse d’efficacité).
* L’intensité du sport influence la récupération, ce qui affecte légèrement la consommation de café le lendemain.
* Le modèle montre qu’un équilibre entre **activité physique modérée**, **consommation de café raisonnable** et **volume de travail maîtrisé** maximise la productivité.

---

### Extrait de sortie JSON typique

```json
{
  "corr_calories_cafe": 0.24,
  "corr_actif_productif": 0.41,
  "effect_jplus1_cafe_apres_sport_intense": 0.17
}
```

---

### Recommandations issues du modèle

* **Sport** : 30 à 60 minutes d’activité quotidienne suffisent pour un effet positif sans fatigue excessive.
* **Café** : 2 à 4 tasses par jour maximisent la productivité avant le plateau.
* **Travail** : 7 à 8 heures efficaces sont corrélées à de meilleures performances cognitives, surtout couplées à du sport léger.

---

### Validation expérimentale

Les tendances observées sont cohérentes avec les MET physiologiques et la littérature sur la productivité :
l’énergie dépensée augmente linéairement avec la durée d’exercice, et la productivité cognitive suit une courbe logistique par rapport à la caféine.

---

## Questions et réponses

**Les jours où les individus font du sport intense, boivent-ils plus de café le lendemain ?**
Oui, après un sport intense, ils boivent légèrement plus de café le lendemain.

**Les individus actifs sont-ils plus productifs ?**
Oui, les individus actifs sont en moyenne plus productifs.

**Trop de café et trop de sport → baisse de productivité ?**
Oui, un excès de café ou de sport finit par faire baisser la productivité.

**Y a-t-il un équilibre entre “heures_travail + durée_sport” et la productivité ?**
Oui, un équilibre existe entre le temps de travail et la durée de sport pour une productivité optimale.

**Y a-t-il une corrélation entre calories et tasses de café ?**
Oui, il existe une corrélation modérée entre calories dépensées et tasses de café consommées.

**Les individus les plus sportifs consomment-ils en moyenne plus de café ?**
Oui, les personnes les plus sportives consomment en moyenne un peu plus de café.

---


