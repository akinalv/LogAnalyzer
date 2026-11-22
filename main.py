import csv
from pathlib import Path

file_path = Path("logs") / "security_events.csv"
report_path = Path("reports") / "analysis_report.txt"

success_count = 0
failed_count = 0
failed_by_ip = {}

# Read security events
with open(file_path, "r", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)

    for event in reader:
        status = event["status"]
        ip_address = event["ip_address"]

        if status == "Success":
            success_count += 1

        elif status == "Failed":
            failed_count += 1
            failed_by_ip[ip_address] = failed_by_ip.get(ip_address, 0) + 1

# Create report content
report = []
report.append("SECURITY LOG ANALYSIS")
report.append("---------------------")
report.append(f"Successful logins: {success_count}")
report.append(f"Failed logins: {failed_count}")

report.append("")
report.append("Failed login attempts by IP:")

for ip, count in failed_by_ip.items():
    report.append(f"{ip}: {count}")

report.append("")
report.append("Suspicious IP addresses:")

for ip, count in failed_by_ip.items():
    if count >= 3:
        report.append(f"WARNING: {ip} - {count} failed attempts")

# Save report
report_path.parent.mkdir(parents=True, exist_ok=True)
report_path.write_text("\n".join(report), encoding="utf-8")

# Display report
print("\n".join(report))
print(f"\nReport saved to: {report_path}")



