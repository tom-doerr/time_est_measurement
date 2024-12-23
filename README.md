<div align="center">

# ⏱️ Time Estimation Trainer

[![Python](https://img.shields.io/badge/Python-3.6+-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Code Style](https://img.shields.io/badge/Code_Style-PEP8-purple?style=for-the-badge)](https://www.python.org/dev/peps/pep-0008/)

A simple CLI tool to help improve your time estimation skills through practice and feedback.

</div>

## 📋 Overview

Time Estimation Trainer is a command-line tool that helps you practice and improve your ability to estimate time intervals. It provides immediate feedback on your accuracy and maintains a log of your performance over time, complete with statistical analysis.

## ✨ Features

- 🎯 Practice estimating customizable time intervals
- 📊 Statistical analysis of your performance
- 📈 Visual boxplot representation of your results
- 📝 Persistent logging of all attempts
- 🔄 Track your progress over time

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher
- NumPy

### Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/time-estimation-trainer.git
cd time-estimation-trainer
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
