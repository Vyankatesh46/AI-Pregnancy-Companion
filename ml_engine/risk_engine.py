MOOD_RISK_SCORES = {
    "Low": 0,
    "Moderate": 2,
    "High": 4
}

KICK_STATUS_SCORES = {
    "NORMAL": 0,
    "LOW_MOVEMENT": 4
}

def sleep_risk_score(sleep_hours):
    """
    Convert sleep hours into risk score.
    """

    if sleep_hours >= 7:
        return 0
    elif sleep_hours >= 5:
        return 1
    else:
        return 2
    
def calculate_total_risk_score(mood_risk, kick_status, sleep_hours):
    """
    Combine multiple signals into a total risk score.
    """

    mood_score = MOOD_RISK_SCORES.get(mood_risk, 0)

    kick_score = KICK_STATUS_SCORES.get(kick_status, 0)

    sleep_score = sleep_risk_score(sleep_hours)

    total_score = mood_score + kick_score + sleep_score

    return total_score

def classify_risk_level(total_score):
    """
    Convert numeric risk score into risk level category.
    """

    if total_score <= 2:
        return "LOW"

    elif total_score <= 5:
        return "MODERATE"

    else:
        return "HIGH"
    
def aggregate_risk(mood_risk, kick_status, sleep_hours):
    """
    Combine all signals into final maternal risk assessment.
    """

    total_score = calculate_total_risk_score(
        mood_risk,
        kick_status,
        sleep_hours
    )

    overall_risk = classify_risk_level(total_score)

    return {
        "total_score": total_score,
        "overall_risk": overall_risk,
        "signals": {
            "mood_risk": mood_risk,
            "kick_status": kick_status,
            "sleep_hours": sleep_hours
        }
    }