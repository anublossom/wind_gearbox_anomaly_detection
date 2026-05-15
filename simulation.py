import math
import random

class GearboxSimulator:
    def __init__(self):
        self.base_temp = 60.0  
        self.time_step = 0

    def generate_telemetry(self):
        self.time_step += 1
        
        # Replicates MATLAB sine wave modeling for wind fluctuations
        wind_fluctuation = math.sin(self.time_step * 0.1) * 2.0
        rpm = max(10.0, 14.0 + wind_fluctuation + random.uniform(-0.5, 0.5))
        
        # Simulates thermodynamics: frictional heat generation
        friction_heat = (rpm - 12.0) * 1.5
        temperature = self.base_temp + friction_heat + random.uniform(-0.2, 0.2)
        
        # Contextual Anomaly injection (5% probability)
        is_anomaly = False
        if random.random() < 0.05:  
            temperature += random.uniform(15.0, 25.0)
            is_anomaly = True

        return {
            "turbine_id": "WTG-ZF-01",
            "rotor_speed_rpm": round(rpm, 2),
            "gearbox_oil_temp_c": round(temperature, 2),
            "anomaly_detected": is_anomaly
        }
