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


def fit_multivariate_by_activity(df_sport: pd.DataFrame, activite: str):
    """Fit multivariate linear model calories = a*duree_min + b*poids_kg + c

    Returns (a, b, c) as floats. Raises ValueError if no rows for activity.
    """
    sub = df_sport[df_sport["activite"] == activite]
    if sub.empty:
        raise ValueError(f"Aucune donnée pour activite={activite}")

    X = np.column_stack([
        sub["duree_min"].to_numpy(),
        sub["poids_kg"].to_numpy(),
        np.ones(len(sub))
    ])
    y = sub["calories"].to_numpy()
    coef, *_ = np.linalg.lstsq(X, y, rcond=None)
    a, b, c = coef
    return float(a), float(b), float(c)


def fit_coffee_linear_0_6(df_work: pd.DataFrame):
    """Fit linear model productivite = slope * tasses_cafe + intercept for tasses in [0,6].

    Returns (slope, intercept) as floats. Raises ValueError if no matching rows.
    """
    sub = df_work[(df_work["tasses_cafe"] >= 0) & (df_work["tasses_cafe"] <= 6)]
    if sub.empty:
        raise ValueError("Aucune donnée café sur [0,6]")

    x = sub["tasses_cafe"].to_numpy()
    y = sub["productivite"].to_numpy()

    slope, intercept = np.polyfit(x, y, 1)

    return float(slope), float(intercept)
