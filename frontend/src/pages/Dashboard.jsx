import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

export default function Dashboard() {
  const navigate = useNavigate();
  const [profile, setProfile] = useState(null);

  useEffect(() => {
    const saved = localStorage.getItem("profile");
    if (saved) setProfile(JSON.parse(saved));
    else navigate("/profile");
  }, []);

  if (!profile) return null;

  const trimester =
    profile.week <= 12 ? "1st Trimester" :
    profile.week <= 26 ? "2nd Trimester" : "3rd Trimester";

  const progress = Math.round((profile.week / 40) * 100);

  return (
    <div className="min-h-screen" style={{ background: "linear-gradient(135deg, #fdf2f8, #ede9fe)" }}>
      
      {/* Navbar */}
      <nav className="bg-white shadow-sm px-8 py-4 flex justify-between items-center">
        <div className="flex items-center gap-2">
          <span className="text-2xl">🤰</span>
          <span className="text-xl font-bold text-pink-500">MomCare AI</span>
        </div>
        <div className="flex gap-6 text-sm font-medium text-gray-500">
          <button onClick={() => navigate("/dashboard")} className="text-pink-500 font-semibold">Dashboard</button>
          <button onClick={() => navigate("/mood")} className="hover:text-pink-400 transition">Mood</button>
          <button onClick={() => navigate("/kicks")} className="hover:text-pink-400 transition">Kicks</button>
          <button onClick={() => navigate("/advice")} className="hover:text-pink-400 transition">Advice</button>
        </div>
        <button
          onClick={() => navigate("/profile")}
          className="text-sm bg-pink-100 text-pink-500 px-4 py-2 rounded-full font-medium hover:bg-pink-200 transition"
        >
          ✏️ Edit Profile
        </button>
      </nav>

      <div className="max-w-5xl mx-auto px-6 py-10">

        {/* Welcome Banner */}
        <div className="rounded-3xl p-8 mb-8 text-white" style={{ background: "linear-gradient(to right, #f472b6, #a78bfa)" }}>
          <h1 className="text-3xl font-bold mb-1">Hello, {profile.name} 👋</h1>
          <p className="text-pink-100 text-sm">You are in your <strong>{trimester}</strong> — Week {profile.week} of 40</p>
          <div className="mt-4 bg-white bg-opacity-30 rounded-full h-3 w-full">
            <div
              className="bg-white rounded-full h-3 transition-all duration-500"
              style={{ width: `${progress}%` }}
            ></div>
          </div>
          <p className="text-xs text-pink-100 mt-1">{progress}% of pregnancy completed</p>
        </div>

        {/* Quick Stats */}
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-8">
          {[
            { icon: "🗓️", label: "Current Week", value: `Week ${profile.week}` },
            { icon: "🥗", label: "Diet Type", value: profile.diet === "veg" ? "Vegetarian" : "Non-Veg" },
            { icon: "💊", label: "Condition", value: profile.condition.charAt(0).toUpperCase() + profile.condition.slice(1) },
            { icon: "👶", label: "Trimester", value: trimester },
          ].map((stat, i) => (
            <div key={i} className="bg-white rounded-2xl p-5 shadow-sm text-center">
              <div className="text-3xl mb-2">{stat.icon}</div>
              <div className="text-xs text-gray-400 font-medium">{stat.label}</div>
              <div className="text-sm font-bold text-gray-700 mt-1">{stat.value}</div>
            </div>
          ))}
        </div>

        {/* Quick Actions */}
        <h2 className="text-lg font-bold text-gray-700 mb-4">Quick Actions</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          {[
            { icon: "😊", title: "Log Your Mood", desc: "How are you feeling today?", path: "/mood", color: "#fdf2f8", border: "#f9a8d4" },
            { icon: "👣", title: "Track Baby Kicks", desc: "Count and log baby movements", path: "/kicks", color: "#ede9fe", border: "#c4b5fd" },
            { icon: "💡", title: "Get AI Advice", desc: "Personalized tips for your week", path: "/advice", color: "#ecfdf5", border: "#6ee7b7" },
          ].map((card, i) => (
            <button
              key={i}
              onClick={() => navigate(card.path)}
              className="text-left rounded-2xl p-6 shadow-sm hover:shadow-md transition-all duration-200 hover:scale-105 border"
              style={{ background: card.color, borderColor: card.border }}
            >
              <div className="text-4xl mb-3">{card.icon}</div>
              <div className="font-bold text-gray-700 text-base">{card.title}</div>
              <div className="text-xs text-gray-400 mt-1">{card.desc}</div>
            </button>
          ))}
        </div>

      </div>
    </div>
  );
}