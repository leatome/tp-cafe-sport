from pathlib import Path
import pandas as pd
from src.plotting import plot_univariate_regression


def test_plot_univariate_regression_writes_png(tmp_path):
    df = pd.DataFrame({
        "activite": ["course"]*5,
        "duree_min": [10,20,30,40,50],
        "poids_kg": [70]*5,
        "calories": [120, 250, 360, 500, 610]
    })
    out = tmp_path / "plot.png"
    plot_univariate_regression(df, "course", slope=10.0, intercept=20.0, out_path=out)
    assert out.exists() and out.stat().st_size > 0
