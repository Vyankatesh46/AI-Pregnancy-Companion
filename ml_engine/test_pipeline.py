from mood_model import predict_mood_risk
from kick_anamoly import detect_kick_anomaly
from risk_engine import aggregate_risk

# Simulated user inputs

answers = [2, 1, 1, 0, 1]
sleep_hours = 5

today_kicks = 12
kick_history = [24, 22, 23, 25, 24, 23, 22]

print("\nRunning Mood Risk Prediction...")

mood_result = predict_mood_risk(answers, sleep_hours)

print("Mood Model Output:")
print(mood_result)

print("\nRunning Kick Movement Analysis...")

kick_result = detect_kick_anomaly(today_kicks, kick_history)

print("Kick Detection Output:")
print(kick_result)


print("\nRunning Risk Aggregation...")

final_risk = aggregate_risk(
    mood_risk=mood_result["risk_level"],
    kick_status=kick_result["status"],
    sleep_hours=sleep_hours
)

print("Final Risk Assessment:")
print(final_risk)