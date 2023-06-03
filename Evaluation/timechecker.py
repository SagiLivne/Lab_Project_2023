import os
import sys
import numpy
import argparse

import numpy as np

import associate
import matplotlib

import datetime
import matplotlib.pyplot as plt

def read_file_list(filename):
    list = []
    with open(filename, 'r') as file:
        lines = file.readlines()  # Read the content of the file

        for line in lines:
            line = line.strip()  # Remove leading/trailing whitespace
            if line:  # Check if the line is not empty
                line_numbers = line.split()  # Split the line into substrings
                for number in line_numbers:
                    list.append(int(number))  # Convert and append the number to the list
    return list 

if __name__ == "__main__":
    ground_truth = sys.argv[1]
    orbslam_file = sys.argv[2]
    ground_truth_vals = read_file_list(ground_truth, False)
    orbslam_vals = read_file_list(orbslam_file, False)

    fig = plt.figure()

    plt.plot(ground_truth_vals, label = "ground_truth", color = "red")
    plt.plot(ground_truth_vals, label = "orbslam", color = "blue")

    plt.show()

