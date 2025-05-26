# Risk Report for Network Port Scan

## Overview

This report summarizes the findings from the network port scan performed on the target subnet `192.168.136.201/24`. The scan was conducted using Nmap with SYN scan (`-sS`) to identify open ports and potential security risks.

---

## Scan Summary

- **Total IPs scanned:** 256
- **Hosts up:** 3
- **Open ports detected:**
  - Port 53 (DNS) open on 192.168.136.62
  - Port 7070 (RealServer) open on 192.168.136.103
- **Other hosts:** No open TCP ports detected or all ports filtered.

---

## Risk Assessment

| IP Address       | Port | Service   | Risk Level | Description                                   |
|------------------|------|-----------|------------|-----------------------------------------------|
| 192.168.136.62   | 53   | DNS       | Medium     | DNS service can be exploited for DNS poisoning or cache poisoning attacks. |
| 192.168.136.103  | 7070 | RealServer| High       | This port is often used by streaming servers; unpatched services may expose vulnerabilities. |

---

## Recommendations

- **DNS Server (Port 53):**
  - Restrict DNS queries to trusted sources.
  - Regularly update and patch DNS server software.
  - Implement DNSSEC where possible.

- **RealServer (Port 7070):**
  - Verify the necessity of the service and restrict access using firewalls.
  - Keep the service updated and monitor for vulnerabilities.
  - Consider network segmentation to isolate this service.

---

## Conclusion

The network shows minimal open ports; however, the identified services require proper hardening and monitoring to reduce attack surface. Continuous scanning and patch management are recommended to maintain network security.

---

*Report generated on:* 2025-05-26

