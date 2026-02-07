import psutil

def monitor_system():
    cpu_threshold = float(input("Enter CPU threshold (%): "))
    memory_threshold = float(input("Enter memory threshold (%): "))
    disk_threshold = float(input("Enter disk threshold (%): "))
    
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('C:\\').percent
    
    print(f"CPU: {cpu_usage}% - {'ALERT' if cpu_usage > cpu_threshold else 'OK'}")
    print(f"Memory: {memory_usage}% - {'ALERT' if memory_usage > memory_threshold else 'OK'}")
    print(f"Disk: {disk_usage}% - {'ALERT' if disk_usage > disk_threshold else 'OK'}")

monitor_system()