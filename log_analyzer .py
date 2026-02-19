from collections import Counter

log_file = "sample_auth_logs.txt"

failed_ips = []
failed_users = []

with open(log_file, "r") as file:
    for line in file:
        if "Failed login" in line:
            parts = line.strip().split()
            user = parts[4]
            ip = parts[-1]
            failed_users.append(user)
            failed_ips.append(ip)

ip_count = Counter(failed_ips)
user_count = Counter(failed_users)

print("Suspicious IPs:")
for ip, count in ip_count.items():
    if count >= 3:
        print(f"{ip} - {count} failed attempts")

print("\nTargeted Users:")
for user, count in user_count.items():
    print(f"{user} - {count} failed attempts")
