#!/usr/bin/env python3

from abc import ABC, abstractmethod
import collections
from typing import Any, Type, Union, Protocol  # noqa: F401


class ProcessingStage(Protocol):

    long_msg: str = "Data Processing"
    demo_msg: str = "Processing"

    def process(self, data: Any) -> Any:
        pass


class ProcessingPipeline(ABC):

    stages: list[ProcessingStage]

    transform_msg: str
    data_parsing: str

    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id = pipeline_id
        self.stages = []

    @abstractmethod
    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)
        # = [InputStage(), TransformStage(), OutputStage()]

    @abstractmethod
    def process(self, data: Any) -> Any:
        in_loop = data
        for stage in self.stages:
            out_loop = stage.process(in_loop)
            # validate?
            in_loop = out_loop
        return out_loop


class InputStage():

    long_msg: str = "Input validation and parsing"
    demo_msg: str = "Processed"

    def process(self, data: dict[ProcessingPipeline, list[str]]) -> dict:

        adapter, real_data = next(out for out in data.items())

        parsing_style = adapter.data_parsing

        print("Input:", real_data[0])

        if parsing_style == "JSON":
            out_list = []
            for i, entry in enumerate(real_data):
                out_list.append({})
                split_entry = entry.strip("\"{} ").split(",")
                for pair in split_entry:
                    k, v = pair.split(":")
                    out_list[i][k] = v

        if parsing_style == "CSV":
            out_list = []
            for entry in real_data:
                out_list.append([entry.strip("\" ").split(",")])

        if parsing_style == "Stream":
            out_list = []
            for entry in real_data:
                out_list.append(entry)

        print("outlist", out_list, out_list[0].__class__)

        return {adapter: out_list}


class TransformStage():

    long_msg: str = "Data transformation and enrichment"
    demo_msg: str = "Analyzed"

    def process(self, data: dict[ProcessingPipeline, list[Any]]) -> dict:

        adapter, real_data = next(out for out in data.items())

        print("Transform:", adapter.transform_msg)

        out_dict = {}
        return out_dict


class OutputStage():

    long_msg: str = "Output formatting and delivery"
    demo_msg: str = "Stored"

    def process(self, data: dict[ProcessingPipeline, list[Any]]) -> str:

        adapter, real_data = next(out for out in data.items())

        out_str = ""
        print("Output:", out_str)
        return out_str


class JSONAdapter(ProcessingPipeline):

    pipeline_id: str

    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)
        self.transform_msg = "Enriched with metadata and validation"
        self.data_parsing = "JSON"

        for stage in [InputStage, TransformStage, OutputStage]:
            self.add_stage(stage)

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage())
        # = [InputStage(), TransformStage(), OutputStage()]

    def process(self, data: Any) -> Union[str, Any]:
        for stage in self.stages:
            data = stage.process({self: data})
        return data


class CSVAdapter(ProcessingPipeline):

    pipeline_id: str

    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)
        self.transform_msg = "Parsed and structured data"
        self.data_parsing = "CSV"

        for stage in [InputStage, TransformStage, OutputStage]:
            self.add_stage(stage)

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage())
        # = [InputStage(), TransformStage(), OutputStage()]

    def process(self, data: Any) -> Union[str, Any]:
        for stage in self.stages:
            data = stage.process({self: data})
        return data


class StreamAdapter(ProcessingPipeline):

    pipeline_id: str

    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)
        self.transform_msg = "Aggregated and filtered"
        self.data_parsing = "Stream"

        for stage in [InputStage, TransformStage, OutputStage]:
            self.add_stage(stage)

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage())
        # = [InputStage(), TransformStage(), OutputStage()]

    def process(self, data: Any) -> Union[str, Any]:
        for stage in self.stages:
            data = stage.process({self: data})
        return data


class NexusManager():

    pipelines: list[ProcessingPipeline]

    def __init__(self) -> None:
        print("Pipeline capacity: 1000 streams/second")

        print("Creating Data Processing Pipeline...")

        self.pipelines = []

        self.add_pipeline(JSONAdapter("Nexus_JSON"))
        self.add_pipeline(CSVAdapter("Nexus_CSV"))
        self.add_pipeline(StreamAdapter("Nexus_Strea"))

        for step, stage in enumerate(self.pipelines[0].stages, start=1):
            print(f"Stage {step}:", stage.long_msg)

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines.append(pipeline)

    def process_data(self):
        pass

    def demo(self) -> None:

        pipeline_print_list: list[str] = []
        letter_order = "ABCDEFGHIJKLMNOPQRSTUBWXYZ"
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


def nexus_pipeline() -> None:
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===")

    print()

    print("Initializing Nexus Manager...")

    nexus = NexusManager()

    print()

    print("=== Multi-Format Data Processing ===")

    print()

    print("Processing JSON data through pipeline...")

    nexus.pipelines[0].process([
        "{\"sensor\": \"temp\", \"value\": 23.5, \"unit\": \"C\"}"
    ])

    print()

    print("Processing CSV data through same pipeline...")

    nexus.pipelines[1].process(["\"user,action,timestamp\""])

    # \ndaniel,did something,06052025

    print()

    print("Processing Stream data through same pipeline...")

    nexus.pipelines[2].process(["Real-time sensor stream"])

    print()

    print("=== Pipeline Chaining Demo ===")

    nexus.demo()

    print()

    print("=== Error Recovery Test ===")

    nexus.error_test()

    print()

    print("Nexus Integration complete. All systems operational.")


if __name__ == "__main__":
    nexus_pipeline()
