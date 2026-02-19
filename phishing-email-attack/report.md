🛡️ SOC Incident Investigation Report – Phishing Email Attack
1. Incident Summary
User reported suspicious email claiming to be from IT Support requesting password reset via external link.
2. Email Details
Sender: it-support@secure-company-login.com
Recipient: employee@company.com
Subject: Urgent: Reset Your Password Immediately
Attachment: None
Embedded Link: http://secure-company-login.com/reset�
3. Investigation Steps
✔️ Analyzed email header
✔️ Extracted sender domain
✔️ Checked domain reputation on VirusTotal
✔️ Verified SPF/DKIM status
✔️ Analyzed embedded URL
4. Findings
Domain recently registered
SPF failed
URL flagged as phishing by VirusTotal
Mismatch between display name and actual sender domain
5. MITRE ATT&CK Mapping
T1566 – Phishing
T1204 – User Execution
6. Action Taken
Blocked sender domain on email gateway
Added URL to firewall blocklist
Reset user password
Escalated to Tier 2
7. Conclusion
Phishing attempt confirmed. No successful compromise detected.
