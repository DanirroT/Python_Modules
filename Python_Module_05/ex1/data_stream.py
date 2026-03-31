#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import List, Dict, Type, Any, Optional, Union


class DataType(ABC):
    pass


class DataStream(ABC):

    name: str
    stream_id: str
    data_type: str
    data: Any

    type_str: str
    name_str: str
    error_msg: str

    def __init__(self, stream_id: str) -> None:

        if not stream_id:
            raise ValueError("Stream ID cannot be empty.")
        self.stream_id = stream_id

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

                if not val_name:
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
        if isinstance(data_batch[0], DataType):
            return ([data for data in data_batch
                    if criteria in str(data.__dict__.values())])
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

    def __init__(self, label: str, value: Union[int, float]) -> None:
        self.label = label
        self.value = value


class SensorStream(DataStream):

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.name = "Sensor"
        self.data_type = "Environmental Data"

        self.type_str = "Sensor"
        self.name_str = "readings processed"
        self.error_msg = "critical sensor alerts"

    def process_batch(self, data_batch: List[SensorType]) -> str:

        formatted_input = ", ".join(f"{data.label}:{data.value}"
                                    for data in data_batch)

        print(f"Stream ID: {self.stream_id}, Type: {self.data_type}")

        print(f"Processing sensor batch: [{formatted_input}]")

        data_dict: dict[str, list[int | float]] = {}
        for data_point in data_batch:

            if not data_point.label:
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
        output_data = stats.get(lookup_stat_name + "_" + lookup_stat)
        if lookup_stat == "avg":
            unit = self.unit(lookup_stat_name)

        if lookup_stat and lookup_stat_name and output_data:
            output_extra = (f"{lookup_stat} {lookup_stat_name}:"
                            f" {output_data}{unit}")

        return ", ".join(x for x in (output_std, output_extra) if x)

    def filter_data(self, data_batch: List[SensorType],
                    criteria: Optional[str] = None) -> List[SensorType]:
        if not criteria:
            return data_batch
        if criteria == "high-priority":
            return_list: list[SensorType] = []
            for data in data_batch:
                if data.label == "temp":
                    if data.value > 40:
                        return_list.append(data)
                elif data.label == "humidity":
                    if data.value > 90:
                        return_list.append(data)
                elif data.label == "pressure":
                    if data.value > 1100:
                        return_list.append(data)
                else:
                    if data.value > 50:
                        return_list.append(data)
            return return_list
        return ([data for data in data_batch
                if criteria in str(data.__dict__.values())])

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

    def __init__(self, label: str, value: Union[int, float]) -> None:
        self.label = label
        self.value = value


class TransactionStream(DataStream):

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.name = "Transaction"
        self.data_type = "Financial Data"

        self.type_str = "Transaction"
        self.name_str = "operations processed"
        self.error_msg = "large transaction"

    def process_batch(self, data_batch: List[TransactionType]
                      ) -> str:

        formatted_input = ", ".join(f"{data.label}:{data.value}"
                                    for data in data_batch)

        print(f"Stream ID: {self.stream_id}, Type: {self.data_type}")

        print(f"Processing transaction batch: [{formatted_input}]")

        data_dict: dict[str, list[int | float]] = {}
        for data_point in data_batch:

            if not data_point.label:
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
        net_flow: int = stats["net_flow"]
        sign = "+" if (net_flow >= 0) else ""

        if net_flow:
            output_extra = f"net flow: {sign}{net_flow} units"

        return ", ".join(x for x in (output_std, output_extra) if x)

    def filter_data(self, data_batch: List[TransactionType],
                    criteria: Optional[str] = None) -> List[TransactionType]:
        if not criteria:
            return data_batch
        if criteria == "high-priority":
            return [data for data in data_batch if data.value > 1000]
        return [data for data in data_batch
                if criteria in str(data.__dict__.values())]

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

    def __init__(self, event: str) -> None:
        self.event = event


class EventStream(DataStream):

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.name = "Event"
        self.data_type = "System Events"

        self.type_str = "Event"
        self.name_str = "events processed"
        self.error_msg = "errors detected"

    def process_batch(self, data_batch: List[EventType]) -> str:

        formatted_input = ", ".join(data.event for data in data_batch)

        print(f"Stream ID: {self.stream_id}, Type: {self.data_type}")

        print(f"Processing event batch: [{formatted_input}]")

        data_list: list[str] = []
        for data_point in data_batch:

            if not data_point.event:
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

    def filter_data(self, data_batch: List[EventType],
                    criteria: Optional[str] = None) -> List[EventType]:
        if not criteria:
            return data_batch
        if criteria == "high-priority":
            return [data for data in data_batch
                    if "error" in str(data.event).lower()]
        return [data for data in data_batch
                if criteria in str(data.__dict__.values())]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:

        data_processed = 0
        output_dict: dict[str, Union[str, int, float]] = {}
        output_dict["error"] = 0
        output_dict["login"] = 0
        output_dict["logout"] = 0
        for message in self.data:
            message_low = message.lower()
            if message_low not in output_dict.keys():
                output_dict[message_low] = 0
            output_dict[message_low] += 1

            if "error" in message_low and message_low not in "error":
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


