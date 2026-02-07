import psutil
def check_cpu_threshold():

    cpu_threshold = float(input("Enter CPU usage threshold "))
    cpu_usage = psutil.cpu_percent(interval=1)
    
    print(f"Current CPU usage: {cpu_usage}%")
    
    if cpu_usage > cpu_threshold:
        print("cpu alert sent on mail")
    else:
        print("cpu usage is normal")
check_cpu_threshold()