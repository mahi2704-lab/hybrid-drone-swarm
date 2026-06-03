import React, { useEffect, useState } from "react";
import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer
} from "recharts";
import L from "leaflet";
import "leaflet/dist/leaflet.css";

/* ✅ FIXED IMPORT PATH (IMPORTANT) */
import floodImg from "../dataset/images/flood.jpeg";
import fireImg from "../dataset/images/fire.jpeg";
import earthquakeImg from "../dataset/images/earthquake.jpeg";

const icon = new L.Icon({
  iconUrl: "https://unpkg.com/leaflet@1.9.4/dist/images/marker-icon.png",
  shadowUrl: "https://unpkg.com/leaflet@1.9.4/dist/images/marker-shadow.png",
  iconSize: [25, 41],
  iconAnchor: [12, 41]
});

export default function Dashboard() {

  const disasters = [
    { name: "Flood Disaster Zone", img: floodImg },
    { name: "Wildfire Emergency Zone", img: fireImg },
    { name: "Earthquake Collapse Zone", img: earthquakeImg }
  ];

  const [activeIndex, setActiveIndex] = useState(0);
  const [active, setActive] = useState(disasters[0]);

  const [confidence, setConfidence] = useState(70);
  const [humanDetected, setHumanDetected] = useState(false);
  const [status, setStatus] = useState("");
  const [blockHash, setBlockHash] =
useState("0xA9F23C7D8E21B4FF");

const [consensus, setConsensus] =
useState("VALIDATED");

const [syncStatus, setSyncStatus] =
useState("CONNECTED");

  const [survivorsPos, setSurvivorsPos] = useState([
    [13.08, 80.27],
    [13.09, 80.28],
    [13.07, 80.25]
  ]);

  const [telemetry, setTelemetry] = useState([
    { t: "T1", battery: 90, signal: 80 },
    { t: "T2", battery: 88, signal: 82 },
    { t: "T3", battery: 85, signal: 78 }
  ]);

  /* 🔁 LIVE SIMULATION */
  useEffect(() => {
    const timer = setInterval(() => {
        // blockchain simulation
setBlockHash(
"0x" +
Math.random()
.toString(16)
.substring(2,18)
.toUpperCase()
);

setConsensus(
Math.random() > 0.2
? "VALIDATED"
: "PENDING"
);

setSyncStatus(
Math.random() > 0.1
? "CONNECTED"
: "SYNCING"
);

      // rotate disaster
      setActiveIndex(prev => {
        const next = (prev + 1) % disasters.length;
        setActive(disasters[next]);
        return next;
      });

      // move survivors
      setSurvivorsPos(prev =>
        prev.map(p => [
          p[0] + (Math.random() - 0.5) * 0.01,
          p[1] + (Math.random() - 0.5) * 0.01
        ])
      );

      // AI confidence
      setConfidence(Math.floor(60 + Math.random() * 40));

      // human detection simulation
      setHumanDetected(Math.random() > 0.5);

      // telemetry update
      setTelemetry(prev => [
        ...prev.slice(1),
        {
          t: "NOW",
          battery: 60 + Math.random() * 40,
          signal: 60 + Math.random() * 40
        }
      ]);

    }, 3000);

    return () => clearInterval(timer);
  }, []);

  return (
    <div style={{
      background: "#020617",
      color: "white",
      minHeight: "100vh",
      padding: "20px"
    }}>

      <h1 style={{ textAlign: "center" }}>
        AI Disaster Response Dashboard
      </h1>

      {/* MAP + CNN */}
      <div style={{
        display: "grid",
        gridTemplateColumns: "2fr 1fr",
        gap: "20px"
      }}>

        {/* MAP */}
        <div style={{
          background: "#1e293b",
          padding: "10px",
          borderRadius: "10px"
        }}>
          <h3>Live Disaster Map</h3>

          <MapContainer center={[13.08, 80.27]} zoom={12} style={{ height: "400px" }}>
            <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />

            {survivorsPos.map((p, i) => (
              <Marker key={i} position={p} icon={icon}>
                <Popup>Survivor {i + 1}</Popup>
              </Marker>
            ))}
          </MapContainer>
        </div>

        {/* CNN PANEL */}
        <div style={{
          background: "#1e293b",
          padding: "10px",
          borderRadius: "10px"
        }}>

          <h3>CNN Vision System</h3>

          <div style={{ position: "relative" }}>
            <img
              src={active.img}
              alt="disaster"
              style={{
                width: "100%",
                height: "200px",
                objectFit: "cover",
                borderRadius: "10px",
                border: "2px solid #334155"
              }}
            />

            {/* BOUNDING BOX */}
            {humanDetected && (
              <>
                <div style={{
                  position: "absolute",
                  top: "50px",
                  left: "60px",
                  width: "120px",
                  height: "90px",
                  border: "3px solid #22c55e",
                  boxShadow: "0 0 10px #22c55e",
                  borderRadius: "4px"
                }} />

                <div style={{
                  position: "absolute",
                  top: "20px",
                  left: "60px",
                  background: "#22c55e",
                  color: "black",
                  padding: "3px 6px",
                  fontSize: "12px",
                  fontWeight: "bold",
                  borderRadius: "4px",
                  animation: "blink 0.6s infinite"
                }}>
                  HUMAN DETECTED
                </div>
              </>
            )}
          </div>

          <div style={{ marginTop: "10px" }}>
            <b>{active.name}</b>
          </div>

          {/* CONFIDENCE */}
          <div style={{ marginTop: "15px" }}>
            <div style={{ display: "flex", justifyContent: "space-between" }}>
              <span>AI Confidence</span>
              <span>{confidence}%</span>
            </div>

            <div style={{
              height: "12px",
              background: "#334155",
              borderRadius: "6px",
              marginTop: "6px",
              overflow: "hidden"
            }}>
              <div style={{
                width: `${confidence}%`,
                height: "100%",
                background: "linear-gradient(90deg,#ef4444,#facc15,#22c55e)",
                transition: "width 0.5s ease"
              }} />
            </div>
          </div>
        </div>
      </div>

      {/* TELEMETRY */}
      <div style={{
        marginTop: "20px",
        background: "#1e293b",
        padding: "15px",
        borderRadius: "10px"
      }}>
        <h3>Drone Telemetry</h3>

        <ResponsiveContainer width="100%" height={250}>
          <LineChart data={telemetry}>
            <XAxis dataKey="t" />
            <YAxis />
            <Tooltip />
            <Line type="monotone" dataKey="battery" stroke="#22c55e" />
            <Line type="monotone" dataKey="signal" stroke="#38bdf8" />
          </LineChart>
        </ResponsiveContainer>
      </div>
      {/* BLOCKCHAIN SECURITY */}

<div
style={{
marginTop:"20px",
background:"#0f172a",
padding:"20px",
borderRadius:"12px",
border:"1px solid #22c55e"
}}
>

<h3
style={{
color:"#22c55e",
marginBottom:"15px"
}}
>
🔗 Blockchain Security Layer
</h3>

<div
style={{
display:"grid",
gridTemplateColumns:"1fr 1fr",
gap:"15px"
}}
>

<div
style={{
background:"#1e293b",
padding:"15px",
borderRadius:"10px"
}}
>
<div style={{color:"#94a3b8"}}>
Latest Block Hash
</div>

<div
style={{
marginTop:"10px",
fontSize:"12px",
wordBreak:"break-word",
color:"#38bdf8"
}}
>
{blockHash}
</div>

</div>

<div
style={{
background:"#1e293b",
padding:"15px",
borderRadius:"10px"
}}
>
<div style={{color:"#94a3b8"}}>
Cloud Synchronization
</div>

<div
style={{
marginTop:"10px",
color:"#22c55e",
fontWeight:"bold"
}}
>
{syncStatus}
</div>

</div>

<div
style={{
background:"#1e293b",
padding:"15px",
borderRadius:"10px"
}}
>
<div style={{color:"#94a3b8"}}>
Consensus
</div>

<div
style={{
marginTop:"10px",
color:"#facc15",
fontWeight:"bold"
}}
>
{consensus}
</div>

</div>

<div
style={{
background:"#1e293b",
padding:"15px",
borderRadius:"10px"
}}
>
<div style={{color:"#94a3b8"}}>
Mission Security
</div>

<div
style={{
marginTop:"10px",
color:"#22c55e",
fontWeight:"bold"
}}
>
ACTIVE
</div>

</div>

</div>

</div>

      {/* CONTROL */}
      <div style={{
        marginTop: "20px",
        background: "#1e293b",
        padding: "15px",
        borderRadius: "10px"
      }}>
        <h3>Control Panel</h3>

        <button
          onClick={() => setStatus("🚑 Rescue Team Deployed Successfully")}
          style={{
            background: "#dc2626",
            color: "white",
            padding: "12px 20px",
            border: "none",
            borderRadius: "8px",
            cursor: "pointer"
          }}
        >
          Deploy Rescue Team
        </button>

        {status && (
          <div style={{
            marginTop: "10px",
            color: "#22c55e",
            fontWeight: "bold"
          }}>
            {status}
          </div>
        )}
      </div>

      {/* ANIMATION */}
      <style>
        {`
          @keyframes blink {
            0% { opacity: 1; }
            50% { opacity: 0; }
            100% { opacity: 1; }
          }
        `}
      </style>

    </div>
  );
}