#  IoT Data Processing System

An educational IoT data processing pipeline built using **Python**, featuring simulated sensors, a gateway communicating via **MQTT** and storing data in **MongoDB**, and a processor to handle real-time analytics or operations.

---

##  Features

-  Simulated Sensor Data Generator
-  Gateway for handling MQTT & MongoDB communication
-  Real-time Data Processing Module
-  Modular design for scalability
-  MongoDB integration for data storage
-  Pure Python implementation

---

##  Project Structure

```
IOT-master/
│
├── main.py                        # Entry point to start the whole system
│
├── sensor/
│   ├── sensor.py                 # Sensor logic
│   └── data_simulator.py         # Simulates sensor data
│
├── gateway/
│   ├── mqtt/client.py            # MQTT client setup and data transmission
│   └── mongo/client.py           # MongoDB client and data storage logic
│
├── processor/
│   └── processor.py              # Processes incoming sensor data
│
├── .gitignore                    # Standard Git ignore file
└── README.md                     # Project documentation (this file)
```

---

##  How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/IOT-master.git
   cd IOT-master
   ```

2. **Install required Python packages:**
   ```bash
   pip install paho-mqtt pymongo
   ```

3. **Make sure MongoDB is running** locally or provide connection details in `gateway/mongo/client.py`.

4. **Run the system:**
   ```bash
   python main.py
   ```

This will launch the sensors, gateway, and processor as a simple simulation pipeline.

---

## Requirements

- Python 3.x
- MongoDB (local or cloud instance)
- MQTT Broker (e.g., Mosquitto — optional if testing locally)

---

##  Test & Extend

- Try modifying `data_simulator.py` to change the format or frequency of sensor data.
- Plug in real MQTT brokers or MongoDB Atlas for live demos.
- Expand `processor.py` to perform analytics, filtering, or alerting logic.

---

##  Developer

IoT Data Simulation & Processing Project  
Developed by: **Niloufar Cheraghi**


