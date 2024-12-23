#!/usr/bin/env python3
import time
import argparse
import numpy as np
import plot_cli
import subprocess


def measure_actual_time(interval: float) -> float:
    """Measures the actual time elapsed."""
    start_time = time.perf_counter()
    input(f"Press Enter after {interval} seconds...")
    end_time = time.perf_counter()
    return end_time - start_time

def log_data(delta: float, actual_time: float) -> None:
    """Logs the estimated and actual times to a file."""
    with open("time_log.txt", "a") as f:
        f.write(f"Delta: {delta}, Actual: {actual_time}\n")

def main():
    parser = argparse.ArgumentParser(description="Time estimation script.")
    parser.add_argument("--interval", type=float, default=5.0, help="Time interval to wait for, in seconds.")
    args = parser.parse_args()

    actual_time = measure_actual_time(args.interval)
    delta = actual_time - args.interval
    log_data(delta, actual_time)
    print(f"Delta for this run: {delta:+.2f} seconds")
    analyze_data()
def analyze_data() -> None:
    """Analyzes the data from time_log.txt."""
    try:
        with open("time_log.txt", "r") as f:
            lines = f.readlines()

        if not lines:
            print("No data to analyze.")
            return

        deltas = [float(line.split(",")[0].split(": ")[1]) for line in lines]
        average_delta = sum(deltas) / len(deltas)
        print(f"Average delta: {average_delta:+.2f} seconds")
        print(f"Number of data points: {len(deltas)}")
        print_boxplot(deltas)
        plot_histogram(deltas)

    except FileNotFoundError:
        print("No log file found.")
    except Exception as e:
        print(f"Error during analysis: {e}")

def print_boxplot(deltas: list[float]) -> None:
    """Prints a boxplot of the deltas."""
    if not deltas:
        print("No data to create a boxplot.")
        return

    # Calculate boxplot values
    q1 = np.percentile(deltas, 25)
    q2 = np.percentile(deltas, 50)
    q3 = np.percentile(deltas, 75)
    iqr = q3 - q1
    lower_fence = q1 - 1.5 * iqr
    upper_fence = q3 + 1.5 * iqr

    print(f"Boxplot of deltas:")
    print(f"  Lower fence: {lower_fence:+.2f}")
    print(f"  Q1 (25%): {q1:+.2f}")
    print(f"  Q2 (50%): {q2:+.2f}")
    print(f"  Q3 (75%): {q3:+.2f}")
    print(f"  Upper fence: {upper_fence:+.2f}")

def plot_histogram(deltas: list[float]) -> None:
    """Plots a histogram of the deltas using plot-cli."""
    if not deltas:
        print("No data to create a histogram.")
        return

    # Save deltas to a temporary file
    with open("deltas.txt", "w") as f:
        for delta in deltas:
            f.write(f"{delta}\n")

    # Call plot-cli to generate the histogram
    subprocess.run(["plot-cli", "histogram", "--data", "deltas.txt", "--title", "Histogram of Deltas"])


if __name__ == "__main__":
    main()
