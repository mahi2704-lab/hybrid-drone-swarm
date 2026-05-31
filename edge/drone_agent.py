import random

class DroneAgent:
    def __init__(self, drone_id):
        self.drone_id = drone_id

    def sense(self):
        """
        Simulate thermal sensor (Edge sensing)
        """
        return random.uniform(30.0, 40.0)

    def ai_inference(self, temperature):
        """
        Lightweight AI-based inference (Explainable Edge AI)
        Returns probability and decision
        """
        # Normalize temperature to probability (mock AI logic)
        probability = min(max((temperature - 30) / 10, 0), 1)

        survivor_detected = probability > 0.6

        explanation = (
            "High thermal anomaly detected"
            if survivor_detected
            else "Thermal reading within normal range"
        )

        return survivor_detected, round(probability, 2), explanation

    def act(self):
        """
        Edge decision-making
        """
        temperature = self.sense()
        detected, confidence, reason = self.ai_inference(temperature)

        print(
            f"[EDGE AI] Drone {self.drone_id} | "
            f"Temp: {temperature:.2f}°C | "
            f"Survivor: {detected} | "
            f"Confidence: {confidence} | "
            f"Reason: {reason}"
        )

        # Return structured data for cloud & blockchain
        return {
            "id": self.drone_id,
            "temperature": round(temperature, 2),
            "survivor_detected": detected,
            "confidence": confidence,
            "reason": reason
        }
