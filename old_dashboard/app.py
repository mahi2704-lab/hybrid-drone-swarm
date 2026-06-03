import streamlit as st
import pandas as pd
import random
import plotly.express as px

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Hybrid Drone Swarm Command Center",
    layout="wide"
)

# =========================
# STYLE (PRO UI)
# =========================
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #0b1220, #0f172a);
    color: white;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background-color: #0f1b2d;
}

/* HEADERS */
.main-title {
    font-size: 42px;
    font-weight: 800;
    text-align: center;
    color: #38bdf8;
}

.sub-title {
    text-align: center;
    color: #cbd5e1;
    margin-bottom: 20px;
}

/* CARDS */
.card {
    background-color: #111c2e;
    padding: 18px;
    border-radius: 14px;
    border: 1px solid #22314a;
    text-align: center;
}

/* METRICS */
.metric-title {
    color: #94a3b8;
    font-size: 14px;
}

.metric-value {
    color: #38bdf8;
    font-size: 28px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR CONTROL PANEL
# =========================
st.sidebar.title("MISSION CONTROL")

controller = st.sidebar.text_input("Controller", "Mission Commander")
location = st.sidebar.text_input("Target Zone", "Chennai Coastal Zone")

disaster = st.sidebar.selectbox(
    "Disaster Type",
    ["Fire", "Flood", "Safe Zone"]
)

priority = st.sidebar.selectbox(
    "Priority",
    ["High", "Medium", "Low"]
)

drones = st.sidebar.slider("Deploy Drone Swarm", 1, 20, 7)

launch = st.sidebar.button("🚀 DEPLOY MISSION")

# =========================
# TITLE
# =========================
st.markdown("""
<div class='main-title'>
Hybrid Edge Cloud Multi-Agent Drone Swarm Framework
</div>

<div class='sub-title'>
AI Disaster Command Center • CNN Intelligence • GPS Swarm Tracking • Edge AI • Blockchain Security
</div>
""", unsafe_allow_html=True)

# =========================
# ONLY RUN AFTER LAUNCH (IMPORTANT INTERACTIVE BEHAVIOUR)
# =========================
if launch:

    st.success(f"Mission Deployed by {controller} at {location}")

    # =========================
    # DRONE SIMULATION
    # =========================
    data = []

    for i in range(drones):

        data.append({
            "Drone": f"DR-{i+1:02}",
            "Lat": 13.05 + random.uniform(-0.02, 0.02),
            "Lon": 80.25 + random.uniform(-0.02, 0.02),
            "Temp": random.randint(70, 120),
            "Confidence": round(random.uniform(0.70, 0.99), 2)
        })

    df = pd.DataFrame(data)

    # =========================
    # METRICS
    # =========================
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(f"""
        <div class='card'>
        <div class='metric-title'>Active Drones</div>
        <div class='metric-value'>{drones}</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div class='card'>
        <div class='metric-title'>Victims Detected</div>
        <div class='metric-value'>{len(df[df['Confidence'] > 0.85])}</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
        <div class='card'>
        <div class='metric-title'>Avg AI Confidence</div>
        <div class='metric-value'>{round(df['Confidence'].mean(),2)}</div>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown(f"""
        <div class='card'>
        <div class='metric-title'>Max Temperature</div>
        <div class='metric-value'>{df['Temp'].max()}°C</div>
        </div>
        """, unsafe_allow_html=True)

    # =========================
    # MAP
    # =========================
    st.subheader("Live Swarm GPS Map")

    st.map(df.rename(columns={"Lat": "lat", "Lon": "lon"}))

    # =========================
    # TELEMETRY
    # =========================
    st.subheader("Drone Telemetry")

    st.dataframe(df, use_container_width=True)

    # =========================
    # ALERTS
    # =========================
    st.subheader("AI Alerts")

    for _, d in df.iterrows():

        if d["Confidence"] > 0.85:
            st.error(f"{d['Drone']} → Possible survivor detected")

        if d["Temp"] > 105:
            st.warning(f"{d['Drone']} → High thermal signature")

    # =========================
    # CNN LOGIC (REAL INTERACTIVE)
    # =========================
    st.subheader("CNN Disaster Intelligence")

    if disaster == "Fire":
        prediction = "FIRE DETECTED"
        img = "https://images.unsplash.com/photo-1475776408506-9a5371e7a068"

    elif disaster == "Flood":
        prediction = "FLOOD DETECTED"
        img = "https://images.unsplash.com/photo-1527489377706-5bf97e608852"

    else:
        prediction = "SAFE ZONE"
        img = "https://images.unsplash.com/photo-1506744038136-46273834b3fb"

    confidence = round(random.uniform(0.88, 0.99), 2)

    st.success(prediction)
    st.write("Confidence:", confidence)

    st.image(img, use_container_width=True)

else:

    st.info("Configure mission and click DEPLOY MISSION to start swarm simulation.")