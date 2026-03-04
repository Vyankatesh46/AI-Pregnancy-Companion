import { useState } from "react";
import { useNavigate } from "react-router-dom";

const moods = [
  { emoji: "😄", label: "Happy", color: "#fef9c3" },
  { emoji: "😌", label: "Calm", color: "#ecfdf5" },
  { emoji: "😔", label: "Sad", color: "#ede9fe" },
  { emoji: "😰", label: "Anxious", color: "#fff7ed" },
  { emoji: "😴", label: "Tired", color: "#f1f5f9" },
  { emoji: "🤢", label: "Nauseous", color: "#fdf2f8" },
];

export default function Mood() {
  const navigate = useNavigate();
  const [selected, setSelected] = useState(null);
  const [note, setNote] = useState("");
  const [saved, setSaved] = useState(false);
  const [history, setHistory] = useState(() => {
    const stored = localStorage.getItem("moodHistory");
    return stored ? JSON.parse(stored) : [];
  });

  const handleSave = () => {
    if (!selected) return;
    const entry = {
      mood: selected,
      note,
      date: new Date().toLocaleDateString("en-IN", {
        day: "numeric", month: "short", year: "numeric",
        hour: "2-digit", minute: "2-digit",
      }),
    };
    const updated = [entry, ...history];
    setHistory(updated);
    localStorage.setItem("moodHistory", JSON.stringify(updated));
    setSaved(true);
    setNote("");
    setSelected(null);
    setTimeout(() => setSaved(false), 2000);
  };

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
          <button onClick={() => navigate("/mood")} className="text-pink-500 font-semibold">Mood</button>
          <button onClick={() => navigate("/kicks")} className="hover:text-pink-400 transition">Kicks</button>
          <button onClick={() => navigate("/advice")} className="hover:text-pink-400 transition">Advice</button>
        </div>
      </nav>

      <div className="max-w-2xl mx-auto px-6 py-10">

        {/* Header */}
        <div className="text-center mb-8">
          <div className="text-5xl mb-3">😊</div>
          <h1 className="text-3xl font-bold text-gray-800">How are you feeling?</h1>
          <p className="text-gray-400 text-sm mt-1">Track your mood every day for better insights</p>
        </div>

        {/* Mood Selector */}
        <div className="bg-white rounded-3xl shadow-sm p-6 mb-6">
          <h2 className="text-sm font-semibold text-gray-500 mb-4">SELECT YOUR MOOD</h2>
          <div className="grid grid-cols-3 gap-3">
            {moods.map((m) => (
              <button
                key={m.label}
                onClick={() => setSelected(m)}
                className={`rounded-2xl p-4 text-center transition-all duration-200 hover:scale-105 border-2 ${
                  selected?.label === m.label
                    ? "border-pink-400 shadow-md scale-105"
                    : "border-transparent"
                }`}
                style={{ background: m.color }}
              >
                <div className="text-4xl mb-1">{m.emoji}</div>
                <div className="text-xs font-medium text-gray-600">{m.label}</div>
              </button>
            ))}
          </div>
        </div>

        {/* Note */}
        <div className="bg-white rounded-3xl shadow-sm p-6 mb-6">
          <h2 className="text-sm font-semibold text-gray-500 mb-3">ADD A NOTE (optional)</h2>
          <textarea
            rows={3}
            placeholder="What's on your mind today?"
            value={note}
            onChange={(e) => setNote(e.target.value)}
            className="w-full px-4 py-3 rounded-xl border border-gray-200 focus:outline-none focus:ring-2 focus:ring-pink-300 text-gray-700 resize-none text-sm"
          />
        </div>

        {/* Save Button */}
        <button
          onClick={handleSave}
          disabled={!selected}
          className={`w-full py-3 rounded-xl text-white font-semibold text-lg transition-all duration-200 ${
            selected ? "hover:opacity-90 hover:scale-105" : "opacity-40 cursor-not-allowed"
          }`}
          style={{ background: "linear-gradient(to right, #f472b6, #a78bfa)" }}
        >
          {saved ? "✅ Mood Saved!" : "Save Mood"}
        </button>

        {/* History */}
        {history.length > 0 && (
          <div className="mt-8">
            <h2 className="text-lg font-bold text-gray-700 mb-4">Recent Mood History</h2>
            <div className="space-y-3">
              {history.slice(0, 5).map((entry, i) => (
                <div key={i} className="bg-white rounded-2xl px-5 py-4 shadow-sm flex items-center gap-4">
                  <div className="text-3xl">{entry.mood.emoji}</div>
                  <div className="flex-1">
                    <div className="font-semibold text-gray-700">{entry.mood.label}</div>
                    {entry.note && <div className="text-xs text-gray-400 mt-0.5">{entry.note}</div>}
                  </div>
                  <div className="text-xs text-gray-400">{entry.date}</div>
                </div>
              ))}
            </div>
          </div>
        )}

      </div>
    </div>
  );
}