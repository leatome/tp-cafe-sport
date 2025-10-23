import pandas as pd
import numpy as np
from src.models import fit_coffee_linear_0_6


def test_fit_coffee_linear_basic():
    rng = np.random.default_rng(42)
    cups = np.arange(0, 7)  # de 0 à 6 inclus
    y = 45 + 4.5 * cups + rng.normal(0, 1.0, size=cups.size)
    df = pd.DataFrame({
        "date": pd.date_range("2025-01-01", periods=7),
        "tasses_cafe": cups,
        "productivite": y,
        "heures_travail": 7
    })

    slope, intercept = fit_coffee_linear_0_6(df)

    # pente positive et réaliste
    assert slope > 3.0
    assert isinstance(intercept, float)
