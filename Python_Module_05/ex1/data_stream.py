#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional, Type, Union  # noqa: F401


class DataType(ABC):
    pass


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

    label: str
    value: Union[int, float]

    def __init__(self, label, value) -> None:
        self.label = label
        self.value = value


class SensorStream(DataStream):

    def __init__(self, name: str, stream_id: str, data_type: str) -> None:
        super().__init__(name, stream_id, data_type)

    def process_batch(self, data_batch: List[SensorType]) -> str:

        formatted_input = ", ".join(f"{data.label}:{data.value}"
                                    for data in data_batch)

        print(f"Stream ID: {self.stream_id}, Type: {self.data_type}")

        print(f"Processing sensor batch: [{formatted_input}]")

        data_dict: dict[str, list[int | float]] = {}
        for data_point in data_batch:

            if not data_point.label or data_point.label == "":
                raise ValueError("Stream value name cannot be empty.")
            if isinstance(data_point.value, (int, float)):
                val = data_point.value
            else:
                try:
                    val = float(data_point.value)
                except (ValueError):
                    raise ValueError("Stream value must be numeric.")

            if data_point.label not in data_dict:
                data_dict[data_point.label] = []
            data_dict[data_point.label].append(val)

        self.data = data_dict

        stats = self.get_stats()

        output_std = f"Sensor analysis: {len(data_batch)} readings processed"

        output_extra = None
        unit = ""
        lookup_stat = "avg"
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

    def get_stats(self) -> dict[str, str | int | float]:

        data_processed = 0
        output_dict: dict[str, Union[int, float]] = {}
        for data_name, data in self.data.items():
            data_num = len(data)
            data_sum = sum(data)
            data_avg = data_sum / data_num

            output_dict[data_name + "_num"] = data_num
            output_dict[data_name + "_sum"] = data_sum
            output_dict[data_name + "_avg"] = data_avg

            data_processed += 1
        output_dict["processed"] = data_processed

        return output_dict

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

    label: str
    value: Union[int, float]

    def __init__(self, label, value) -> None:
        self.label = label
        self.value = value


class TransactionStream(DataStream):

    def __init__(self, name: str, stream_id: str, data_type: str) -> None:
        super().__init__(name, stream_id, data_type)

    def process_batch(self, data_batch: List[TransactionType]
                      ) -> str:

        formatted_input = ", ".join(f"{data.label}:{data.value}"
                                    for data in data_batch)

        print(f"Stream ID: {self.stream_id}, Type: {self.data_type}")

        print(f"Processing transaction batch: [{formatted_input}]")

        data_dict: dict[str, list[int | float]] = {}
        for data_point in data_batch:

            if not data_point.label or data_point.label == "":
                raise ValueError("Stream value name cannot be empty.")
            if isinstance(data_point.value, (int, float)):
                val = data_point.value
            else:
                try:
                    val = float(data_point.value)
                except (ValueError):
                    raise ValueError("Stream value must be numeric.")

            if data_point.label not in data_dict:
                data_dict[data_point.label] = []
            data_dict[data_point.label].append(val)

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


class EventType(DataType):

    event: str

    def __init__(self, event) -> None:
        self.event = event


class EventStream(DataStream):

    def __init__(self, name: str, stream_id: str, data_type: str) -> None:
        super().__init__(name, stream_id, data_type)

    def process_batch(self, data_batch: List[EventType]) -> str:

        formatted_input = ", ".join(data.event for data in data_batch)

        print(f"Stream ID: {self.stream_id}, Type: {self.data_type}")

        print(f"Processing event batch: [{formatted_input}]")

        data_list: list[str] = []
        for data_point in data_batch:

            if not data_point.event or data_point.event == "":
                raise ValueError("Stream value cannot be empty.")
            if isinstance(data_point.event, str):
                val = data_point.event
            else:
                try:
                    val = str(data_point.event)
                except ValueError:
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

    @classmethod
    def get_class_name(cls) -> str:
        return cls.__name__


class OtherType(DataType):

    other: str

    def __init__(self, other) -> None:
        self.other = other


