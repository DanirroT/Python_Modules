#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional, Tuple, Union  # noqa: F401

git config --global user.name "Daniel Ribeiro"

class DataType(ABC):
    ...


class DataStream(ABC):

    name: str
    stream_id: str
    data_type: str
    data: Any

    def __init__(self, name: str, stream_id: str, data_type: str) -> None:

        if not name or name == "":
            raise ValueError("Stream name cannot be empty.")
        self.name = name
        if not stream_id or stream_id == "":
            raise ValueError("Stream ID cannot be empty.")
        self.stream_id = stream_id
        if not data_type or data_type == "":
            raise ValueError("Stream Type cannot be empty.")
        self.data_type = data_type

    @abstractmethod
    def process_batch(self, data_batch: List[Any]
                      ) -> str:
        return ""

        """
            if not data_batch:
                raise ValueError("Data batch cannot be empty.")

            if not isinstance(data_batch, list):
                raise ValueError("Data batch must be a list.")

            if not isinstance(data_batch[0], dict):
                formatted_input = ", ".join(f"{key}:{value}"
                                            for dta in data_batch
                                            for key, value in dta.items()
                                            )

            if not isinstance(data_batch[0], list):
                formatted_input = str(data_batch)

            if not isinstance(data_batch[0], (str, int, float)):
                formatted_input = ", ".join(f"{value}"
                                            for dta in data_batch
                                            for value in dta
                                            )

            print(f"Stream ID: {self.stream_id}, Type: {self.data_type}")

            print(f"Processing information batch: [{formatted_input}]")

            data_dict: dict[str, list[int | float]] = {}
            for simple_dict in data_batch:

                val_name, val_str = next(iter(simple_dict.items()))

                if not val_name or val_name == "":
                    raise ValueError("Stream value name cannot be empty.")
                if isinstance(val_str, (int, float)):
                    val = val_str
                else:
                    try:
                        val = float(val_str)
                    except (ValueError):
                        raise ValueError("Stream value must be numeric.")

                if val_name not in data_dict:
                    data_dict[val_name] = []
                data_dict[val_name].append(val)

            self.data = data_dict

            output_std = (f"Stream analysis: {len(data_batch)}"
                        "sets of information processed")

            return output_std
        """

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if not criteria:
            return data_batch
        return [data for data in data_batch if criteria in str(data)]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:

        data_processed = 0
        output_dict: dict[str, Union[str, int, float]] = {}
        for data_name, data in self.data.items():
            data_num = len(data)

            output_dict[data_name + "_num"] = data_num

            data_processed += 1
        output_dict["processed"] = data_processed

        return output_dict


class SensorType(DataType):
    def __init__(self, label, value):
        self._label = label
        self._value = value

    def __str__(self):
        return f"{self._label}:{self._value}"

    def label(self):
        return self._label

    def value(self):
        return self._value

class SensorStream(DataStream):

    dataStrings = []
    data_processed = 0
    stats = {}

    def __init__(self, name: str, stream_id: str, data_type: str) -> None:
        super().__init__(name, stream_id, data_type)

    def process(self, data):
        self.dataStrings.append(str(data))

        self.data_processed += 1

        self.stats[data.label() + "_num"] = self.stats[data.label() + "_num"] + 1 if data.label() + "_num" in self.stats else 1
        self.stats[data.label() + "_sum"] = self.stats[data.label() + "_sum"] + data.value() if data.label() + "_sum" in self.stats else data.value()
        self.stats[data.label() + "_avg"] = self.stats[data.label() + "_sum"] / self.stats[data.label() + "_num"]

    def get_stats(self) -> dict[str, str | int | float]:
        return self.stats

    def process_batch(self, data_batch: List[SensorType]
                      ) -> str:

        for d in data_batch:
            self.process(d)

        print(f"Stream ID: {self.stream_id}, Type: {self.data_type}")

        formatted_input = ", ".join(self.dataStrings)
        print(f"Processing sensor batch: [{formatted_input}]")

        stats = self.get_stats()

        output_std = f"Sensor analysis: {len(self.dataStrings)} readings processed"

        output_extra = None
        unit = ""
        lookup_stat = "num"
        lookup_stat_name = "temp"
        output_data = stats["temp" + "_" + lookup_stat]
        if lookup_stat == "avg":
            unit = self.unit(lookup_stat_name)

        if lookup_stat and lookup_stat_name and output_data:
            output_extra = (f"{lookup_stat} {lookup_stat_name}:"
                            f" {output_data}{unit}")

        return ", ".join(x for x in (output_std, output_extra) if x)

        """
        def filter_data(self, data_batch: List[Any],
                        criteria: Optional[str] = None) -> List[Any]:
            if not criteria:
                return data_batch
            return [data for data in data_batch if criteria in str(data)]
        """

    def unit(self, data_name: str) -> str:

        if data_name == "temp":
            return "°C"
        elif data_name == "humidity":
            return "%"
        elif data_name == "pressure":
            return "hPa"
        else:
            return ""


