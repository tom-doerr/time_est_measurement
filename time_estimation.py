import time
from typing import Tuple

def get_user_estimate() -> float:
    """Prompts the user for a time estimate in seconds."""
    while True:
        try:
            estimate_str = input("Enter your time estimate in seconds: ")
            estimate = float(estimate_str)
            if estimate > 0:
                return estimate
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def measure_actual_time() -> float:
    """Measures the actual time elapsed."""
    start_time = time.perf_counter()
    input("Press Enter when the time is up...")
    end_time = time.perf_counter()
    return end_time - start_time

def log_data(estimate: float, actual_time: float) -> None:
    """Logs the estimated and actual times to a file."""
    with open("time_log.txt", "a") as f:
        f.write(f"Estimate: {estimate}, Actual: {actual_time}\n")

def main() -> None:
    """Main function to orchestrate the time estimation process."""
    estimate = get_user_estimate()
    actual_time = measure_actual_time()
    log_data(estimate, actual_time)
    print("Time logged.")

if __name__ == "__main__":
    main()
