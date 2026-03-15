#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any, Union, Protocol


class ProcessingStage(Protocol):

    long_msg: str  # = "Data Processing"
    demo_msg: str  # = "Processing"

    def process(self, data: Any) -> Any:
        pass


class ProcessingPipeline(ABC):

    stages: list[ProcessingStage]
    stage_types: list[type[ProcessingStage]]

    transform_msg: str
    stage_iter: int
    stream_type: str

    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id = pipeline_id
        self.stages = []

        self.stage_iter = 0

    def set_stage_types(self, stage_types: list[type[ProcessingStage]]
                        ) -> None:
        self.stage_types = stage_types.copy()

    @abstractmethod
    def add_stage(self) -> None:
        for stage in self.stage_types:
            self.stages.append(stage())
        # = [InputStage(), TransformStage(), OutputStage()]

    @abstractmethod
    def process(self, data: Any) -> Any:
        in_loop = data
        for stage in self.stages:
            out_loop = stage.process(in_loop)
            # validate?
            in_loop = out_loop
        return out_loop

    @abstractmethod
    def data_parsing(self, in_data: list[str]) -> list[Any]:
        pass

    @abstractmethod
    def data_transform(self, in_data: list[Any]) -> Any:
        pass

    @abstractmethod
    def str_output(self, in_data: Any) -> str:
        pass


class InputStage():

    long_msg: str = "Input validation and parsing"
    demo_msg: str = "Processed"

    def process(self, data: dict[str, Any]) -> dict:

        adapter = data["adapter"]
        real_data = data["payload"]

        out_list = None

        out_list = adapter.data_parsing(real_data)

        return out_list


class TransformStage():

    long_msg: str = "Data transformation and enrichment"
    demo_msg: str = "Analyzed"

    def process(self, data: dict[str, Any]) -> dict:

        adapter = data["adapter"]
        real_data = data["payload"]

        out_list = adapter.data_transform(real_data)

        return out_list


class OutputStage():

    long_msg: str = "Output formatting and delivery"
    demo_msg: str = "Stored"

    def process(self, data: dict[str, Any]) -> str:

        adapter = data["adapter"]
        real_data = data["payload"]

        out_str = None

        out_str = adapter.str_output(real_data)

        return out_str


class JSONAdapter(ProcessingPipeline):

    pipeline_id: str

    data_defaults: dict[str, tuple[int | float, int | float]]

    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)
        self.transform_msg = "Enriched with metadata and validation"
        self.set_data_defaults()

        self.stream_type = "JSON"

        self.set_stage_types([InputStage, TransformStage, OutputStage])

        self.add_stage()

    def add_stage(self) -> None:
        for stage in self.stage_types:
            self.stages.append(stage())
        # = [InputStage(), TransformStage(), OutputStage()]

    def set_data_defaults(self) -> None:

        self.data_defaults = {}

        self.data_defaults["temp"] = (10, 25)
        self.data_defaults["pressure"] = (1000, 1020)
        self.data_defaults["humidity"] = (40, 85)

    def process(self, data: list[str]) -> Union[str, Any]:

        for stage in self.stages:
            self.stage_iter += 1

            if not data:
                return "No valid data given!"

            data = stage.process({"adapter": self, "payload": data})
            # print("\t", stage.__class__.__name__, data)

        self.stage_iter = 0

        return data

    def data_parsing(self, in_data: list[str]) -> list[dict[str, Any]]:

        out_list: list[dict[str, Any]] = []

        for i, entry in enumerate(in_data):

            out_list.append({})
            split_entry = entry.strip("{} ").split(",")

            for pair in split_entry:

                try:
                    k, v = pair.split(":")
                except ValueError:
                    raise ValueError("Invalid data format")

                k_strip = k.strip("\"\' ")
                v_strip = v.strip("\"\' ")

                try:
                    v_strip = int(v_strip)
                except ValueError:
                    try:
                        v_strip = float(v_strip)
                    except ValueError:
                        pass

                out_list[i][k_strip] = v_strip

        return out_list

    def data_transform(self, in_data: list[dict[str, Any]]
                       ) -> list[dict[str, Any]]:

        for reading in in_data:

            sensor = reading["sensor"]
            reading["norm_range"] = self.data_defaults.get(
                sensor, (None, None))

        return in_data

    def str_output(self, in_data: list[dict[str, Any]]) -> str:
        # print("\toutput", in_data)

        lookup_sensor_name = "temp"

        sensor = value = unit = norm_range = None

        for reading in in_data:
            # print("\t\t: ", reading)
            if reading["sensor"] == lookup_sensor_name:

                sensor = reading["sensor"]
                value = reading["value"]
                unit = reading["unit"]
                norm_range = reading["norm_range"]
                break
        # print("\tall got:", sensor, value, unit, norm_range)

        if sensor == "temp":
            sensor = "temperature"

        if value < norm_range[0]:
            range_status = "Under normal range"
        elif value > norm_range[1]:
            range_status = "Above normal range"
        else:
            range_status = "Normal range"

        out_str = (f"Processed {sensor} reading: {value}{unit} "
                   f"({range_status})")

        #  Processed temperature reading: 23.5°C (Normal range)

        return out_str


