import json
import openai
from llm_engine.prompts import (
    build_base_system_prompt,
    build_pregnancy_prompt,
    build_postpartum_prompt,
)

# Goose.ai configuration
openai.api_key = "sk-CjILPpDNjKr7Xo7mTwRNhTLH2S0Gn9noI5sqW6mIvv03zcA9"
openai.api_base = "https://api.goose.ai/v1"


class LLMService:

    @staticmethod
    def generate_personalized_guidance(data: dict) -> dict:

        # ---- ROUTING LOGIC ----
        is_postpartum = data.get("is_postpartum", False)

        if is_postpartum:
            user_prompt = build_postpartum_prompt(data)
        else:
            user_prompt = build_pregnancy_prompt(data)

        system_prompt = build_base_system_prompt()

        # Force JSON output by ending prompt with opening brace
        full_prompt = system_prompt + "\n" + user_prompt + "\n\nJSON Response:\n{"

        # ---- LLM CALL ----
        response = openai.Completion.create(
            engine="gpt-j-6b",
            prompt=full_prompt,
            max_tokens=800,
            temperature=0.2,
            stop=["}}}"]
        )

        raw_output = "{" + response.choices[0].text
        print("RAW OUTPUT:", raw_output)

        # ---- Extract JSON from response ----
        try:
            start = raw_output.find("{")
            end = raw_output.rfind("}") + 1
            if start != -1 and end != 0:
                json_str = raw_output[start:end]
                parsed = json.loads(json_str)
            else:
                raise ValueError("No JSON found")
        except Exception:
            # ---- Build smart fallback using ML data ----
            risk_level = data.get("risk_level", "Low")
            week = data.get("week", "Unknown")
            trimester = data.get("trimester", "Unknown")
            diet_flags = data.get("diet_flags", [])
            mood_risk = data.get("mood_risk", "Low")

            parsed = {
                "summary": f"You are at week {week} of your pregnancy (Trimester {trimester}). Risk level is {risk_level}.",
                "weekly_guidance": f"At week {week}, focus on regular checkups and staying hydrated.",
                "diet_recommendation": f"Diet flags detected: {', '.join(diet_flags)}. Eat iron-rich foods like spinach and lentils.",
                "mental_health_support": "Practice deep breathing and light walks daily." if mood_risk != "Low" else "You are doing great! Stay positive.",
                "risk_alert": f"Risk level is {risk_level}. {data.get('risk_reason', '')}",
                "doctor_consult_advice": "Please consult your doctor regularly." if risk_level == "High" else "Monitor your health and consult if needed.",
                "confidence_note": "This is supportive guidance, not a medical diagnosis."
            }

        return parsed