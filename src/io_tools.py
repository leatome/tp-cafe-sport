from pathlib import Path
import pandas as pd


def load_datasets(data_dir: Path):
    """Load and minimally clean the sport and travail datasets.

    Args:
        data_dir (Path or str): directory containing Sport_raw.csv and Travail_raw.csv

    Returns:
        tuple[pd.DataFrame, pd.DataFrame]: (sport_df, travail_df)
    """
    data_dir = Path(data_dir)
    sport = pd.read_csv(data_dir / "Sport_raw.csv")
    travail = pd.read_csv(data_dir / "Travail_raw.csv")

    rename_sport = {
        "activity": "activite",
        "duration_min": "duree_min",
        "poids": "poids_kg"
    }
    sport = sport.rename(columns=rename_sport)
    # If the dataset provides duree + unite (e.g. 1.5,h or 45,min) compute duree_min
    if "duree_min" not in sport.columns:
        if "duree" in sport.columns:
            # coerce duree to numeric (may contain decimals for hours)
            sport["duree"] = pd.to_numeric(sport["duree"], errors="coerce")
            if "unite" in sport.columns:
                units = sport["unite"].astype(str).str.lower().str.strip()
                # entries containing 'h' are hours; containing 'min' are minutes
                is_hour = units.str.contains(r"\bh\b|heure|heures") | units.str.contains("h")
                # default: treat as minutes when unit is missing/unknown
                duree_min = sport["duree"].copy()
                # multiply hours by 60
                duree_min.loc[is_hour.fillna(False)] = duree_min.loc[is_hour.fillna(False)] * 60
                sport["duree_min"] = pd.to_numeric(duree_min, errors="coerce")
            else:
                # no unit column -> assume minutes
                sport["duree_min"] = sport["duree"]
    for c in ["duree_min", "poids_kg", "calories"]:
        if c in sport.columns:
            sport[c] = pd.to_numeric(sport[c], errors="coerce")
    if "date" in sport.columns:
        sport["date"] = pd.to_datetime(sport["date"], errors="coerce")

    # Harmonisation des libellés d'activité
    sport["activite"] = (
        sport["activite"]
        .astype(str)
        .str.strip()
        .str.lower()
        .str.normalize("NFKD")
        .str.encode("ascii", errors="ignore")
        .str.decode("utf-8")
        .replace({
            "cours": "course",
            "velò": "velo",
            "vélo": "velo"
        })
    )
    
    rename_work = {
        "hours_work": "heures_travail",
        "coffee_cups": "tasses_cafe",
        "productivity": "productivite"
    }
    travail = travail.rename(columns=rename_work)
    for c in ["tasses_cafe", "heures_travail", "productivite"]:
        travail[c] = pd.to_numeric(travail[c], errors="coerce")
    travail["date"] = pd.to_datetime(travail["date"], errors="coerce")

    for col in ["activite", "duree_min", "poids_kg", "calories"]:
        if col not in sport.columns:
            raise ValueError(f"Colonne manquante dans Sport_raw.csv: {col}")
    for col in ["date", "heures_travail", "tasses_cafe", "productivite"]:
        if col not in travail.columns:
            raise ValueError(f"Colonne manquante dans Travail_raw.csv: {col}")

    sport = sport.dropna(subset=["activite", "duree_min", "poids_kg", "calories"]) 
    travail = travail.dropna(subset=["date", "heures_travail", "tasses_cafe", "productivite"]) 

    return sport, travail