class OtherType(DataType):

    other: Any

    def __init__(self, other: Any) -> None:
        self.other = other


class OtherStream(DataStream):

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.name = "Other"
        self.data_type = "Any"

        self.type_str = "Other"
        self.name_str = "items processed"
        self.error_msg = "other high-priority items present"

    def process_batch(self, data_batch: List[Any]) -> str:
        return super().process_batch(data_batch)


class StreamProcessor():

    name: str
    batch_num: int
    streams: dict[Type[DataType], DataStream]

    def __init__(self, name: str) -> None:

        if not name:
            raise ValueError("Stream name cannot be empty.")
        self.name = name

        self.batch_num = 0
        self.streams = {
            SensorType: SensorStream("S01"),
            TransactionType: TransactionStream("T01"),
            EventType: EventStream("E01"),
            DataType: OtherStream("O01"),
        }

    def process_all_batches(self, batches: List[DataType]) -> str:

        self.batch_num += 1
        return_string = f"Batch {self.batch_num} Results:"

        grouped: dict[DataStream, list[Any]] = {
            stream: [] for stream in self.streams.values()}

        fallback_stream = self.streams[DataType]

        for data in batches:
            found = False
            for data_type, stream in self.streams.items():
                if isinstance(data, data_type):
                    grouped[stream].append(data)
                    found = True
                    break
            if not found:
                grouped[fallback_stream].append(data)

        for stream in self.streams.values():

            grouped_len = len(grouped[stream])

            if grouped_len > 0:
                return_string += (
                    f"\n- {stream.type_str} data: {grouped_len}"
                    f" {stream.name_str}")

        return_string += ("\n\nStream filtering active: "
                          "High-priority data only\n")

        filtered_results: dict[DataStream, List[Any]] = {}

        total_filtered_num = 0

        for stream, batch in grouped.items():
            if batch:
                filtered_results[stream] = stream.filter_data(
                    batch, criteria="high-priority")
                total_filtered_num += len(filtered_results[stream])

        if total_filtered_num:
            return_string += "Filtered results: "
            error_list_str = []

            for stream, filtered in filtered_results.items():

                filter_len = len(filtered)

                if filter_len > 0:
                    error_list_str.append(
                        f"{filter_len} {stream.error_msg}")

            return_string += ", ".join(error_list_str)
        else:
            return_string += "No High-priority data"

        return return_string


def data_stream() -> None:

    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    print()

    print("Initializing Sensor Stream...")

    Sensor = SensorStream("SENSOR_001")

    print(Sensor.process_batch([
        SensorType("temp", 22.5),  # °C
        # SensorType("temp", 30),  # °C
        SensorType("humidity", 65),  # %
        SensorType("pressure", 1013)  # hPa
    ]))

    print()

    """
    Sensor_filtered = Sensor.filter_data([
        SensorType("temp", 50),  # °C
        SensorType("humidity", 65),  # %
        SensorType("pressure", 1013)  # hPa
        ], "high-priority")

    print([data.__dict__.values() for data in Sensor_filtered])

    print()
    """

    print("Initializing Transaction Stream...")

    Transaction = TransactionStream("TRANS_001")

    print(Transaction.process_batch([
        TransactionType("buy", 100),
        TransactionType("sell", 150),
        TransactionType("buy", 75)
    ]))

    print()

    """
    Transaction_filtered = Transaction.filter_data([
        TransactionType("buy", 100),
        TransactionType("sell", 10000),
        TransactionType("buy", 75)], "high-priority")

    print([data.__dict__.values() for data in Transaction_filtered])

    print()
    """

    print("Initializing Event Stream...")

    Event = EventStream("EVENT_001")

    print(Event.process_batch([
        EventType("login"),
        EventType("error"),
        EventType("logout")
    ]))

    print()

    """
    Event_filtered = Event.filter_data([
        EventType("login"),
        EventType("error"),
        EventType("logout")], "high-priority")

    print([data.__dict__.values() for data in Event_filtered])

    print()
    """

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
        EventType("git status"),
        TransactionType("sell", 1500),
        # OtherType("high-priority"),
        SensorType("humidity", 95),
        EventType("error")
    ]))

    print()

    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    data_stream()