class StreamProcessor():

    name: str
    batch_num: int
    stream_list: dict[Type, Type]

    def __init__(self, name: str) -> None:

        if not name or name == "":
            raise ValueError("Stream name cannot be empty.")
        self.name = name

        self.batch_num = 0
        self.stream_list = {SensorStream: SensorType,
                            TransactionStream: TransactionType,
                            EventStream: EventType}

    def process_all_batches(self, batches: List[DataType]) -> str:

        # print(batches)
        # print()
        # print(self.stream_list)
        # print()

        self.batch_num += 1
        return_string = f"Batch {self.batch_num} Results:"

        processed_dict: dict[str, int] = {stream_type.__name__: 0
                                          for stream_type in self.stream_list}
        processed_dict["Other"] = 0

        # print("processed_dict", processed_dict)
        # print()

        for data in batches:
            # print("data", data.__class__.__name__)
            found = False
            for data_stream, data_types in self.stream_list.items():
                # print(
                # "\tstream_type", data_stream.__name__, data_types.__name__)
                if data.__class__ == data_types:
                    found = True
                    processed_dict[data_stream.__name__] += 1
                    
                    break
            if not found:
                processed_dict["Other"] += 1

        if processed_dict["SensorStream"]:
            return_string += (
                f"\n- Sensor data: {processed_dict["SensorStream"]}"
                " readings processed")
        if processed_dict["TransactionStream"]:
            return_string += (
                f"\n- Transaction data: {processed_dict["TransactionStream"]}"
                " operations processed")
        if processed_dict["EventStream"]:
            return_string += (
                f"\n- Event data: {processed_dict["EventStream"]}"
                " events processed")

        # print("processed_dict", processed_dict)

        return_string += "\nStream filtering active: High-priority data only\n"

        filtered_results: dict[str, int] = {
            stream_type.__name__: 0 for stream_type in self.stream_list}
        filtered_results["Other"] = 0

        if sum(filtered_results.values()):
            return_string += "Filtered results:"
            if filtered_results["SensorStream"]:
                return_string += (f"{filtered_results["SensorStream"]}"
                                  " critical sensor alerts")
            if filtered_results["TransactionStream"]:
                return_string += (f"{filtered_results["TransactionStream"]}"
                                  " large transaction")
            if filtered_results["EventStream"]:
                return_string += (f"{filtered_results["EventStream"]}"
                                  " errors detected")
        else:
            return_string += "No High-priority data"

        return return_string


def data_stream() -> None:

    # print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    # print()
    # print("Initializing Sensor Stream...")

    # Sensor = SensorStream("Sensor", "SENSOR_001", "Environmental Data")

    # print(Sensor.process_batch([
    #     SensorType("temp", 22.5),  # °C
    #     SensorType("humidity", 65),  # %
    #     SensorType("pressure", 1013)  # hPa
    # ]))

    # print()

    # print("Initializing Transaction Stream...")

    # Transaction = TransactionStream("Transaction", "TRANS_001",
    #                                 "Financial Data")

    # print(Transaction.process_batch([
    #     TransactionType("buy", 100),
    #     TransactionType("sell", 150),
    #     TransactionType("buy", 75)
    # ]))

    # print()

    # print("Initializing Event Stream...")

    # Event = EventStream("Event", "EVENT_001", "System Events")

    # print(Event.process_batch([
    #     EventType("login"),
    #     EventType("error"),
    #     EventType("logout")
    # ]))

    print()

    print("=== Polymorphic Stream Processing ===")

    print("Processing mixed stream types through unified interface...")

    print()

    poly_stream = StreamProcessor("Poly")

    print(poly_stream.process_all_batches([
        EventType("login"),
        SensorType("temp", 42.5),
        TransactionType("buy", 100),
        TransactionType("sell", 150),
        TransactionType("buy", 75),
        EventType("error"),
        TransactionType("sell", 1500),
        SensorType("humidity", 95),
        EventType("logout"),
        OtherType("other")
    ]))

    print()

    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    data_stream()
