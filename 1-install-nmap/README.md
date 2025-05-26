# Task 1: Install Nmap

This directory contains instructions, notes, and verification for installing Nmap on your system.

## 📌 Task Objective
- Install the Nmap network scanning tool.
- Verify the installation and record the installed version.

## 📦 Files Included

| File                   | Description                                                  |
|:-----------------------|:-------------------------------------------------------------|
| `install_notes.md`      | Notes on installation process and command used               |
| `verify_installation.sh`| Shell script to verify Nmap installation and version         |
| `version_check.png`     | Screenshot of terminal showing Nmap version after installation|

## 🛠️ Installation Steps

### For Debian/Ubuntu/Kali:
```bash
sudo apt update
sudo apt install nmap -y

For Fedora:
```bash
sudo dnf install nmap -y

For Arch:
```bash
sudo pacman -S nmap

✅ Verify Installation
Run the following command to check the installed Nmap version:
```bash
nmap --version

📷 Example:
A screenshot of the version check result is saved as version_check.png.

📜 Notes:
Ensure you have root privileges for installation.

Confirm successful installation before proceeding to the next task.

