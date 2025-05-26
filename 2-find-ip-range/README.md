# 📡 2. Find Local IP Range

## 📖 Overview

In this section, we determine the local IP address and subnet mask of the machine to identify the IP range of the local network. This information is essential for scanning the network effectively.

---

## 📂 Contents

| File                  | Description                                      |
|-----------------------|-------------------------------------------------|
| ifconfig_sample.txt    | Sample output of the `ifconfig` or `ip a` command |
| identify_subnet.py     | Python script to extract IP and subnet, and calculate network range |

---

## 🛠️ How to Use

1. Run the following command to get your network configuration:

- On Linux/macOS:
  ```bash
  ifconfig

or
 ```bash
  ip a

On Windows:
 ```bash
  ipconfig
Save the output to ifconfig_sample.txt.

Run the Python script to automatically find your IP range:
 ```bash
  python3 identify_subnet.py

🎯 Objective
Identify local IP address and subnet mask

Calculate network IP range in CIDR notation


