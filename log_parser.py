import re
from collections import Counter

with open("sample.log", "r") as file:
    logs = file.readlines()

ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
status_pattern = r'" (\d{3}) '

ips = [re.search(ip_pattern, log).group() for log in logs if re.search(ip_pattern, log)]
status_codes = [re.search(status_pattern, log).group(1) for log in logs if re.search(status_pattern, log)]

unique_ips = set(ips)
status_counts = Counter(status_codes)

print(f"Total Log Entries: {len(logs)}")
print(f"Unique IPs: {len(unique_ips)}")
print("Status Code Counts:", status_counts)