class TransactionType(DataType):
    def __init__(self, label, value):
        self._label = label
        self._value = value

    def __str__(self):
        return f"{self._label}:{self._value}"

    def label(self):
        return self._label

    def value(self):
        return self._value

class TransactionStream(DataStream):

    def __init__(self, name: str, stream_id: str, data_type: str) -> None:
        super().__init__(name, stream_id, data_type)

    def process_batch(self, data_batch: List[dict[str, Union[int, float]]]
                      ) -> str:

        formatted_input = ", ".join(f"{key}:{value}"
                                    for d in data_batch
                                    for key, value in d.items()
                                    )

        print(f"Stream ID: {self.stream_id}, Type: {self.data_type}")

        print(f"Processing transaction batch: [{formatted_input}]")

        data_dict: dict[str, list[int | float]] = {}
        for simple_dict in data_batch:

            val_name, val_str = next(iter(simple_dict.items()))

            if not val_name or val_name == "":
                raise ValueError("Stream value name cannot be empty.")
            if isinstance(val_str, (int, float)):
                val = val_str
            else:
                try:
                    val = float(val_str)
                except (ValueError):
                    raise ValueError("Stream value must be numeric.")

            if val_name not in data_dict:
                data_dict[val_name] = []
            data_dict[val_name].append(val)

        self.data = data_dict

        stats = self.get_stats()

        output_std = f"Transaction analysis: {len(data_batch)}"

        output_extra = None
        net_flow = stats["net_flow"]
        sign = "+" if (net_flow >= 0) else ""

        if net_flow:
            output_extra = f"net flow: {sign}{net_flow} units"

        return ", ".join(x for x in (output_std, output_extra) if x)

        """
        def filter_data(self, data_batch: List[Any],
                        criteria: Optional[str] = None) -> List[Any]:
            if not criteria:
                return data_batch
            return [data for data in data_batch if criteria in str(data)]
        """

    def get_stats(self) -> dict[str, str | int | float]:

        data_processed = 0
        output_dict: dict[str, Union[int, float]] = {}
        net_flow = 0
        for data_name, data in self.data.items():
            if data_name == "buy":
                net_flow += sum(data)
            elif data_name == "sell":
                net_flow -= sum(data)

            data_num = len(data)
            data_sum = sum(data)
            data_avg = data_sum / data_num

            output_dict[data_name + "_num"] = data_num
            output_dict[data_name + "_sum"] = data_sum
            output_dict[data_name + "_avg"] = data_avg

            data_processed += 1
        output_dict["processed"] = data_processed
        output_dict["net_flow"] = net_flow

        return output_dict


