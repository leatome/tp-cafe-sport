import pandas as pd
from pathlib import Path
from src.io_tools import load_datasets


def test_load_datasets_minimal_columns(tmp_path):
    # Créer des CSV temporaires simulant Sport_raw.csv et Travail_raw.csv
    sport_csv = tmp_path / "Sport_raw.csv"
    work_csv = tmp_path / "Travail_raw.csv"

    df_sport = pd.DataFrame({
        "activity": ["velo", "course"],
        "duration_min": [30, 60],
        "poids": [70, 75],
        "calories": [250, 600],
        "date": pd.to_datetime(["2025-01-01", "2025-01-02"])
    })
    df_work = pd.DataFrame({
        "date": pd.to_datetime(["2025-01-01", "2025-01-02"]),
        "hours_work": [8, 7],
        "coffee_cups": [2, 3],
        "productivity": [60, 65]
    })

    df_sport.to_csv(sport_csv, index=False)
    df_work.to_csv(work_csv, index=False)

    # Appeler load_datasets sur le dossier temporaire
    df_sport_loaded, df_work_loaded = load_datasets(tmp_path)

    for col in ["activite", "duree_min", "poids_kg", "calories"]:
        assert col in df_sport_loaded.columns
    for col in ["date", "heures_travail", "tasses_cafe", "productivite"]:
        assert col in df_work_loaded.columns
    assert pd.api.types.is_numeric_dtype(df_sport_loaded["duree_min"])
    assert pd.api.types.is_numeric_dtype(df_work_loaded["tasses_cafe"])
