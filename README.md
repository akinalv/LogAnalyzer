# Security Log Analyzer

A beginner-friendly Python cybersecurity project designed to analyze security events and detect potentially suspicious login activity.

## Project Overview

Security Log Analyzer is a simple tool that reads authentication events from a CSV file, analyzes login activity, identifies repeated failed login attempts, and generates a security report.

The project demonstrates basic security log analysis and Python automation.

## Features

- Reads security events from CSV files.
- Counts successful login attempts.
- Counts failed login attempts.
- Groups failed attempts by IP address.
- Detects suspicious IP addresses based on repeated failed logins.
- Generates an automated text report.

## Technologies Used

- Python 3
- CSV module
- pathlib module
- PowerShell
- Git and GitHub

## Project Structure

```text
LogAnalyzer/
├── logs/
│   └── security_events.csv
├── reports/
│   └── analysis_report.txt
├── main.py
├── .gitignore
└── README.md
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/akinalv/LogAnalyzer.git
```

2. Open the project directory:

```bash
cd LogAnalyzer
```

3. Run the analyzer:

```bash
python main.py
```

No external Python packages are required.

## Detection Logic

The analyzer counts failed login attempts for each IP address.

An IP address is flagged as suspicious when it generates **3 or more failed login attempts**.

## Example Output

```text
SECURITY LOG ANALYSIS
---------------------
Successful logins: 2
Failed logins: 4

Failed login attempts by IP:
192.168.1.15: 3
203.0.113.50: 1

Suspicious IP addresses:
WARNING: 192.168.1.15 - 3 failed attempts
```

## Learning Objectives

This project demonstrates practical skills in:

- Python programming
- Working with CSV files
- Basic security event analysis
- Identifying suspicious login patterns
- Automating security reports

## Project Status

Version 1.0 — Initial implementation.

Future improvements may include:
- Configurable detection thresholds
- Date and time filtering
- More security event types
- Graphical reports
- Improved error handling

## Disclaimer

This project is intended for educational purposes and uses sample security log data.

