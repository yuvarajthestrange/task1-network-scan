# 3. Run SYN Scan

## 📌 Objective:
Perform a TCP SYN scan on your local network using Nmap to identify active devices and their open ports.

---

## 📖 Steps:

1. **Create and run a SYN scan using Nmap**  
   Example command:
   ```bash
   sudo nmap -sS 192.168.1.0/24

Save the scan results
Output the results to a text file for future analysis:
 ```bash
  sudo nmap -sS 192.168.1.0/24 -oN sample_results.txt

📂 Files in this folder:

File Name       	Description
scan_script.sh	        Shell script to automate the SYN scan.
sample_results.txt	Sample output of the scan results.
scan_diagram.png	Network diagram showing scanned devices.

📌 Notes:
Run Nmap with sudo/root privileges for accurate SYN scan results.

Replace 192.168.1.0/24 with your actual local subnet.
