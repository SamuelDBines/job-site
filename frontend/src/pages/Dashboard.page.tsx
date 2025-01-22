import React from "react";
import { useNavigate } from "react-router-dom";

const Dashboard: React.FC = () => {
  const navigate = useNavigate();

  const handleLogout = () => {
    console.log("User logged out");
    // Add logout logic here (e.g., clear tokens or session)
    navigate("/login");
  };

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h1>Welcome to the Dashboard</h1>
      <button onClick={handleLogout} style={{ padding: "10px 20px", backgroundColor: "#4a90e2", color: "#fff", border: "none", borderRadius: "4px", cursor: "pointer" }}>
        Logout
      </button>
    </div>
  );
};

export default Dashboard;
