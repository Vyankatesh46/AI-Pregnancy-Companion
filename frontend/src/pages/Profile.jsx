import { useState } from "react";
import { useNavigate } from "react-router-dom";

export default function Profile() {
  const navigate = useNavigate();
  const [form, setForm] = useState({
    name: "",
    week: "",
    diet: "veg",
    condition: "normal",
  });

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    localStorage.setItem("profile", JSON.stringify(form));
    navigate("/dashboard");
  };

  return (
    <div className="min-h-screen flex items-center justify-center" style={{ background: "linear-gradient(135deg, #fdf2f8, #ede9fe)" }}>
      <div className="bg-white rounded-3xl shadow-xl p-10 w-full max-w-md">
        
        {/* Header */}
        <div className="text-center mb-8">
          <div className="text-5xl mb-3">🤰</div>
          <h1 className="text-3xl font-bold text-gray-800">Welcome</h1>
          <p className="text-gray-400 mt-1 text-sm">Let's set up your pregnancy profile</p>
        </div>

        <form onSubmit={handleSubmit} className="space-y-5">
          
          {/* Name */}
          <div>
            <label className="block text-sm font-medium text-gray-600 mb-1">Your Name</label>
            <input
              type="text"
              name="name"
              placeholder="Enter your name"
              value={form.name}
              onChange={handleChange}
              required
              className="w-full px-4 py-3 rounded-xl border border-gray-200 focus:outline-none focus:ring-2 focus:ring-pink-300 text-gray-700"
            />
          </div>

          {/* Pregnancy Week */}
          <div>
            <label className="block text-sm font-medium text-gray-600 mb-1">Pregnancy Week</label>
            <input
              type="number"
              name="week"
              placeholder="e.g. 24"
              min="1"
              max="42"
              value={form.week}
              onChange={handleChange}
              required
              className="w-full px-4 py-3 rounded-xl border border-gray-200 focus:outline-none focus:ring-2 focus:ring-pink-300 text-gray-700"
            />
          </div>

          {/* Diet */}
          <div>
            <label className="block text-sm font-medium text-gray-600 mb-1">Diet Type</label>
            <select
              name="diet"
              value={form.diet}
              onChange={handleChange}
              className="w-full px-4 py-3 rounded-xl border border-gray-200 focus:outline-none focus:ring-2 focus:ring-pink-300 text-gray-700 bg-white"
            >
              <option value="veg">🥦 Vegetarian</option>
              <option value="nonveg">🍗 Non-Vegetarian</option>
            </select>
          </div>

          {/* Condition */}
          <div>
            <label className="block text-sm font-medium text-gray-600 mb-1">Health Condition</label>
            <select
              name="condition"
              value={form.condition}
              onChange={handleChange}
              className="w-full px-4 py-3 rounded-xl border border-gray-200 focus:outline-none focus:ring-2 focus:ring-pink-300 text-gray-700 bg-white"
            >
              <option value="normal">✅ Normal</option>
              <option value="diabetic">🩸 Diabetic</option>
              <option value="anemic">💊 Anemic</option>
            </select>
          </div>

          {/* Submit Button */}
          <button
            type="submit"
            className="w-full py-3 rounded-xl text-white font-semibold text-lg mt-2 transition-all duration-200 hover:opacity-90 hover:scale-105"
            style={{ background: "linear-gradient(to right, #f472b6, #a78bfa)" }}
          >
            Save & Continue →
          </button>

        </form>
      </div>
    </div>
  );
}