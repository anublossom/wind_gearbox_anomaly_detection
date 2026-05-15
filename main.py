from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from simulation import GearboxSimulator
import threading
import time

app = FastAPI()
sim = GearboxSimulator()

# Configures CORS so your local HTML file can talk to the API safely
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

database_telemetry_historian = []

def industrial_data_collector():
    while True:
        data_packet = sim.generate_telemetry()
        data_packet["timestamp"] = time.strftime("%H:%M:%S")
        
        database_telemetry_historian.append(data_packet)
        if len(database_telemetry_historian) > 20:
            database_telemetry_historian.pop(0)
            
        time.sleep(1.5) 

# Spins up the background collection thread immediately on launch
threading.Thread(target=industrial_data_collector, daemon=True).start()

@app.get("/api/telemetry")
def get_live_telemetry():
    return database_telemetry_historian
