import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from llm_engine.llm_service import LLMService

test_data = {
    "week": 24,
    "trimester": 2,
    "risk_level": "Medium",
    "risk_reason": "High BP trend detected",
    "mood_risk": "Low",
    "diet_flags": ["Low hemoglobin"],
    "user_profile": {
        "age": 27,
        "weight": 68,
        "diet_preference": "Vegetarian",
        "medical_history": ["Gestational diabetes"]
    },
    "is_postpartum": False
}

print("Calling LLM...")

try:
    result = LLMService.generate_personalized_guidance(test_data)
    import json
    print("SUCCESS!")
    print(json.dumps(result, indent=2))
except Exception as e:
    print(f"ERROR: {e}")