from pathlib import Path
import pandas as pd
from src.io_tools import load_datasets
from src.models import (
    fit_univariate_by_activity,
    fit_multivariate_by_activity,
    fit_coffee_linear_0_6,
)
from src.plotting import (
    plot_univariate_regression,
    plot_coffee_regression,
)
from src.analysis import build_daily_join, questions_summary

DATA_DIR = Path("data")
OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

if __name__ == "__main__":
    # --- 1. Chargement ---
    df_sport, df_work = load_datasets(DATA_DIR)

    # --- 2. Régressions sport ---
    for act in df_sport["activite"].unique():
        slope, intercept = fit_univariate_by_activity(df_sport, act)
        out = OUTPUT_DIR / f"plot_sport_{act}.png"
        plot_univariate_regression(df_sport, act, slope, intercept, out)
        print(f"[SPORT] {act}: slope={slope:.2f}, intercept={intercept:.2f}")

    # --- 2.b Régressions sport multivariées ---
    from src.plotting import plot_multivariate_regression

    for act in df_sport["activite"].unique():
        a, b, c = fit_multivariate_by_activity(df_sport, act)
        out_3d = OUTPUT_DIR / f"plot_sport_multivar_{act}.png"
        plot_multivariate_regression(df_sport, act, a, b, c, out_3d)
        print(f"[SPORT MULTIVARIÉ] {act}: a={a:.2f}, b={b:.2f}, c={c:.2f}")

    # --- 3. Régression café ---
    slope_cafe, intercept_cafe = fit_coffee_linear_0_6(df_work)
    out_cafe = OUTPUT_DIR / "plot_coffee.png"
    plot_coffee_regression(df_work, slope_cafe, intercept_cafe, out_cafe)
    print(f"[CAFÉ] slope={slope_cafe:.2f}, intercept={intercept_cafe:.2f}")

    # --- 4. Analyse corrélationnelle ---
    daily = build_daily_join(df_sport, df_work)
    summary = questions_summary(daily)
    print("\n=== ANALYSE CORRÉLATIONNELLE ===")
    for k, v in summary.items():
        print(f"{k}: {v}")

    # --- 5. Export JSON ---
    summary_path = OUTPUT_DIR / "summary.json"
    pd.Series(summary).to_json(summary_path, indent=2, force_ascii=False)
    print(f"\nRésultats sauvegardés dans {summary_path.resolve()}")
