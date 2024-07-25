import asyncio
import random
from typing import Dict, List, Any, Optional, Union, Callable
from dataclasses import dataclass, field
from abc import ABC, abstractmethod
import logging
import json
from datetime import datetime
import aiohttp
import numpy as np
from scipy import stats
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@dataclass
class Sensor:
    id: str
    type: str
    value: Any
    unit: str
    min_value: float
    max_value: float
    accuracy: float = 0.1
    last_calibration: datetime = field(default_factory=datetime.now)
    calibration_interval: int = 30  # days
    failure_probability: float = 0.001
    data_source: Optional[Callable] = None

    def to_dict(self):
        return {
            "id": self.id,
            "type": self.type,
            "value": self.value,
            "unit": self.unit,
            "min_value": self.min_value,
            "max_value": self.max_value,
            "accuracy": self.accuracy,
            "last_calibration": self.last_calibration.isoformat(),
            "calibration_interval": self.calibration_interval,
            "failure_probability": self.failure_probability
        }

    def needs_calibration(self) -> bool:
        return (datetime.now() - self.last_calibration).days >= self.calibration_interval

    def is_failed(self) -> bool:
        return random.random() < self.failure_probability

@dataclass
class Actuator:
    id: str
    type: str
    state: Any
    possible_states: List[Any] = field(default_factory=list)
    energy_consumption: float = 0.0
    last_maintenance: datetime = field(default_factory=datetime.now)
    maintenance_interval: int = 90  # days
    failure_probability: float = 0.0005

    def to_dict(self):
        return {
            "id": self.id,
            "type": self.type,
            "state": self.state,
            "possible_states": self.possible_states,
            "energy_consumption": self.energy_consumption,
            "last_maintenance": self.last_maintenance.isoformat(),
            "maintenance_interval": self.maintenance_interval,
            "failure_probability": self.failure_probability
        }

    def needs_maintenance(self) -> bool:
        return (datetime.now() - self.last_maintenance).days >= self.maintenance_interval

    def is_failed(self) -> bool:
        return random.random() < self.failure_probability

class DigitalTwin(ABC):
    def __init__(self, id: str):
        self.id = id
        self.sensors: Dict[str, Sensor] = {}
        self.actuators: Dict[str, Actuator] = {}
        self.state: Dict[str, Any] = {}
        self.history: List[Dict[str, Any]] = []
        self.alerts: List[str] = []
        self.last_update: Optional[datetime] = None
        self.anomaly_detector = AnomalyDetector()
        self.predictive_maintenance = PredictiveMaintenance()
        self.optimization_engine = OptimizationEngine()

    def add_sensor(self, sensor: Sensor):
        self.sensors[sensor.id] = sensor
        logger.info(f"Added sensor {sensor.id} to {self.id}")

    def add_actuator(self, actuator: Actuator):
        self.actuators[actuator.id] = actuator
        logger.info(f"Added actuator {actuator.id} to {self.id}")

    @abstractmethod
    async def update_state(self):
        pass

    @abstractmethod
    async def process_data(self):
        pass

    @abstractmethod
    async def control_actuators(self):
        pass

    async def run(self):
        logger.info(f"Starting {self.__class__.__name__} {self.id}")
        while True:
            try:
                await self.update_state()
                await self.process_data()
                await self.control_actuators()
                self.history.append(self.state.copy())
                if len(self.history) > 10000:  # Keep last 10000 states
                    self.history.pop(0)
                self.last_update = datetime.now()
                await self.save_state()
                await self.detect_anomalies()
                await self.perform_predictive_maintenance()
                await self.optimize_performance()
                await asyncio.sleep(1)  # Adjust the interval as needed
            except Exception as e:
                logger.error(f"Error in {self.__class__.__name__} {self.id}: {str(e)}")
                self.alerts.append(f"Error: {str(e)}")
                await asyncio.sleep(5)  # Wait before retrying

    async def save_state(self):
        state_to_save = {
            "id": self.id,
            "timestamp": self.last_update.isoformat(),
            "sensors": {sensor_id: sensor.to_dict() for sensor_id, sensor in self.sensors.items()},
            "actuators": {actuator_id: actuator.to_dict() for actuator_id, actuator in self.actuators.items()},
            "state": self.state,
            "alerts": self.alerts
        }
        with open(f"{self.id}_state.json", "w") as f:
            json.dump(state_to_save, f, indent=2)

    async def detect_anomalies(self):
        anomalies = self.anomaly_detector.detect(self.state, self.history)
        for anomaly in anomalies:
            self.alerts.append(f"Anomaly detected: {anomaly}")

    async def perform_predictive_maintenance(self):
        maintenance_actions = self.predictive_maintenance.predict(self.state, self.history)
        for action in maintenance_actions:
            self.alerts.append(f"Maintenance required: {action}")

    async def optimize_performance(self):
        optimizations = self.optimization_engine.optimize(self.state, self.actuators)
        for optimization in optimizations:
            self.alerts.append(f"Optimization suggestion: {optimization}")

