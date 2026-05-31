import random

def edge_analyze(sensor_data):

    battery, signal, cpu, latency = sensor_data

    score = 0

    # BATTERY
    if battery < 40:
        score += 2
    elif battery < 70:
        score += 1

    # SIGNAL
    if signal < 40:
        score += 2
    elif signal < 70:
        score += 1

    # CPU
    if cpu > 85:
        score += 2
    elif cpu > 60:
        score += 1

    # LATENCY
    if latency > 12:
        score += 2
    elif latency > 7:
        score += 1

    # FINAL STATUS
    if score <= 2:
        return "SAFE"

    elif score <= 5:
        return "WARNING"

    else:
        return "CRITICAL"