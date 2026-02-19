# SOC Incident Investigation Report – Brute Force Login Attempt

## 🧾 1. Incident Summary
Multiple failed login attempts detected from a single external IP address targeting corporate user accounts.

---

## 🚨 2. Alert Details
- Alert Type: Multiple Failed Login Attempts
- Source IP: 192.168.1.25
- Target User: admin
- Failed Attempts: 25 attempts in 3 minutes
- Timeframe: Outside normal working hours

---

## 🔍 3. Investigation Steps
1. Reviewed authentication logs in SIEM (Splunk – simulated).
2. Identified repeated failed login attempts from a single IP.
3. Checked if multiple usernames were targeted.
4. Verified IP reputation on VirusTotal.
5. Checked for successful login attempts after failures.

---

## ⚠️ 4. Findings
- High frequency login attempts within short time.
- Same IP targeting multiple accounts.
- No prior malicious history found for the IP.
- No successful compromise detected.

---

## 🧠 5. MITRE ATT&CK Mapping
- T1110 – Brute Force
- T1078 – Valid Accounts (Potential Risk)

---

## 🛡 6. Response Actions Taken
- Blocklisted source IP on firewall.
- Reset affected user passwords.
- Escalated to Tier 2 SOC for monitoring.

---

## ✅ 7. Conclusion
The brute force attempt was identified and contained successfully. No successful compromise occurred.
