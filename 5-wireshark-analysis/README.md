# 📊 Wireshark Packet Capture & Analysis

## 📌 Objective:
Capture live network traffic using Wireshark and analyze it by applying specific display filters to inspect network behavior and detect potential anomalies.

---

## 📥 Files Included:
- `capture.pcapng` — The actual packet capture file obtained from Wireshark.
- `wireshark_filters.txt` — List of useful Wireshark display filters used during analysis.
- `capture_screenshot.png` — Screenshot of the Wireshark capture or applied filters.
- `README.md` — This documentation file explaining the module.

---

## 📌 How to Capture Packets:
1. Open **Wireshark**.
2. Select your active network interface.
3. Click **Start Capturing Packets**.
4. After a few minutes of traffic, click **Stop**.
5. Save the capture file as `capture.pcapng`.

---

## 📌 How to Apply Filters:
Use display filters in Wireshark's filter bar, such as:
- `http`
- `tcp.port == 80`
- `ip.addr == 192.168.1.1`
- `dns`

---

## 📤 Upload Files:
Once you capture and save your data:
- Save `capture.pcapng`
- Create `wireshark_filters.txt` with your filters
- Take a screenshot `capture_screenshot.png`  
And add them to this directory.

---

## 📅 Task Completed On:
`26-05-2025`
