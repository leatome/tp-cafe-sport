import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pathlib import Path


def plot_univariate_regression(df_sport: pd.DataFrame, activite: str, slope: float, intercept: float, out_path: Path):
    sub = df_sport[df_sport["activite"] == activite]
    x = sub["duree_min"].to_numpy()
    y = sub["calories"].to_numpy()
    plt.figure()
    plt.scatter(x, y, s=20)
    if x.size > 0:
        x_line = np.linspace(x.min(), x.max(), 100)
    else:
        x_line = np.linspace(0, 1, 2)
    y_line = slope * x_line + intercept
    plt.plot(x_line, y_line, color="red")
    plt.xlabel("Durée (min)")
    plt.ylabel("Calories")
    plt.title(f"{activite} : calories vs durée")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(out_path, dpi=160, bbox_inches="tight")
    plt.close()
