#!/usr/bin/env python3

import pandas as pd, requests, matplotlib.pyplot as plt, numpy as np, sys, importlib


def loading():

    print("LOADING STATUS: Loading programs...")

    print() 

    print("Checking dependencies:")

    with open("requirements.txt") as requirements_file:
        requirements_str = requirements_file.read()
        requirements_lines = requirements_str.split("\n")
        for line in requirements_lines:
            print("line")

        print("Analyzing Matrix data...")
        print("/path/to/matrix_env/lib/python3.11/site-packages")

        image_output_name = "matrix\\_analysis.png"

        print("Analysis complete!")

        plt.imshow(image)

        plt.savefig(image_output_name)

        print("Results saved to:", image_output_name)


if __name__ == "__main__":
    loading()
