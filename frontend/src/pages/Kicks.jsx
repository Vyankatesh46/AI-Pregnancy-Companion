import { useState } from "react";
import { useNavigate } from "react-router-dom";

export default function Kicks() {
  const navigate = useNavigate();
  const [kicks, setKicks] = useState(0);
  const [sessions, setSessions] = useState(() => {
    const stored = localStorage.getItem("kickSessions");
    return stored ? JSON.parse(stored) : [];
  });
  const [timer, setTimer] = useState(0);
  const [running, setRunning] = useState(false);
  const [intervalId, setIntervalId] = useState(null);
  const [lastKickTime, setLastKickTime] = useState(null);

  const startSession = () => {
    setKicks(0);
    setTimer(0);
    setRunning(true);
    setLastKickTime(null);
    const id = setInterval(() => {
      setTimer((prev) => prev + 1);
    }, 1000);
    setIntervalId(id);
  };

  const logKick = () => {
    if (!running) return;
    setKicks((prev) => prev + 1);
    setLastKickTime(new Date().toLocaleTimeString());
  };

  const stopSession = () => {
    clearInterval(intervalId);
    setRunning(false);
    const session = {
      kicks,
      duration: timer,
      date: new Date().toLocaleDateString("en-IN", {
        day: "numeric", month: "short", year: "numeric",
        hour: "2-digit", minute: "2-digit",
      }),
    };
    const updated = [session, ...sessions];
    setSessions(updated);
    localStorage.setItem("kickSessions", JSON.stringify(updated));
  };

  const formatTime = (seconds) => {
    const m = Math.floor(seconds / 60).toString().padStart(2, "0");
    const s = (seconds % 60).toString().padStart(2, "0");
    return `${m}:${s}`;
  };

  const getStatus = () => {
    if (kicks >= 10) return { text: "✅ Great! Baby is very active!", color: "text-green-500" };
    if (kicks >= 5) return { text: "👍 Good movement detected", color: "text-purple-500" };
    return { text: "👀 Keep counting...", color: "text-pink-400" };
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
          <button onClick={() => navigate("/mood")} className="hover:text-pink-400 transition">Mood</button>
          <button onClick={() => navigate("/kicks")} className="text-pink-500 font-semibold">Kicks</button>
          <button onClick={() => navigate("/advice")} className="hover:text-pink-400 transition">Advice</button>
        </div>
      </nav>

      <div className="max-w-2xl mx-auto px-6 py-10">

        {/* Header */}
        <div className="text-center mb-8">
          <div className="text-5xl mb-3">👣</div>
          <h1 className="text-3xl font-bold text-gray-800">Baby Kick Tracker</h1>
          <p className="text-gray-400 text-sm mt-1">Count 10 kicks — healthy babies kick 10 times in 2 hours</p>
        </div>

        {/* Main Counter Card */}
        <div className="bg-white rounded-3xl shadow-sm p-8 mb-6 text-center">

          {/* Kick Count */}
          <div
            className="w-40 h-40 rounded-full mx-auto flex flex-col items-center justify-center mb-6 shadow-inner"
            style={{ background: "linear-gradient(135deg, #fdf2f8, #ede9fe)" }}
          >
            <div className="text-6xl font-bold text-pink-500">{kicks}</div>
            <div className="text-xs text-gray-400 mt-1">kicks</div>
          </div>

          {/* Timer */}
          <div className="text-2xl font-mono font-semibold text-purple-400 mb-2">
            ⏱ {formatTime(timer)}
          </div>

          {/* Status */}
          {running && (
            <p className={`text-sm font-medium mb-4 ${getStatus().color}`}>
              {getStatus().text}
            </p>
          )}

          {/* Last Kick */}
          {lastKickTime && (
            <p className="text-xs text-gray-400 mb-4">Last kick at {lastKickTime}</p>
          )}

          {/* Buttons */}
          <div className="flex gap-3 justify-center mt-4">
            {!running ? (
              <button
                onClick={startSession}
                className="px-8 py-3 rounded-xl text-white font-semibold transition-all hover:scale-105"
                style={{ background: "linear-gradient(to right, #f472b6, #a78bfa)" }}
              >
                ▶ Start Session
              </button>
            ) : (
              <>
                <button
                  onClick={logKick}
                  className="px-8 py-4 rounded-xl text-white font-bold text-lg transition-all hover:scale-105 shadow-md"
                  style={{ background: "linear-gradient(to right, #f472b6, #a78bfa)" }}
                >
                  👣 Kick!
                </button>
                <button
                  onClick={stopSession}
                  className="px-6 py-3 rounded-xl bg-gray-100 text-gray-600 font-semibold hover:bg-gray-200 transition"
                >
                  ⏹ Stop
                </button>
              </>
            )}
          </div>
        </div>

        {/* Sessions History */}
        {sessions.length > 0 && (
          <div>
            <h2 className="text-lg font-bold text-gray-700 mb-4">Previous Sessions</h2>
            <div className="space-y-3">
              {sessions.slice(0, 5).map((s, i) => (
                <div key={i} className="bg-white rounded-2xl px-5 py-4 shadow-sm flex items-center justify-between">
                  <div className="flex items-center gap-3">
                    <div className="text-2xl">👣</div>
                    <div>
                      <div className="font-semibold text-gray-700">{s.kicks} kicks</div>
                      <div className="text-xs text-gray-400">Duration: {formatTime(s.duration)}</div>
                    </div>
                  </div>
                  <div className="text-xs text-gray-400">{s.date}</div>
                </div>
              ))}
            </div>
          </div>
        )}

      </div>
    </div>
  );
}