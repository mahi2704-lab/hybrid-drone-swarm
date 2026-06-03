import streamlit as st
import requests
import time
import pandas as pd
import pydeck as pdk
import random

st.set_page_config(
    page_title="Hybrid Edge-Cloud Digital Twin Drone Swarm",
    layout="wide"
)

st.title("Hybrid Edge-Cloud Digital Twin Drone Swarm")
st.subheader("Industry-Level Monitoring Dashboard")

history = {

    "battery": [],

    "signal": [],

    "cpu": [],

    "latency": [],

    "anomaly": []
}

placeholder = st.empty()

while True:

    response = requests.get(
        "http://backend:8000/drone-status"
    )

    data = response.json()

    # STORE HISTORY
    history["battery"].append(data["battery_level"])

    history["signal"].append(data["signal_strength"])

    history["cpu"].append(data["cpu_usage"])

    history["latency"].append(data["edge_latency"])

    history["anomaly"].append(data["anomaly_score"])

    # KEEP LAST 25 VALUES
    for key in history:

        if len(history[key]) > 25:

            history[key].pop(0)

    with placeholder.container():

        # TOP METRICS
        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Active Drones",
            data["active_drones"]
        )

        col2.metric(
            "Battery",
            f'{data["battery_level"]}%'
        )

        col3.metric(
            "Signal",
            f'{data["signal_strength"]}%'
        )

        col4, col5, col6 = st.columns(3)

        col4.metric(
            "CPU Usage",
            f'{data["cpu_usage"]}%'
        )

        col5.metric(
            "Edge Latency",
            f'{data["edge_latency"]} ms'
        )

        col6.metric(
            "AI Anomaly Score",
            data["anomaly_score"]
        )

        # EDGE STATUS
        if data["edge_status"] == "SAFE":

            st.success(
                f'Edge Status: {data["edge_status"]}'
            )

        elif data["edge_status"] == "WARNING":

            st.warning(
                f'Edge Status: {data["edge_status"]}'
            )

        else:

            st.error(
                f'Edge Status: {data["edge_status"]}'
            )

        # SYSTEM STATUS
        if data["status"] == "OPERATIONAL":

            st.success(
                f'System Status: {data["status"]}'
            )

        elif data["status"] == "WARNING":

            st.warning(
                f'System Status: {data["status"]}'
            )

        else:

            st.error(
                f'System Status: {data["status"]}'
            )

        # CHARTS
        st.markdown("## Real-Time Drone Telemetry")

        df = pd.DataFrame({

            "Battery": history["battery"],

            "Signal": history["signal"],

            "CPU": history["cpu"],

            "Latency": history["latency"],

            "AI Score": history["anomaly"]
        })

        st.line_chart(df)

        # DYNAMIC DRONE MAP
        st.markdown("## Drone Swarm Map")

        num_drones = data["active_drones"]

        drone_data = []

        for i in range(num_drones):

            drone_data.append({

                "lat": 13.0827 + random.uniform(-0.05, 0.05),

                "lon": 80.2707 + random.uniform(-0.05, 0.05),

                "drone_id": f"Drone {i+1}"
            })

        drone_positions = pd.DataFrame(drone_data)

        layer = pdk.Layer(

            "ScatterplotLayer",

            data=drone_positions,

            get_position=["lon", "lat"],

            get_color=[255, 0, 0, 180],

            get_radius=250,

            pickable=True
        )

        view_state = pdk.ViewState(

            latitude=13.0827,

            longitude=80.2707,

            zoom=10
        )

        tooltip = {

            "html": "<b>{drone_id}</b>",

            "style": {

                "backgroundColor": "black",

                "color": "white"
            }
        }

        st.pydeck_chart(

            pdk.Deck(

                layers=[layer],

                initial_view_state=view_state,

                tooltip=tooltip
            )
        )

        # BLOCKCHAIN INFO
        st.markdown("## Blockchain Secured Event Hash")

        st.code(data["block_hash"])

        st.markdown("## Last Updated")

        st.write(data["timestamp"])

    time.sleep(2)