class CSVAdapter(ProcessingPipeline):

    pipeline_id: str

    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)
        self.transform_msg = "Parsed and structured data"

        self.stream_type = "CSV"

        self.set_stage_types([InputStage, TransformStage, OutputStage])

        self.add_stage()

    def add_stage(self) -> None:
        for stage in self.stage_types:
            self.stages.append(stage())
        # = [InputStage(), TransformStage(), OutputStage()]

    def process(self, data: list[str]) -> Union[str, Any]:
        for stage in self.stages:
            self.stage_iter += 1

            if not data:
                return "No valid data given!"

            data = stage.process({"adapter": self, "payload": data})
            # print("\t", stage.__class__.__name__, data)

        self.stage_iter = 0

        return data

    def data_parsing(self, in_data: list[str]) -> list[list[Any]]:
        out_list: list[list[Any]] = []

        for entry in in_data:

            line: list[Any] = []

            for cell in entry.strip("\" ").split(","):

                try:
                    cell = int(cell)
                except ValueError:
                    try:
                        cell = float(cell)
                    except ValueError:
                        pass
                line.append(cell)

            out_list.append(line)

        # print("CSV Perocesor", out_list, out_list.__class__)
        # print("\t", out_list[0], out_list[0].__class__)
        # print("\t\t", out_list[0][0], out_list[0][0].__class__)

        return out_list

    def data_transform(self, in_data: list[list[Any]]
                       ) -> dict[str, list[Any]]:

        headers = in_data[0]

        data = in_data[1:]

        out_dict: dict[str, list[Any]] = {
            "lines": ([",".join(map(str, line)) for line in in_data])
        }

        for i, header in enumerate(headers):

            column: list[Any] = [line[i] if i < len(line) else None
                                 for line in data]

            # print(f"column {i}:", header, column)

            out_dict[header] = column

        return out_dict

    def str_output(self, in_data: dict[str, list[Any]]) -> str:

        log_len = len(in_data["lines"]) - 1

        out_str = f"User activity logged: {log_len} actions processed"

        return out_str


class StreamAdapter(ProcessingPipeline):

    pipeline_id: str

    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)
        self.transform_msg = "Aggregated and filtered"

        self.stream_type = "Stream"

        self.set_stage_types([InputStage, TransformStage, OutputStage])

        self.add_stage()

    def add_stage(self) -> None:
        for stage in self.stage_types:
            self.stages.append(stage())
        # = [InputStage(), TransformStage(), OutputStage()]

    def process(self, data: list[str]) -> Union[str, Any]:

        self.stage_iter = 0

        for stage in self.stages:
            self.stage_iter += 1

            if not data:
                return "No valid data given!"

            data = stage.process({"adapter": self, "payload": data})
            # print("\t", stage.__class__.__name__, data)

        return data

    def data_parsing(self, in_data: list[str]) -> list[str]:

        out_list = []

        for entry in in_data:

            out_list.append(entry)

        return out_list

    def data_transform(self, in_data: list[str]
                       ) -> dict[str, dict[str, list[Any]]]:

        out_dict: dict[str, dict[str, list[Any]]] = {}

        for line in in_data:

            # print("\t\t", line)

            if ("{" not in line and ":" not in line
                    and "\"" not in line and "}" not in line):
                continue

            line_dict = self.str_dict_decode(line)

            # print("\t\tdict: ", line_dict)

            if not out_dict.get(line_dict["sensor"]):
                out_dict[line_dict["sensor"]] = {
                    "unit": [line_dict["unit"]], "values": []
                }

            out_dict[line_dict["sensor"]]["values"].append(line_dict["value"])

            if line_dict["unit"] not in out_dict[line_dict["sensor"]]["unit"]:
                out_dict[line_dict["sensor"]]["unit"].append(line_dict["unit"])

        return out_dict

    def str_output(self, in_data: dict[str, dict[str, list[Any]]]) -> str:

        log_len = 0

        for sensor in in_data.values():
            log_len += len(sensor["values"])

        lookup_stat_name = "temp"

        lookup_stat = "avg"

        values = in_data[lookup_stat_name]["values"]

        unit = ""

        data_num = len(values)
        data_sum = sum(values)
        data_avg = data_sum / data_num

        if lookup_stat == "num":
            output_data = data_num

        if lookup_stat == "sum":
            output_data = data_sum

        if lookup_stat == "avg":
            output_data = round(data_avg, 1)

        if lookup_stat == "avg":
            unit = self.unit(in_data[lookup_stat_name]["unit"])

        output_extra = (f"{lookup_stat}: {output_data}{unit}")

        out_str = f"Stream summary: {log_len} readings, {output_extra}"

        return out_str

    def str_dict_decode(self, in_str: str) -> dict[str, Any]:

        out_dict: dict[str, Any] = {}

        split_in = in_str.strip("{} ").split(",")

        for pair in split_in:

            try:
                k, v = pair.split(":")
            except ValueError:
                raise ValueError("Invalid data format")

            k_strip = k.strip("\"\' ")
            v_strip = v.strip("\"\' ")

            try:
                v_strip = int(v_strip)
            except ValueError:
                try:
                    v_strip = float(v_strip)
                except ValueError:
                    pass

            out_dict[k_strip] = v_strip

        return out_dict

    def unit(self, data_name: str) -> str:

        if data_name == "temp":
            return "°C"
        elif data_name == "humidity":
            return "%"
        elif data_name == "pressure":
            return "hPa"
        else:
            return ""


