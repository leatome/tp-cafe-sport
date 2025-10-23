import numpy as np
import pandas as pd


def fit_univariate_by_activity(df_sport: pd.DataFrame, activite: str):
    """Fit a univariate linear regression calories = slope * duree_min + intercept

    Returns (slope, intercept) as floats. Raises ValueError if no rows for activity.
    """
    sub = df_sport[df_sport["activite"] == activite]
    if sub.empty:
        raise ValueError(f"Aucune donnée pour activite={activite}")

    x = sub["duree_min"].to_numpy()
    y = sub["calories"].to_numpy()

    slope, intercept = np.polyfit(x, y, 1)

    return float(slope), float(intercept)
