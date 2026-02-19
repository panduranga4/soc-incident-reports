
🛡 SOC Incident Investigation Report – Brute Force Login Attempt
📌 Scenario
Multiple failed login attempts detected from a single IP address targeting corporate user accounts.
🔎 Investigation Steps
1️⃣ Log Analysis
Identified repeated failed login attempts.
Source IP: 192.168.1.25
Target user: admin
Attempts: 25 within 3 minutes
2️⃣ Suspicious Indicators
High frequency login attempts
Attempts outside normal working hours
Same IP targeting multiple usernames
3️⃣ Threat Intelligence Check
Checked IP on VirusTotal
No prior known malicious history (for simulation)
4️⃣ Action Taken
Blocklisted IP on firewall
Reset affected user passwords
Escalated to Tier 2 for monitoring
🛠 Tools Used
SIEM (Splunk – simulated logs)
VirusTotal
Basic Python log parsing
📊 MITRE ATT&CK Mapping
T1110 – Brute Force
T1078 – Valid Accounts
✅ Conclusion
Attack attempt successfully identified and contained. No successful compromise detected.