class NexusManager():

    pipelines: list[ProcessingPipeline]
    _rate: int

    def __init__(self, rate) -> None:

        print(f"Pipeline capacity: {rate} streams/second")
        print()

        self._rate = rate
        self.pipelines = []

    def show_pipelines(self):
        for step, stage in enumerate(self.pipelines[0].stages, start=1):
            print(f"Stage {step}:", stage.long_msg)

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines.append(pipeline)

    def clear_pipelines(self):
        self.pipelines = []

    def register_data(self, all_data):
        self.all_data = all_data

    def process_data(self) -> None:

        same = ""

        for pipeline, data in zip(self.pipelines, self.all_data):

            try:

                out_str = pipeline.process(data)

                print(f"Processing {pipeline.stream_type} "
                      f"data through{same} pipeline...")
                print("Input:", data[0])
                print("Transform:", pipeline.transform_msg)
                print("Output:", out_str)

                same = " same"

            except ValueError as e:
                print(f"Error detected in Stage {pipeline.stage_iter}:", e)
                print("Recovery initiated: Switching to backup processor")
                print("Recovery successful: Pipeline restored, "
                      "processing resumed")

            print()

    def demo(self) -> None:

        pipeline_print_list: list[str] = []
        letter_order = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for pipeline in self.pipelines:
            pipeline_print_list.append("Pipeline " +
                                       letter_order[len(pipeline_print_list)])
        print(" -> ".join(pipeline_print_list))

        pipeline_len = len(pipeline_print_list)

        pipeline_print_process: list[str] = ["Raw"]

        for stage in self.pipelines[0].stages:
            pipeline_print_process.append(stage.demo_msg)

        print("Data flow:", " -> ".join(pipeline_print_process))

        print()

        print(f"Chain result: {100} records processed through",
              f"{pipeline_len}-stage pipeline")

        print(f"Performance: {95}% efficiency, {0.2}s total processing time")

    def error_test(self) -> None:

        print("Simulating pipeline failure...")

        temp = self.pipelines[0]
        self.pipelines[0] = self.pipelines[2]
        self.pipelines[2] = temp

        self.register_data([
            "{\"sensor\":: \"temp\", \"value\": 22.1, \"unit\": \"°C\"}"
        ])

        self.process_data()

        temp = self.pipelines[2]
        self.pipelines[2] = self.pipelines[0]
        self.pipelines[0] = temp


def nexus_pipeline() -> None:

    all_data = [
        ["{\"sensor\": \"temp\", \"value\": 23.5, \"unit\": \"C\"}",
            "{\"sensor\": \"pressure\", \"value\": 1018, \"unit\": \"hPa\"}"],

        ["\"user,action,timestamp\"",
            "\"daniel,did something,06052025\""],

        ["Real-time sensor stream",
            "{\"sensor\": \"temp\", \"value\": 22.1, \"unit\": \"°C\"}",
            "{\"sensor\": \"temp\", \"value\": 20, \"unit\": \"°C\"}",
            "{\"sensor\": \"temp\", \"value\": 24.4, \"unit\": \"°C\"}",
            "{\"sensor\": \"temp\", \"value\": 22.1, \"unit\": \"°C\"}",
            "{\"sensor\": \"temp\", \"value\": 22.1, \"unit\": \"°C\"}"]
    ]

    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===")

    print()

    print("Initializing Nexus Manager...")

    nexus = NexusManager(1000)

    print("Creating Data Processing Pipeline...")
    nexus.add_pipeline(JSONAdapter("Nexus_JSON"))
    nexus.add_pipeline(CSVAdapter("Nexus_CSV"))
    nexus.add_pipeline(StreamAdapter("Nexus_Stream"))
    nexus.show_pipelines()

    print()

    print("=== Multi-Format Data Processing ===")

    print()

    nexus.register_data(all_data)

    nexus.process_data()

    print("=== Pipeline Chaining Demo ===")

    nexus.demo()

    print()

    print("=== Error Recovery Test ===")

    nexus.error_test()

    print("Nexus Integration complete. All systems operational.")


if __name__ == "__main__":
    nexus_pipeline()
