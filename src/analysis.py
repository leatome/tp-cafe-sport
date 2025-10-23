import pandas as pd
import numpy as np


def build_daily_join(df_sport: pd.DataFrame, df_work: pd.DataFrame) -> pd.DataFrame:
    """Aggregate sport by date and join with work dataframe.

    Produces columns like 'calories_jour' and 'duree_jour' merged with work data.
    """
    # Ensure date column is datetime
    df_s = df_sport.copy()
    df_w = df_work.copy()
    df_s["date"] = pd.to_datetime(df_s["date"])
    df_w["date"] = pd.to_datetime(df_w["date"])

    agg = df_s.groupby("date").agg({
        "duree_min": "sum",
        "calories": "sum"
    }).rename(columns={"duree_min": "duree_jour", "calories": "calories_jour"}).reset_index()

    daily = pd.merge(df_w, agg, on="date", how="left")
    # fill missing sport days with zeros
    daily["duree_jour"] = daily["duree_jour"].fillna(0)
    daily["calories_jour"] = daily["calories_jour"].fillna(0)

    return daily


def questions_summary(daily_df: pd.DataFrame) -> dict:
    """Compute requested summary indicators and correlations.

    Returns a dict containing at least:
      - corr_calories_cafe: Pearson corr between calories_jour and tasses_cafe
      - corr_actif_productif: Pearson corr between an 'actif' flag and productivite
      - effect_jplus1_cafe_apres_sport_intense: average change in tasses the day after an intense sport day
    """
    res = {}

    # corr calories vs coffee
    if "calories_jour" in daily_df.columns and "tasses_cafe" in daily_df.columns:
        try:
            res["corr_calories_cafe"] = float(daily_df["calories_jour"].corr(daily_df["tasses_cafe"]))
        except Exception:
            res["corr_calories_cafe"] = None
    else:
        res["corr_calories_cafe"] = None

    # corr actif vs productivite: actif = had any sport (duree_jour > 0)
    if "duree_jour" in daily_df.columns and "productivite" in daily_df.columns:
        actif = (daily_df["duree_jour"] > 0).astype(float)
        try:
            res["corr_actif_productif"] = float(pd.Series(actif).corr(daily_df["productivite"]))
        except Exception:
            res["corr_actif_productif"] = None
    else:
        res["corr_actif_productif"] = None

    # effect J+1: when today's calories_jour is 'intense' (> threshold), look at tasses next day
    if "calories_jour" in daily_df.columns and "tasses_cafe" in daily_df.columns:
        thresh = 500  # arbitrary threshold for 'intense' session
        mask = daily_df["calories_jour"] > thresh
        if mask.any():
            # tasses shifted to next day
            t_next = daily_df["tasses_cafe"].shift(-1)
            vals = t_next[mask]
            if vals.dropna().size > 0:
                # effect = mean next-day tasses after intense sport minus overall mean tasses
                effect = float(vals.mean() - daily_df["tasses_cafe"].mean())
                res["effect_jplus1_cafe_apres_sport_intense"] = effect
            else:
                res["effect_jplus1_cafe_apres_sport_intense"] = None
        else:
            res["effect_jplus1_cafe_apres_sport_intense"] = None
    else:
        res["effect_jplus1_cafe_apres_sport_intense"] = None

    return res
