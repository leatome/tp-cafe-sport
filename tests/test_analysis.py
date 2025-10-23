import pandas as pd
from datetime import timedelta
from src.analysis import build_daily_join, questions_summary


def test_build_and_questions_summary():
    sport = pd.DataFrame({
        "date": pd.to_datetime(["2025-01-01","2025-01-02"]),
        "activite": ["course","velo"],
        "duree_min": [60, 30],
        "poids_kg": [70, 70],
        "calories": [700, 250]
    })
    work = pd.DataFrame({
        "date": pd.to_datetime(["2025-01-01","2025-01-02"]),
        "heures_travail": [8, 7],
        "tasses_cafe": [2, 3],
        "productivite": [60, 62]
    })

    daily = build_daily_join(sport, work)
    assert "calories_jour" in daily.columns
    summary = questions_summary(daily)
    for key in [
        "corr_calories_cafe",
        "corr_actif_productif",
        "effect_jplus1_cafe_apres_sport_intense"
    ]:
        assert key in summary
