#!/usr/bin/env python3

from typing import List, Dict, Any, Optional, Tuple, Union  # noqa: F401


class SensorStream():

    name: str
    stream_id: str
    data_type: str
    raw_data: str
    processed_data: dict[str, list[Union[int, float]]]

    def __init__(self, name: str, stream_id: str, data_type: str, data_str: str
                 ) -> None:
        
        if not name or name == "":
            raise ValueError("Stream name cannot be empty.")
        self.name = name
        self.stream_id = stream_id
        self.data_type = data_type
        self.raw_data = data_str
        print("\ngiven data:", self.raw_data)
        print()
        data_list = self.raw_data.strip("[]").split(", ")
        print("Parsed data:", data_list)
        print()
        data_dict: dict[str, list[int | float]] = {}
        for item in data_list:
            val_name, val_str = item.split(":")
            if not val_name or val_name == "":
                raise ValueError("Stream value name cannot be empty.")
            val = float(val_str)
            if val_name not in data_dict:
                data_dict[val_name] = []
            data_dict[val_name].append(val)
        print("Parsed data:", data_dict)
        print()
        self.processed_data = data_dict

    def process_batch(self, data_batch: List[Any]) -> str:
        print("Processing sensor batch:", self.data)

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        output_list: List[Any] = []
        if not criteria:
            return []
        for data in data_batch:
            if criteria in str(data):
                output_list.append(data)
        return output_list

    def get_stats(self) -> Dict[str, Union[str, int, float]]:

        print(f"Stream ID: {self.stream_id}, Type: {self.data_type}")

        data_processed = 0
        output_dict: dict[str, Union[str, int, float]] = {}
        for data_name, data in self.processed_data.items():
            data_num = len(data)
            data_sum = sum(data)
            data_avg = data_sum / data_num

            print("stats:", data_num, data_sum, data_avg)

            output_dict[data_name + "_sum"] = data_sum
            output_dict[data_name + "_num"] = data_num
            output_dict[data_name + "_avg"] = data_avg

            data_processed += 1
        return output_dict


def data_stream() -> None:

    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    print()

    print("Initializing Sensor Stream...")

    Sensor = SensorStream("Sensor", "SENSOR_001", "Environmental Data",
                          "[temp:22.5, temp:2.5, humidity:65, pressure:1013]")

    Sensor.get_stats()

    Sensor.filter_data(Sensor.processed_data, "temp_avg")

    # print()

    # print("Initializing Sensor Stream...")

    # Sensor = StreamProcessor("Transaction", "TRANS_001", "Financial Data",
    #                          {"buy": 100, "sell": 150, "buy": 75})

    # Sensor.get_stats()

    # print()

    # print("Initializing Sensor Stream...")

    # Sensor = StreamProcessor("Event", "EVENT_001", "System Events",
    #                          {"login", "error", "logout"})

    # Sensor.get_stats()

    # print()

    print()

    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    data_stream()


Your Mission: Create a sophisticated data streaming system that demonstrates advanced polymorphic behavior. Build stream handlers that can process mixed data types while maintaining type-specific optimizations.
Advanced Architecture:
• Stream Base: DataStream - an abstract base class with core streaming functionality
• Specialized Streams: SensorStream(stream_id), TransactionStream(stream_id), EventStream(stream_id)
• Required Methods (must be implemented in DataStream and overridden in subclasses):
    ◦ process_batch(self, data_batch: List[Any]) -> str - Process a batch of data
    ◦ filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any] - Filter data based on criteria
    ◦ get_stats(self) -> Dict[str, Union[str, int, float]] - Return stream
statistics
• Stream Manager: StreamProcessor that handles multiple stream types polymorphically
• Advanced Features: Batch processing, filtering, transformation pipelines

Required Implementation:
• Create a DataStream abstract base class with process_batch() as an abstract method
• Provide default implementations for filter_data() and get_stats() that can be overridden
• Implement specialized stream classes with overridden behavior for different data domains
• Build a StreamProcessor that can handle any stream type through polymorphism
• Demonstrate batch processing of mixed stream types
• Include stream filtering and transformation capabilities
• Add comprehensive error handling for stream processing failures


This exercise demonstrates subtype polymorphism in action. Your StreamProcessor should be able to handle any DataStream subtype without knowing the specific implementation details. This is the power of polymorphic design!



Example:

$> python3 data_stream.py
=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===

Initializing Sensor Stream...
Stream ID: SENSOR_001, Type: Environmental Data
Processing sensor batch: [temp:22.5, humidity:65, pressure:1013]
Sensor analysis: 3 readings processed, avg temp: 22.5°C

Initializing Transaction Stream...
Stream ID: TRANS_001, Type: Financial Data
Processing transaction batch: [buy:100, sell:150, buy:75]
Transaction analysis: 3 operations, net flow: +25 units

Initializing Event Stream...
Stream ID: EVENT_001, Type: System Events
Processing event batch: [login, error, logout]
Event analysis: 3 events, 1 error detected

=== Polymorphic Stream Processing ===
Processing mixed stream types through unified interface...

Batch 1 Results:
- Sensor data: 2 readings processed
- Transaction data: 4 operations processed
- Event data: 3 events processed

Stream filtering active: High-priority data only
Filtered results: 2 critical sensor alerts, 1 large transaction

All streams processed successfully. Nexus throughput optimal.