import numpy as np

def get_recent_history(kick_history, window=7):
    """
    Select recent kick history window.
    """

    if len(kick_history) <= window:
        return kick_history

    return kick_history[-window:]

def calculate_baseline(kick_history):
    """
    Calculate baseline baby movement using recent history.
    """

    recent_history = get_recent_history(kick_history)

    baseline = np.mean(recent_history)

    return baseline

def detect_kick_anomaly(today_kicks, kick_history):
    """
    Detect abnormal baby movement compared to personal baseline.
    """

    # Safety check: invalid today value
    if today_kicks is None or today_kicks < 0:
        return {
            "status": "INVALID_INPUT",
            "message": "Invalid kick count provided."
        }

    # Safety check: no history available
    if not kick_history or len(kick_history) < 3:
        return {
            "status": "INSUFFICIENT_HISTORY",
            "message": "Not enough history to determine baseline.",
            "today": today_kicks
        }

    baseline = calculate_baseline(kick_history)

    threshold = baseline * 0.6

    if today_kicks < threshold:
        status = "LOW_MOVEMENT"
    else:
        status = "NORMAL"

    return {
        "baseline": round(baseline, 2),
        "today": today_kicks,
        "threshold": round(threshold, 2),
        "status": status
    }