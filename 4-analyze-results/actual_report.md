# 📊 Nmap Scan Analysis Report

---

## 📅 Date of Scan:
2025-05-26

## 🌐 Network Scanned:
192.168.136.0/24

## 🔍 Active Hosts Detected:
- 192.168.136.62
- 192.168.136.103
- 192.168.136.201

## 🛡️ Open Ports and Services:
| Host IP         | Open Port | Service     | MAC Address               |
|------------------|-----------|-------------|----------------------------|
| 192.168.136.62   | 53        | domain      | 86:C4:67:BE:2F:4E (Unknown) |
| 192.168.136.103  | 7070      | realserver  | F8:54:F6:EE:72:C5 (AzureWave Technology) |
| 192.168.136.201  | None      | None        | Not available             |

---

## 🔐 Security Risks:
- **Port 53 (DNS)** open on 192.168.136.62 → If unused for internal DNS, consider disabling to avoid abuse.
- **Port 7070 (RealServer)** on 192.168.136.103 → Rare service port; ensure this is intentional and monitored.
- **All ports closed** on 192.168.136.201 → No immediate concerns.

---

## 📌 Recommendations:
- Restrict Port 53 and 7070 to trusted IPs using firewall rules.
- Monitor RealServer service for unusual traffic.
- Document and validate all open ports and their intended use.
- Maintain updated security patches on hosts.

---

## 📝 Analyst:
Yuvaraj
