#!/usr/bin/env python3

def loading() -> None:

    print()

    print("LOADING STATUS: Loading programs...")

    print()

    print("Checking dependencies:")

    try:
        import pandas as pd
        print(f"[OK] pandas ({pd.__version__}) - Data manipulation ready")
        # import requests
        # print(f"[OK] requests ({requests.__version__})
        #       - Network access ready")
        import numpy as np
        print(f"[OK] numpy ({np.__version__}) - Network access ready")
        import matplotlib as mat
        import matplotlib.pyplot as plt
        print(f"[OK] matplotlib ({mat.__version__}) - Visualization ready")
        # import numpy as np
        # import sys
        # import importlib
    except ModuleNotFoundError as e:
        print("ModuleNotFoundError:", e)
        print("To install all Requirements for this",
              "Script use one of the following:")
        print("$> pip install -r requirements.txt")
        print("$> poetry install")
        return

    def process_data(data: np.ndarray) -> pd.DataFrame:
        print(f"Processing {len(data)} data points...")

        data_set = pd.DataFrame(data, columns=["signal"])

        return data_set

    def genrerate_visualisation(
            data: pd.DataFrame, image_output_name: str) -> None:

        print("Generating visualization...")

        plt.plot(data["signal"])

        plt.savefig(image_output_name)

    print()

    data = np.random.rand(1000)

    # print(data)
    # print()
    # print(type(data))

    print("Analyzing Matrix data...")

    processed_data = process_data(data)

    image_output_name = "matrix\\_analysis.png"

    genrerate_visualisation(processed_data, image_output_name)

    print()

    print("Analysis complete!")
    print("Results saved to:", image_output_name)


if __name__ == "__main__":

    loading()