class SensorDataProcessor:
    @staticmethod
    async def process(sensor_data: Dict[str, Any]) -> Dict[str, Any]:
        processed_data = {}
        for sensor_id, value in sensor_data.items():
            if sensor_id == 'history':
                continue
            # Simple moving average
            processed_data[f"{sensor_id}_avg"] = sum(
                history[sensor_id] for history in sensor_data.get('history', [])[-10:]
            ) / min(10, len(sensor_data.get('history', [])))
            # Exponential moving average
            processed_data[f"{sensor_id}_ema"] = SensorDataProcessor._calculate_ema(
                [history[sensor_id] for history in sensor_data.get('history', [])], span=10
            )
            # Rate of change
            if len(sensor_data.get('history', [])) >= 2:
                processed_data[f"{sensor_id}_rate"] = (
                    sensor_data['history'][-1][sensor_id] - sensor_data['history'][-2][sensor_id]
                )
            # Standard deviation
            processed_data[f"{sensor_id}_std"] = np.std([history[sensor_id] for history in sensor_data.get('history', [])])
        return processed_data

    @staticmethod
    def _calculate_ema(data, span):
        return pd.Series(data).ewm(span=span).mean().iloc[-1]

class ActuatorController:
    @staticmethod
    async def control(actuators: Dict[str, Actuator], state: Dict[str, Any]) -> List[str]:
        actions = []
        for actuator_id, actuator in actuators.items():
            if actuator.is_failed():
                actions.append(f"Actuator {actuator_id} has failed and needs immediate maintenance")
                continue

            if actuator.type == "HVAC":
                new_state = ActuatorController._control_hvac(state)
            elif actuator.type == "motor":
                new_state = ActuatorController._control_motor(state)
            else:
                logger.warning(f"Unknown actuator type: {actuator.type}")
                continue

            if new_state != actuator.state:
                actuator.state = new_state
                actions.append(f"Actuator {actuator_id} state changed to {actuator.state}")
                logger.info(f"Actuator {actuator_id} state set to {actuator.state}")

            if actuator.needs_maintenance():
                actions.append(f"Actuator {actuator_id} needs scheduled maintenance")

        return actions

    @staticmethod
    def _control_hvac(state: Dict[str, Any]) -> str:
        temp_avg = state.get("temp1_avg", 0)
        if temp_avg > 25:
            return "cooling"
        elif temp_avg < 18:
            return "heating"
        else:
            return "off"

    @staticmethod
    def _control_motor(state: Dict[str, Any]) -> str:
        current_speed = state.get("speed1", 0)
        target_speed = state.get("target_speed", 1000)
        if current_speed < target_speed * 0.9:
            return "accelerating"
        elif current_speed > target_speed * 1.1:
            return "decelerating"
        else:
            return "steady"

class DigitalTwinFactory:
    @staticmethod
    def create_digital_twin(twin_type: str, id: str) -> DigitalTwin:
        if twin_type == "SmartBuilding":
            return SmartBuildingDigitalTwin(id)
        elif twin_type == "IndustrialMachine":
            return IndustrialMachineDigitalTwin(id)
        else:
            raise ValueError(f"Unknown digital twin type: {twin_type}")

class SmartBuildingDigitalTwin(DigitalTwin):
    async def update_state(self):
        for sensor in self.sensors.values():
            if sensor.is_failed():
                self.alerts.append(f"Sensor {sensor.id} has failed and needs replacement")
                continue
            if sensor.needs_calibration():
                self.alerts.append(f"Sensor {sensor.id} needs calibration")
            sensor.value = await self.simulate_sensor_reading(sensor)
        self.state = {sensor.id: sensor.value for sensor in self.sensors.values()}
        self.state['history'] = self.history

    async def process_data(self):
        processed_data = await SensorDataProcessor.process(self.state)
        self.state.update(processed_data)
        await self.check_alerts()

    async def control_actuators(self):
        actions = await ActuatorController.control(self.actuators, self.state)
        self.alerts.extend(actions)

    async def simulate_sensor_reading(self, sensor: Sensor) -> float:
        if sensor.data_source:
            return await sensor.data_source()
        base_value = random.uniform(sensor.min_value, sensor.max_value)
        noise = random.uniform(-sensor.accuracy, sensor.accuracy)
        return round(base_value + noise, 2)

    async def check_alerts(self):
        if self.state.get("temp1_avg", 0) > 30:
            self.alerts.append(f"High temperature alert: {self.state['temp1_avg']}°C")
        if self.state.get("humid1_avg", 0) > 65:
            self.alerts.append(f"High humidity alert: {self.state['humid1_avg']}%")

