import psutil
import time

# Define thresholds
CPU_THRESHOLD = 80  # in percentage
MEMORY_THRESHOLD = 80  # in percentage
DISK_THRESHOLD = 80  # in percentage

def check_system_health():
    # Get CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        print(f"Alert: CPU usage is high at {cpu_usage}%")

    # Get memory usage
    memory_info = psutil.virtual_memory()
    if memory_info.percent > MEMORY_THRESHOLD:
        print(f"Alert: Memory usage is high at {memory_info.percent}%")

    # Get disk usage
    disk_info = psutil.disk_usage('/')
    if disk_info.percent > DISK_THRESHOLD:
        print(f"Alert: Disk usage is high at {disk_info.percent}%")

def main():
    while True:
        check_system_health()
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    main()
