import socket
import json
from datetime import datetime

def save_data(sensordata):
    date = datetime.now().strftime("%Y-%m-%d")
    for sensor,value in sensordata.items():
        if sensor != "Timestamp":
            filename = f"{sensor}_{date}.json"
            try:
                with open(filename, "r") as f:
                    existing_data = json.load(f)
            except:
                existing_data = []
            dataupdate = {sensor:value, "Timestamp":sensordata["Timestamp"]}
            existing_data.append(dataupdate)
            with open(filename, "w") as f:
                json.dump(existing_data, f)

HOST = "127.0.0.1"
PORT = 65432
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        elif data:
            sensor_data = json.loads(data)
            save_data(sensor_data)


