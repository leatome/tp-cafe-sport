import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pathlib import Path
from mpl_toolkits.mplot3d import Axes3D

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

def plot_multivariate_regression(df, activite, a, b, c, output_path):
    """Draw a 3D scatter of (duree_min, poids_kg, calories) and the fitted plane.
    Saves PNG to output_path.
    """
    subset = df[df["activite"] == activite]
    if subset.empty:
        return

    X, Y = np.meshgrid(
        np.linspace(subset["duree_min"].min(), subset["duree_min"].max(), 30),
        np.linspace(subset["poids_kg"].min(), subset["poids_kg"].max(), 30)
    )
    Z = a * X + b * Y + c

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection="3d")
    ax.scatter(subset["duree_min"], subset["poids_kg"], subset["calories"], color="blue", alpha=0.6)
    ax.plot_surface(X, Y, Z, color="red", alpha=0.3)
    ax.set_xlabel("Durée (min)")
    ax.set_ylabel("Poids (kg)")
    ax.set_zlabel("Calories")
    ax.set_title(f"Régression multivariée - {activite}")
    plt.tight_layout()
    plt.savefig(output_path, dpi=160, bbox_inches="tight")
    plt.close()

def plot_coffee_regression(df_work: pd.DataFrame, slope: float, intercept: float, out_path: Path):
    """Scatter productivite vs tasses_cafe and draw regression line, save PNG."""
    x = df_work["tasses_cafe"].to_numpy()
    y = df_work["productivite"].to_numpy()

    plt.figure()
    plt.scatter(x, y, s=25, color="blue")
    if x.size > 0:
        x_line = np.linspace(x.min(), x.max(), 100)
    else:
        x_line = np.linspace(0, 6, 2)
    y_line = slope * x_line + intercept
    plt.plot(x_line, y_line, color="red")
    plt.xlabel("Tasses de café")
    plt.ylabel("Productivité")
    plt.title("Productivité vs Tasses de café (0–6)")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(out_path, dpi=160, bbox_inches="tight")
    plt.close()
    