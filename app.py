#!/usr/bin/env python3
import datetime
import os
import sys
import socket
from pathlib import Path

def log_execution():
    # Get current timestamp
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Get system information
    hostname = socket.gethostname()
    python_version = sys.version.split()[0]
    working_dir = os.getcwd()
    
    # Create a log message
    log_message = f"""
Cron Job Execution Details:
-------------------------
Timestamp: {current_time}
Hostname: {hostname}
Python Version: {python_version}
Working Directory: {working_dir}
Script Path: {Path(__file__).absolute()}
"""
    
    # Print to stdout (will be captured in cron log if configured)
    print(log_message)
    
    # Optionally, write to a specific log file
    log_file = Path("/tmp/cron_execution.log")
    with open(log_file, "a") as f:
        f.write(log_message + "\n")

if __name__ == "__main__":
    log_execution()
