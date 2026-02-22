#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional, Tuple  # noqa: F401


class DataProcessor(ABC):

    validation_mesg = "Validation:"
    invalid_data_mesg = "Invalid data for"
    processed_mesg = "Processed data: "

    @abstractmethod
    def process(self, data: Any) -> str:
        print(f"Processing data: {data}")
        if not self.validate(data):
            return self.invalid_data_mesg + self.__class__.__name__
        return self.format_output(data)

    @abstractmethod
    def validate(self, data: Any) -> bool:
        if len(data) > 1:
            for item in data:
                try:
                    buffer = int(item)
                except ValueError:
                    return False
        del buffer
        print(self.validation_mesg, "Numeric data verified")
        return True

    def format_output(self, result: str) -> str:
        return self.processed_mesg + result


class NumericProcessor(DataProcessor):
    processed_mesg = "Processed "

    def process(self, data: Any) -> str:
        if not self.validate(data):
            return self.invalid_data_mesg + self.__class__.__name__
        i_len = len(data)
        i_sum = sum(data)
        i_avg = i_sum / i_len
        return self.format_output(f"{i_len} numeric values, " +
                                  f"sum={i_sum}, avg={i_avg:.1f}")

    def validate(self, data: Any) -> bool:
        if len(data) > 1:
            for item in data:
                try:
                    buffer = int(item)
                except ValueError:
                    return False
        del buffer
        print(self.validation_mesg, "Numeric data verified")
        return True

    def format_output(self, result: str) -> str:
        return self.processed_mesg + result


class TextProcessor(DataProcessor):
    processed_mesg = "Processed text: "

    def process(self, data: Any) -> str:
        if not self.validate(data):
            return self.invalid_data_mesg + self.__class__.__name__
        s_len = len(data)
        word_count = len(data.strip().split())
        return self.format_output(f"{s_len} characters, {word_count} words")

    def validate(self, data: Any) -> bool:
        try:
            buffer = str(data)
        except ValueError:
            return False
        del buffer
        print(self.validation_mesg, "Text data verified")
        return True

    def format_output(self, result: str) -> str:
        return self.processed_mesg + result


class LogProcessor(DataProcessor):
    log_type = ""

    def process(self, data: Any) -> str:
        if not self.validate(data):
            return self.invalid_data_mesg + self.__class__.__name__
        if data.startswith("ERROR") or data.startswith("ALERT"):
            self.log_type = "[ALERT]"
        elif data.startswith("INFO"):
            self.log_type = "[INFO]"
        elif data.startswith("DEBUG"):
            self.log_type = "[DEBUG]"
        else:
            self.log_type = "[UNKNOWN]"
        return self.format_output(data)

    def validate(self, data: Any) -> bool:
        try:
            buffer = str(data)
        except ValueError:
            return False
        if not (data.startswith("ERROR") or data.startswith("INFO")
                or data.startswith("DEBUG") or data.startswith("ALERT")):
            print("Invalid data for LogProcessor")
        del buffer
        print(self.validation_mesg, "Log entry verified")
        return True

    def format_output(self, result: str) -> str:
        return self.processed_mesg + result


"""
System Architecture:
• Base Class: DataProcessor - an abstract base class defining the common
processing interface
• Specialized Classes: NumericProcessor(), TextProcessor(), LogProcessor()
(no constructor parameters required)
• Required Methods (must be implemented in all classes):
    ◦ process(self, data: Any) -> str - Process the data and return result
    string
    ◦ validate(self, data: Any) -> bool - Validate if data is appropriate for
    this processor
    ◦ format_output(self, result: str) -> str - Format the output string
• Polymorphic Behavior: Same method calls, different specialized behaviors
Required Implementation:
• Create a DataProcessor abstract base class using ABC and @abstractmethod
• Mark process() and validate() as abstract methods
• Provide a default implementation for format_output() that can be overridden
• Override abstract methods in subclasses to provide specialized behavior
• Demonstrate polymorphic usage by processing different data types through the
same interface
• Include proper error handling for invalid data
"""


def stream_processor():
    num_p = NumericProcessor()
    txt_p = TextProcessor()
    log_p = LogProcessor()

    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    print()
    numeric_data = [1, 2, 3, 4, 5]
    print(f"Processing data: {numeric_data}")
    print("Output:", num_p.process(numeric_data))
    print()
    text_data = "Hello Nexus World"
    print(f"Processing data: {text_data}")
    print("Output:", txt_p.process(text_data))
    print()
    log_data = "ERROR: Connection timeout"
    print(f"Processing data: {log_data}")
    print("Output:", log_p.process(log_data))
    print()

    print("=== Polymorphic Processing Demo ===")

    print("Processing multiple data types through same interface...")
    print("Result 1:", num_p.process([1, 2, 3]))
    print("Result 2:", txt_p.process("Hello World!"))
    print("Result 3:", log_p.process("INFO level detected: System ready"))


if __name__ == "__main__":
    stream_processor()
