#!/bin/bash

# This script checks if Nmap is installed and displays its version

echo "Checking Nmap installation..."

# Check if nmap is available
if command -v nmap &> /dev/null
then
    echo "✅ Nmap is installed."
    echo "Nmap Version:"
    nmap --version
else
    echo "❌ Nmap is not installed."
    echo "Please install Nmap using: sudo apt install nmap -y"
fi
