#!/bin/bash

# Simple Nmap TCP SYN scan over local network

echo "Starting TCP SYN Scan on local network..."

# Replace '192.168.1.0/24' with your actual subnet if different
nmap -sS 192.168.1.0/24 -oN sample_results.txt

echo "Scan completed. Results saved in sample_results.txt"
