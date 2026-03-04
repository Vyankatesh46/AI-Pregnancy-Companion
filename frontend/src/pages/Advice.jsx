import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";

const adviceData = {
  1: {
    tip: "Take folic acid daily. Avoid alcohol and smoking completely.",
    food: ["Leafy greens", "Oranges", "Fortified cereals", "Beans"],
    exercise: "Light walking 15 mins/day",
    warning: "Avoid raw fish, unpasteurized dairy",
  },
  2: {
    tip: "Morning sickness is normal. Eat small frequent meals.",
    food: ["Ginger tea", "Crackers", "Bananas", "Yogurt"],
    exercise: "Gentle stretching and walking",
    warning: "Avoid spicy and oily foods",
  },
  3: {
    tip: "Your baby's heart starts beating! Stay hydrated.",
    food: ["Water-rich fruits", "Milk", "Eggs", "Spinach"],
    exercise: "Prenatal yoga beginner poses",
    warning: "Avoid caffeine above 200mg/day",
  },
};

const getAdvice = (week, diet, condition) => {
  const weekGroup = week <= 12 ? 1 : week <= 26 ? 2 : 3;
  const base = adviceData[weekGroup];

  let extra = [];
  if (condition === "diabetic") extra.push("🩸 Avoid sugary foods. Monitor blood sugar regularly.");
  if (condition === "anemic") extra.push("💊 Take iron supplements. Eat iron-rich foods daily.");
  if (diet === "veg") extra.push("🥦 Ensure you get enough protein from lentils, tofu, and dairy.");

  return { ...base, extra };
};

export default function Advice() {
  const navigate = useNavigate();
  const [profile, setProfile] = useState(null);
  const [advice, setAdvice] = useState(null);
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const saved = localStorage.getItem("profile");
    if (saved) {
      const p = JSON.parse(saved);
      setProfile(p);
      setAdvice(getAdvice(Number(p.week), p.diet, p.condition));
    } else {
      navigate("/profile");
    }
  }, []);

  const handleAsk = () => {
    if (!question.trim()) return;
    setLoading(true);
    setAnswer("");
    setTimeout(() => {
      setAnswer(
        `Based on your Week ${profile.week} pregnancy: "${question}" — Always consult your doctor for medical advice. Generally, staying hydrated, eating balanced meals, and getting rest are key. 💗`
      );
      setLoading(false);
    }, 1500);
  };

  if (!profile || !advice) return null;

  return (
    <div className="min-h-screen" style={{ background: "linear-gradient(135deg, #fdf2f8, #ede9fe)" }}>

      {/* Navbar */}
      <nav className="bg-white shadow-sm px-8 py-4 flex justify-between items-center">
        <div className="flex items-center gap-2">
          <span className="text-2xl">🤰</span>
          <span className="text-xl font-bold text-pink-500">MomCare AI</span>
        </div>
        <div className="flex gap-6 text-sm font-medium text-gray-500">
          <button onClick={() => navigate("/dashboard")} className="hover:text-pink-400 transition">Dashboard</button>
          <button onClick={() => navigate("/mood")} className="hover:text-pink-400 transition">Mood</button>
          <button onClick={() => navigate("/kicks")} className="hover:text-pink-400 transition">Kicks</button>
          <button onClick={() => navigate("/advice")} className="text-pink-500 font-semibold">Advice</button>
        </div>
      </nav>

      <div className="max-w-3xl mx-auto px-6 py-10">

        {/* Header */}
        <div className="text-center mb-8">
          <div className="text-5xl mb-3">💡</div>
          <h1 className="text-3xl font-bold text-gray-800">AI Pregnancy Advice</h1>
          <p className="text-gray-400 text-sm mt-1">Personalized for Week {profile.week} • {profile.diet === "veg" ? "Vegetarian" : "Non-Veg"} • {profile.condition}</p>
        </div>

        {/* Tip of the Day */}
        <div className="rounded-3xl p-6 mb-6 text-white" style={{ background: "linear-gradient(to right, #f472b6, #a78bfa)" }}>
          <h2 className="font-bold text-lg mb-2">💬 Tip of the Day</h2>
          <p className="text-pink-100 text-sm leading-relaxed">{advice.tip}</p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">

          {/* Food Recommendations */}
          <div className="bg-white rounded-3xl p-6 shadow-sm">
            <h2 className="font-bold text-gray-700 mb-3">🥗 Recommended Foods</h2>
            <ul className="space-y-2">
              {advice.food.map((f, i) => (
                <li key={i} className="flex items-center gap-2 text-sm text-gray-600">
                  <span className="w-2 h-2 rounded-full bg-pink-300 inline-block"></span>
                  {f}
                </li>
              ))}
            </ul>
          </div>

          {/* Exercise */}
          <div className="bg-white rounded-3xl p-6 shadow-sm">
            <h2 className="font-bold text-gray-700 mb-3">🏃‍♀️ Exercise</h2>
            <p className="text-sm text-gray-600">{advice.exercise}</p>

            <h2 className="font-bold text-gray-700 mt-5 mb-3">⚠️ Avoid</h2>
            <p className="text-sm text-red-400">{advice.warning}</p>
          </div>
        </div>

        {/* Personalized Tips */}
        {advice.extra.length > 0 && (
          <div className="bg-white rounded-3xl p-6 shadow-sm mb-6">
            <h2 className="font-bold text-gray-700 mb-3">✨ Personalized for You</h2>
            <ul className="space-y-2">
              {advice.extra.map((e, i) => (
                <li key={i} className="text-sm text-gray-600 bg-pink-50 rounded-xl px-4 py-2">{e}</li>
              ))}
            </ul>
          </div>
        )}

        {/* Ask AI */}
        <div className="bg-white rounded-3xl p-6 shadow-sm">
          <h2 className="font-bold text-gray-700 mb-3">🤖 Ask AI</h2>
          <div className="flex gap-3">
            <input
              type="text"
              placeholder="e.g. Can I eat papaya? Is back pain normal?"
              value={question}
              onChange={(e) => setQuestion(e.target.value)}
              onKeyDown={(e) => e.key === "Enter" && handleAsk()}
              className="flex-1 px-4 py-3 rounded-xl border border-gray-200 focus:outline-none focus:ring-2 focus:ring-pink-300 text-gray-700 text-sm"
            />
            <button
              onClick={handleAsk}
              className="px-6 py-3 rounded-xl text-white font-semibold transition-all hover:scale-105"
              style={{ background: "linear-gradient(to right, #f472b6, #a78bfa)" }}
            >
              Ask
            </button>
          </div>

          {loading && (
            <div className="mt-4 text-center text-pink-400 text-sm animate-pulse">
              🤔 Thinking...
            </div>
          )}

          {answer && (
            <div className="mt-4 bg-pink-50 rounded-2xl px-5 py-4 text-sm text-gray-600 leading-relaxed">
              💗 {answer}
            </div>
          )}
        </div>

      </div>
    </div>
  );
}