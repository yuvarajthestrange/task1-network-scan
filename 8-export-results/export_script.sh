#!/bin/bash

# Script to run Nmap SYN scan and save results to scan_results.txt

TARGET_SUBNET="192.168.136.201/24"
OUTPUT_FILE="scan_results.txt"

echo "Starting SYN scan on subnet $TARGET_SUBNET..."
nmap -sS $TARGET_SUBNET > $OUTPUT_FILE

echo "Scan complete. Results saved in $OUTPUT_FILE."
