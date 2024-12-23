#!/usr/bin/env python3
import time
import argparse


def measure_actual_time(interval: float) -> float:
    """Measures the actual time elapsed."""
    start_time = time.perf_counter()
    input(f"Press Enter after {interval} seconds...")
    end_time = time.perf_counter()
    return end_time - start_time

def log_data(estimate: float, actual_time: float) -> None:
    """Logs the estimated and actual times to a file."""
    with open("time_log.txt", "a") as f:
        f.write(f"Estimate: {estimate}, Actual: {actual_time}\n")

def main():
    parser = argparse.ArgumentParser(description="Time estimation script.")
    parser.add_argument("--interval", type=float, default=10.0, help="Time interval to wait for, in seconds.")
    args = parser.parse_args()

    estimate = float(input("Enter your time estimate in seconds: "))
    actual_time = measure_actual_time(args.interval)
    log_data(estimate, actual_time)
    print("Time logged.")

if __name__ == "__main__":
    main()
