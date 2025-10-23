from pathlib import Path
import pandas as pd
from src.plotting import plot_coffee_regression


def test_plot_coffee_regression_writes_png(tmp_path):
    df = pd.DataFrame({
        "tasses_cafe": [0, 1, 2, 3, 4, 5, 6],
        "productivite": [45, 50, 54, 58, 63, 67, 70],
    })
    out = tmp_path / "coffee_plot.png"
    plot_coffee_regression(df, slope=4.5, intercept=45.0, out_path=out)
    assert out.exists() and out.stat().st_size > 0
