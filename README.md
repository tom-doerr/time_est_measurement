<div align="center">

# ⏱️ Time Estimation Measurement

[![Python](https://img.shields.io/badge/Python-3.6+-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Code Style](https://img.shields.io/badge/Code_Style-PEP8-purple?style=for-the-badge)](https://www.python.org/dev/peps/pep-0008/)

A CLI tool for measuring time estimation accuracy as an indicator of brain state and stimulation levels.

</div>

## 📋 Overview

Time Estimation Measurement is a research tool that measures how accurately you estimate time intervals. Since time estimation varies with brain state - feeling faster during high mental activity and slower during low activity - these measurements can provide insights into cognitive states and attention levels.

## ✨ Features

- 🧠 Measure subjective time perception
- 📊 Statistical analysis of time perception accuracy
- 📈 Visual representation of perception variations
- 📝 Persistent data logging for trend analysis
- 🔬 Track cognitive state indicators over time

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher
- NumPy

### Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/time-est-measurement.git
cd time-est-measurement
```

2. Install dependencies:
```bash
pip install numpy
```

### Usage

Run the trainer with default settings (5-second interval):
```bash
./time_estimation.py
```

Or specify a custom time interval:
```bash
./time_estimation.py --interval 10.0
```

## 📊 Understanding the Output

The trainer provides:
- Immediate feedback on your current attempt
- Running average of all attempts
- Statistical analysis including:
  - Quartile distribution
  - Upper and lower fences
  - Total number of attempts

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