class EventStream(DataStream):

    def __init__(self, name: str, stream_id: str, data_type: str) -> None:
        super().__init__(name, stream_id, data_type)

    def process_batch(self, data_batch: List[str]) -> str:

        formatted_input = ", ".join(dta for dta in data_batch)

        print(f"Stream ID: {self.stream_id}, Type: {self.data_type}")

        print(f"Processing event batch: [{formatted_input}]")

        data_list: list[str] = []
        for inp in data_batch:

            if not inp or inp == "":
                raise ValueError("Stream value cannot be empty.")
            if isinstance(inp, str):
                val = inp
            else:
                try:
                    val = str(inp)
                except (ValueError):
                    raise ValueError("Stream value must be a string.")

            data_list.append(val)

        self.data = data_list

        stats = self.get_stats()

        output_std = f"Event analysis: {len(data_batch)} events"

        output_extra = None
        error_num = stats["error"]
        error_spell = "error" if (error_num == 1) else "errors"

        if error_num:
            output_extra = f"{error_num} {error_spell} detected"

        return ", ".join(x for x in (output_std, output_extra) if x)

        """
        def filter_data(self, data_batch: List[Any],
                        criteria: Optional[str] = None) -> List[Any]:
            if not criteria:
                return data_batch
            return [data for data in data_batch if criteria in str(data)]
        """

    def get_stats(self) -> Dict[str, Union[str, int, float]]:

        data_processed = 0
        output_dict: dict[str, Union[str, int, float]] = {}
        output_dict["error"] = 0
        output_dict["login"] = 0
        output_dict["logout"] = 0
        for message in self.data:
            message_low = message.lower()
            if not output_dict[message_low]:
                output_dict[message_low] = 0
            output_dict[message_low] += 1

            if "error" in message_low and "error" not in message_low:
                output_dict["error"] += 1

            if (("login" in message_low or "logged in" in message_low)
                    and message_low not in ("login", "logged in")):
                output_dict["login"] += 1

            if (("logout" in message_low or "logged out" in message_low)
                    and message_low not in ("logout", "logged out")):
                output_dict["logout"] += 1

            data_processed += 1
        output_dict["processed"] = data_processed

        return output_dict


class StreamProcessor():

    name: str
    stream_list: List[DataStream]

    def __init__(self, name: str, stream_list: List[DataStream]) -> None:

        if not name or name == "":
            raise ValueError("Stream name cannot be empty.")
        self.name = name

        self.stream_list = stream_list

    def add_stream(self, stream: DataStream) -> None:
        self.stream_list.append(stream)

    def process_all_batches(self, batches: List[Any]) -> str:

        num = 1
        return_string = f"Batch {num} Results:"
        processed_data: DataStream
        sensor_processed = 0
        transaction_processed = 0
        event_processed = 0
        if "Sensor analysis" in batches:
            sensor_processed += 1
        if "Transaction analysis" in batches:
            transaction_processed += 1
        if "Event analysis" in batches:
            event_processed += 1

        if sensor_processed:
            return_string += (f"\n- Sensor data: {sensor_processed}"
                              "readings processed")
        if transaction_processed:
            return_string += (f"\n- Transaction data: {transaction_processed}"
                              "operations processed")
        if event_processed:
            return_string += (f"\n- Event data: {event_processed}"
                              "events processed")

        return return_string

    def filter_all(self, criteria: str) -> List[Any]:
        if not criteria:
            return data_batch
        return [data for data in data_batch if criteria in str(data)]


def data_stream() -> None:

    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    print()
    print("Initializing Sensor Stream...")

    Sensor = SensorStream("Sensor", "SENSOR_001", "Environmental Data")

    print(Sensor.process_batch(
        [
            SensorType("temp", 22.5),  # °C
            SensorType("humidity", 65),  # %
            SensorType("pressure", 1013)  # hPa
        ]
    ))
    print()

    """
    print("Initializing Transaction Stream...")

    Transaction = TransactionStream("Transaction", "TRANS_001",
                                    "Financial Data")

    print(Transaction.process_batch([
                               {"buy": 100},
                               {"sell": 150},
                               {"buy": 75}
                               ]))

    print()

    print("Initializing Event Stream...")

    Event = EventStream("Event", "EVENT_001", "System Events")

    print(Event.process_batch(["login", "error", "logout"]))

    print()

    print("=== Polymorphic Stream Processing ===")

    Sensor_to_process = SensorStream("Sensor", "SENSOR_001",
                                     "Environmental Data")

    Sensor_to_process.process_batch([
                               {"temp": 22.5},  # °C
                               {"humidity": 65},  # %
                               {"pressure": 1013}  # hPa
                               ])

    Transaction_to_process = TransactionStream("Transaction", "TRANS_001",
                                               "Financial Data")

    Transaction_to_process.process_batch([
                               {"buy": 100},
                               {"sell": 150},
                               {"buy": 75}
                               ])

    Event_to_process = EventStream("Event", "EVENT_001", "System Events")

    Event_to_process.process_batch(["login", "error", "logout"])

    processor = StreamProcessor()
    processor.process_batch(
      [
        SensorType()
        TransactionType()
        ..
      ]
    )

    processor = StreamProcessor()

    processor.process_batch
    """
    print()

    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    data_stream()
