import psutil
from datetime import datetime

# Time
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# CPU
cpu_usage = psutil.cpu_percent(interval=1)

# RAM
ram = psutil.virtual_memory()
ram_usage = ram.percent

# Disk
disk = psutil.disk_usage('/')
disk_usage = disk.percent

# Battery (optional)
battery = psutil.sensors_battery()
battery_percent = battery.percent if battery else "N/A"

# Output
report = f"""
📅 Time: {now}
🧠 CPU Usage: {cpu_usage}%
💾 RAM Usage: {ram_usage}%
📂 Disk Usage: {disk_usage}%
🔋 Battery: {battery_percent}%
-----------------------------
"""

print(report)

# Save to log file
with open("system_health.log", "a") as file:
    file.write(report)
