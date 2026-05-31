import React, { useState, useEffect } from "react";
import "./App.css";

function App() {
  const totalDrones = 5;

  const [anomalies, setAnomalies] = useState(1);
  const [survivors, setSurvivors] = useState(1);
  const [criticalBattery, setCriticalBattery] = useState(0);

  const [drones, setDrones] = useState([
    { name: "DRONE_1", battery: 20, status: "CHARGING" },
    { name: "DRONE_2", battery: 21, status: "AVOIDING_OBSTACLE" },
    { name: "DRONE_3", battery: 96, status: "SEARCHING" },
    { name: "DRONE_4", battery: 97, status: "SEARCHING" },
    { name: "DRONE_5", battery: 88, status: "SURVEYING" }
  ]);

  useEffect(() => {
    const interval = setInterval(() => {
      setDrones((prevDrones) => {
        const updated = prevDrones.map((drone) => {
          let newBattery = Math.max(
            0,
            Math.min(100, drone.battery + Math.floor(Math.random() * 11) - 5)
          );

          const statuses = [
            "SEARCHING",
            "CHARGING",
            "AVOIDING_OBSTACLE",
            "SURVIVOR_FOUND",
            "IDLE"
          ];

          return {
          <h1>LIVE UPDATE TEST 123</h1>
            ...drone,
            battery: newBattery,
            status: statuses[Math.floor(Math.random() * statuses.length)]
          };
        });

        setCriticalBattery(updated.filter((d) => d.battery < 20).length);

        return updated;
      });

      setAnomalies(Math.floor(Math.random() * 3));
      setSurvivors(Math.floor(Math.random() * 2));
    }, 3000);

    return () => clearInterval(interval);
  }, []);

  return (
    <div className="App">
      <h1>Hybrid Edge-Cloud Multi-Agent Drone Swarm Framework</h1>
      <h2>Secure AI-Based Disaster Response Dashboard</h2>

      <div>
        <h3>Total Drones: {totalDrones}</h3>
        <h3>Total Anomalies: {anomalies}</h3>
        <h3>Anomaly Percentage: {(anomalies / totalDrones) * 100}%</h3>
        <h3>Survivors Found: {survivors}</h3>
        <h3>Critical Battery Drones: {criticalBattery}</h3>
      </div>

      <div style={{ display: "flex", gap: "20px", flexWrap: "wrap" }}>
        {drones.map((drone, index) => (
          <div
            key={index}
            style={{
              border: "1px solid white",
              padding: "20px",
              width: "220px",
              borderRadius: "10px"
            }}
          >
            <h2>{drone.name}</h2>
            <p>Battery: {drone.battery}%</p>
            <p>Status: {drone.status}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;