class IndustrialMachineDigitalTwin(DigitalTwin):
    async def update_state(self):
        for sensor in self.sensors.values():
            if sensor.is_failed():
                self.alerts.append(f"Sensor {sensor.id} has failed and needs replacement")
                continue
            if sensor.needs_calibration():
                self.alerts.append(f"Sensor {sensor.id} needs calibration")
            sensor.value = await self.simulate_sensor_reading(sensor)
        self.state = {sensor.id: sensor.value for sensor in self.sensors.values()}
        self.state['history'] = self.history

    async def process_data(self):
        processed_data = await SensorDataProcessor.process(self.state)
        self.state.update(processed_data)
        await self.check_alerts()

    async def control_actuators(self):
        actions = await ActuatorController.control(self.actuators, self.state)
        self.alerts.extend(actions)

    async def simulate_sensor_reading(self, sensor: Sensor) -> Union[float, int]:
        if sensor.data_source:
            return await sensor.data_source()
        base_value = random.uniform(sensor.min_value, sensor.max_value)
        noise = random.uniform(-sensor.accuracy, sensor.accuracy)
        if sensor.type == "rotational_speed":
            return int(base_value + noise)
        return round(base_value + noise, 2)

    async def check_alerts(self):
        if self.state.get("speed1_avg", 0) > 4500:
            self.alerts.append(f"High speed alert: {self.state['speed1_avg']} RPM")
        if self.state.get("temp1_avg", 0) > 75:
            self.alerts.append(f"High temperature alert: {self.state['temp1_avg']}°C")

class AnomalyDetector:
    def __init__(self):
        self.scaler = StandardScaler()
        self.pca = PCA(n_components=2)
        self.kmeans = KMeans(n_clusters=2)

    def detect(self, current_state: Dict[str, Any], history: List[Dict[str, Any]]) -> List[str]:
        if len(history) < 100:  # Need enough data for meaningful analysis
            return []

        df = pd.DataFrame(history)
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        X = df[numeric_cols]

        X_scaled = self.scaler.fit_transform(X)
        X_pca = self.pca.fit_transform(X_scaled)
        labels = self.kmeans.fit_predict(X_pca)

        anomalies = []
        current_point = np.array([current_state[col] for col in numeric_cols]).reshape(1, -1)
        current_point_scaled = self.scaler.transform(current_point)
        current_point_pca = self.pca.transform(current_point_scaled)
        current_label = self.kmeans.predict(current_point_pca)

        if current_label != labels[-1]:
            anomalies.append("Sudden change in system behavior detected")

        # Check for values outside of 3 standard deviations
        for col in numeric_cols:
            mean = df[col].mean()
            std = df[col].std()
            if abs(current_state[col] - mean) > 3 * std:
                anomalies.append(f"Anomaly detected in {col}: value {current_state[col]} is outside of 3 standard deviations")

        return anomalies

class PredictiveMaintenance:
    def predict(self, current_state: Dict[str, Any], history: List[Dict[str, Any]]) -> List[str]:
        maintenance_actions = []

        if len(history) < 100:  # Need enough data for meaningful analysis
            return maintenance_actions

async def main():
    # Example usage
    building_twin = DigitalTwinFactory.create_digital_twin("SmartBuilding", "Building1")
    building_twin.add_sensor(Sensor("temp1", "temperature", 0, "°C", 15, 35))
    building_twin.add_sensor(Sensor("humid1", "humidity", 0, "%", 30, 70))
    building_twin.add_actuator(Actuator("hvac1", "HVAC", "off", ["off", "cooling", "heating"]))

    machine_twin = DigitalTwinFactory.create_digital_twin("IndustrialMachine", "Machine1")
    machine_twin.add_sensor(Sensor("speed1", "rotational_speed", 0, "RPM", 0, 5000))
    machine_twin.add_sensor(Sensor("temp1", "temperature", 0, "°C", 20, 80))
    machine_twin.add_actuator(Actuator("motor1", "motor", "off", ["off", "accelerating", "decelerating", "steady"]))

    await asyncio.gather(
        building_twin.run(),
        machine_twin.run()
    )

if __name__ == "__main__":
    asyncio.run(main())
