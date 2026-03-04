import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import Profile from "./pages/Profile";
import Dashboard from "./pages/Dashboard";
import Mood from "./pages/Mood";
import Kicks from "./pages/Kicks";
import Advice from "./pages/Advice";

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Navigate to="/profile" />} />
        <Route path="/profile" element={<Profile />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/mood" element={<Mood />} />
        <Route path="/kicks" element={<Kicks />} />
        <Route path="/advice" element={<Advice />} />
      </Routes>
    </BrowserRouter>
  );
}