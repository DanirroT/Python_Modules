#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional, Tuple, Union  # noqa: F401


class DataStream(ABC):

    name: str
    stream_id: str
    data_type: str
    data: Any

    def __init__(self, name: str, stream_id: str, data_type: str, data: Any
                 ) -> None:
        self.name = name
        self.stream_id = stream_id
        self.data_type = data_type
        self.data = data

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        print("Batch 1 Results:")
        return "123"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        output_list: List[Any] = []
        for data in data_batch:
            if criteria in str(data):
                output_list.append(data)
        return data

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        data_processed = 0
        output_dict: dict[str, Union[str, int, float]] = {}
        for data in self.data:
            if (isinstance(data, list) and
                    isinstance(data[0], int) or isinstance(data[0], float)):
                data_num = len(data)
                data_sum = sum(data)
                data_avg = data_sum / data_num
                output_dict["sum"] = data_sum
                output_dict["num"] = data_num
                output_dict["avg"] = data_avg
            if isinstance(data, str):
                data_num = len(data)
                output_dict["sum"] = data_sum

            data_processed += 1
        return output_dict


class SensorStream(DataStream):

    def __init__(self, name: str, stream_id: str, data_type: str, data: str
                 ) -> None:
        super().__init__(name, stream_id, data_type, data)

    def process_batch(self, data_batch: List[Any]) -> str:
        print("Batch 1 Results:")
        return "123"

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

        print("Processing sensor batch:", self.data)
        data_processed = 0
        output_dict: dict[str, Union[str, int, float]] = {}
        for data in self.data:
            if (isinstance(data, list) and
                    isinstance(data[0], int) or isinstance(data[0], float)):
                data_num = len(data)
                data_sum = sum(data)
                data_avg = data_sum / data_num
                print("stats:", data_num, data_sum, data_avg)
                output_dict["sum"] = data_sum
                output_dict["num"] = data_num
                output_dict["avg"] = data_avg
            if isinstance(data, str):
                data_num = len(data)
                print("stats:", data_num)
                output_dict["sum"] = data_num

            data_processed += 1
        return output_dict


def data_stream() -> None:

    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    print()

    print("Initializing Sensor Stream...")

    Sensor = SensorStream("Sensor", "SENSOR_001", "Environmental Data",
                          "[temp:22.5, humidity:65, pressure:1013]")

    Sensor.get_stats()

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
