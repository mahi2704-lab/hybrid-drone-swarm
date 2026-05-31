
import { Link } from "react-router-dom";
import { useEffect, useState } from "react";

export default function Home() {
  const disasters = [
    "Flood",
    "Fire",
    "Earthquake",
    "Cyclone",
    "Landslide"
  ];

  const [disaster, setDisaster] = useState("Flood");
  const [battery, setBattery] = useState(92);
  const [wind, setWind] = useState(24);
  const [drones, setDrones] = useState(6);
  const [survivors, setSurvivors] = useState(5);

  useEffect(() => {
    const timer = setInterval(() => {
      setBattery(Math.floor(Math.random() * 30) + 70);
      setWind(Math.floor(Math.random() * 40) + 10);
      setDrones(Math.floor(Math.random() * 6) + 5);
      setSurvivors(Math.floor(Math.random() * 12) + 1);

      const randomDisaster =
        disasters[Math.floor(Math.random() * disasters.length)];

      setDisaster(randomDisaster);
    }, 5000);

    return () => clearInterval(timer);
  }, []);

  return (
    <div
      style={{
        background: "#020617",
        color: "white",
        minHeight: "100vh",
        padding: "30px"
      }}
    >
      <div
        style={{
          textAlign: "center",
          marginBottom: "30px"
        }}
      >
        <h1
          style={{
            fontSize: "42px",
            lineHeight: "1.3"
          }}
        >
          Hybrid Edge-Cloud Multi-Agent Drone Swarm Framework
        </h1>

        <h2
          style={{
            color: "#38bdf8"
          }}
        >
          Secure AI-Based Disaster Response
        </h2>

        <p
          style={{
            color: "#94a3b8",
            maxWidth: "900px",
            margin: "auto"
          }}
        >
          AI Powered Autonomous Rescue Coordination using Drone Swarm
          Intelligence, CNN-Based Survivor Detection, Edge AI Processing,
          Cloud Orchestration and Real-Time Mission Telemetry.
        </p>
      </div>

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(4,1fr)",
          gap: "15px",
          marginBottom: "30px"
        }}
      >
        <div
          style={{
            background: "#1e293b",
            padding: "20px",
            borderRadius: "10px"
          }}
        >
          <h3>Disaster Type</h3>
          <h2 style={{ color: "#ef4444" }}>{disaster}</h2>
        </div>

        <div
          style={{
            background: "#1e293b",
            padding: "20px",
            borderRadius: "10px"
          }}
        >
          <h3>Active Drones</h3>
          <h2 style={{ color: "#38bdf8" }}>{drones}</h2>
        </div>

        <div
          style={{
            background: "#1e293b",
            padding: "20px",
            borderRadius: "10px"
          }}
        >
          <h3>Wind Speed</h3>
          <h2 style={{ color: "#facc15" }}>{wind} km/h</h2>
        </div>

        <div
          style={{
            background: "#1e293b",
            padding: "20px",
            borderRadius: "10px"
          }}
        >
          <h3>Detected Survivors</h3>
          <h2 style={{ color: "#22c55e" }}>{survivors}</h2>
        </div>
      </div>

      <div
        style={{
          background: "#0f172a",
          padding: "25px",
          borderRadius: "12px",
          marginBottom: "30px"
        }}
      >
        <h2 style={{ marginBottom: "15px" }}>
          Drone Swarm Telemetry
        </h2>

        <div
          style={{
            display: "grid",
            gridTemplateColumns: "repeat(3,1fr)",
            gap: "15px"
          }}
        >
          <div style={{ background: "#1e293b", padding: "15px", borderRadius: "10px" }}>
            <h3>Drone-01</h3>
            <p>Battery: {battery}%</p>
            <p>Altitude: 120m</p>
            <p>Status: Searching</p>
          </div>

          <div style={{ background: "#1e293b", padding: "15px", borderRadius: "10px" }}>
            <h3>Drone-02</h3>
            <p>Battery: {battery - 8}%</p>
            <p>Altitude: 140m</p>
            <p>Status: Tracking</p>
          </div>

          <div style={{ background: "#1e293b", padding: "15px", borderRadius: "10px" }}>
            <h3>Drone-03</h3>
            <p>Battery: {battery - 12}%</p>
            <p>Altitude: 110m</p>
            <p>Status: Mapping</p>
          </div>
        </div>
      </div>

      <div
        style={{
          textAlign: "center"
        }}
      >
        <Link to="/dashboard">
          <button
            style={{
              padding: "15px 40px",
              fontSize: "18px",
              background: "#2563eb",
              color: "white",
              border: "none",
              borderRadius: "10px",
              cursor: "pointer"
            }}
          >
            Launch Mission Control
          </button>
        </Link>
      </div>
    </div>
  );
}

