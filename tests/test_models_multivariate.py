import pandas as pd
import numpy as np
from src.models import fit_multivariate_by_activity


def test_fit_multivariate_estimates_both_coeffs():
    rng = np.random.default_rng(1)
    n = 60
    duree = rng.integers(10, 90, n)
    poids = rng.integers(55, 95, n)
    MET = 7.5  # vélo
    y = (MET * 3.5 * poids / 200.0) * duree + 15 + rng.normal(0, 20, n)
    df = pd.DataFrame({
        "activite": ["velo"] * n,
        "duree_min": duree,
        "poids_kg": poids,
        "calories": y
    })
    a, b, c = fit_multivariate_by_activity(df, "velo")
    assert a > 0
    assert b > 0
