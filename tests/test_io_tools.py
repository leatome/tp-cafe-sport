import pandas as pd
from pathlib import Path
from src.io_tools import load_datasets


def test_load_datasets_minimal_columns(tmp_path):
    data_dir = Path("data")
    df_sport, df_work = load_datasets(data_dir)
    for col in ["activite", "duree_min", "poids_kg", "calories"]:
        assert col in df_sport.columns
    for col in ["date", "heures_travail", "tasses_cafe", "productivite"]:
        assert col in df_work.columns
    assert pd.api.types.is_numeric_dtype(df_sport["duree_min"])
    assert pd.api.types.is_numeric_dtype(df_work["tasses_cafe"])
