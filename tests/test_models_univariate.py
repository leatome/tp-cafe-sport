import pandas as pd
import numpy as np
from src.models import fit_univariate_by_activity


def test_fit_univariate_returns_reasonable_slope():
    # Données synthétiques cohérentes avec MET(course)=9.8, poids=70
    rng = np.random.default_rng(0)
    minutes = np.arange(10, 70, 10)
    a_true = 9.8 * 3.5 * 70 / 200  # ≈ 12.005
    calories = a_true * minutes + 20 + rng.normal(0, 5, size=minutes.size)
    df = pd.DataFrame({
        "activite": ["course"] * len(minutes),
        "duree_min": minutes,
        "poids_kg": [70] * len(minutes),
        "calories": calories
    })

    slope, intercept = fit_univariate_by_activity(df, "course")

    # On tolère un écart de ±3 calories/min à cause du bruit
    assert abs(slope - a_true) < 3.0
    assert isinstance(intercept, float)
