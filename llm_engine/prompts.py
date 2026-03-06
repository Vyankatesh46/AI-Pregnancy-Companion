def build_base_system_prompt():
    return """
You are an emotionally supportive AI Pregnancy & Postnatal Companion.

You provide:
- Week-based pregnancy guidance
- Diet personalization
- Mental health support
- Risk-aware safety suggestions

IMPORTANT RULES:
- Do NOT diagnose.
- Do NOT override provided risk_level.
- If risk_level is High → strongly recommend doctor consultation.
- If risk_level is Medium → suggest monitoring and consultation.
- Maintain calm, reassuring tone.
- Always include safety disclaimer.
- Return ONLY valid JSON.
- No markdown.
- No explanations outside JSON.

Output must strictly follow this JSON format:

{
  "summary": "",
  "weekly_guidance": "",
  "diet_recommendation": "",
  "mental_health_support": "",
  "risk_alert": "",
  "doctor_consult_advice": "",
  "confidence_note": ""
}
"""


def build_pregnancy_prompt(data: dict):
    week = data.get("week", "Unknown")
    trimester = data.get("trimester", "Unknown")
    risk_level = data.get("risk_level", "Low")
    risk_reason = data.get("risk_reason", "")
    mood_risk = data.get("mood_risk", "Low")
    diet_flags = data.get("diet_flags", [])
    profile = data.get("user_profile", {})

    return f"""
User Context:
- Week: {week}
- Trimester: {trimester}
- Risk Level: {risk_level}
- Risk Reason: {risk_reason}
- Mood Risk: {mood_risk}
- Diet Flags: {diet_flags}
- Age: {profile.get("age")}
- Weight: {profile.get("weight")}
- Diet Preference: {profile.get("diet_preference")}
- Medical History: {profile.get("medical_history")}

Provide personalized pregnancy guidance.
Adapt advice to trimester.
Adapt diet to preference.
Highlight ML-detected risks without exaggeration.
Include mental health coping tips if mood risk exists.
Include disclaimer: "This is supportive guidance, not a medical diagnosis."
Return JSON only.
"""


def build_postpartum_prompt(data: dict):
    risk_level = data.get("risk_level", "Low")
    mood_risk = data.get("mood_risk", "Low")
    profile = data.get("user_profile", {})

    return f"""
User Context (Postpartum):
- Risk Level: {risk_level}
- Mood Risk: {mood_risk}
- Age: {profile.get("age")}
- Diet Preference: {profile.get("diet_preference")}
- Medical History: {profile.get("medical_history")}

Provide postpartum recovery guidance:
- Physical recovery
- Emotional well-being
- Breastfeeding support
- Rest & nutrition

Include stronger doctor suggestion if risk_level is High.
Include mental health check-in if mood_risk is not Low.
Include disclaimer: "This is supportive guidance, not a medical diagnosis."
Return JSON only.
"""


def build_diet_prompt(data: dict):
    return f"""
Focus specifically on diet personalization.
Diet flags: {data.get("diet_flags")}
Diet preference: {data.get("user_profile", {}).get("diet_preference")}
Return JSON only.
"""


def build_mental_health_prompt(data: dict):
    return f"""
Mood risk level: {data.get("mood_risk")}
Provide supportive, calming coping strategies.
Do not diagnose.
Return JSON only.
"""