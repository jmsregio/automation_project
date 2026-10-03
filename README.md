# Mini Network Automation Project

## Overview
This project provides an automated health-checking script for Cisco network infrastructure. It reads target device parameters from a structured JSON inventory file, checks endpoint reachability over HTTPS/RESTCONF, displays a status summary in the terminal, and exports the final status records to a JSON output report.

## Project Structure
```text
automation_project/
│
├── inventory.json    # Contains target device details (Hostname, IP, Type, Location)
├── network_check.py  # Primary Python execution script
├── README.md         # Project documentation and instructions
└── output.json       # Generated output report containing device status (UP/DOWN)
```
## Features
- **Dynamic Inventory Management**: Reads device parameters directly from `inventory.json`.
- **Automated Health Monitoring**: Connects to multiple Cisco devices over HTTPS/RESTCONF to test reachability.
- **Console Reporting**: Formats device statuses into a clean, easy-to-read summary table.
- **JSON Data Export**: Saves real-time execution results directly into `output.json`.
- **Robust Error Handling**: Catches file access issues, invalid JSON formatting, and connection timeouts cleanly without breaking script execution.

## How to Run the Script
1. Open PowerShell or Command Prompt and navigate to the project directory:
   ```powershell
   cd automation_project
2. Through VS Code:
  Open network_check.py
  Press Run or F5 to run and debug code
  Check terminal for output and open output.json to check results
  
## Prerequisites
- Python 3.10 or higher
- Required Python modules:
  pip install requests urllib3
