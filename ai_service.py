import random


def predict_anomaly(sensor_data):

    battery, signal, cpu, latency = sensor_data

    anomaly_score = (
        (100 - battery) * 0.3 +
        (100 - signal) * 0.2 +
        cpu * 0.3 +
        latency * 5 * 0.2
    ) / 100

    anomaly_score += random.uniform(-0.1, 0.1)

    anomaly_score = max(0, min(anomaly_score, 1))

    return round(anomaly_score, 2)