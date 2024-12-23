#!/usr/bin/env python3
import time
import argparse


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
    parser.add_argument("--interval", type=float, default=10.0, help="Time interval to wait for, in seconds.")
    args = parser.parse_args()

    actual_time = measure_actual_time(args.interval)
    delta = actual_time - args.interval
    log_data(delta, actual_time)
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
        print(f"Average delta: {average_delta:.2f} seconds")

    except FileNotFoundError:
        print("No log file found.")
    except Exception as e:
        print(f"Error during analysis: {e}")


if __name__ == "__main__":
    main()
