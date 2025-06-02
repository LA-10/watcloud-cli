import json
import shutil
import psutil
import math
from colorama import init, Fore
import concurrent.futures

# Configuration
DEFAULT_LIMIT_GI = 20  # Default quota limit in GiB
DUE_DATE_FILE_NAME = "soft_threshold_due.txt"
DATA_DIR = "watcloud/data"

init(autoreset=True)

with open('watcloud/data/cluster_info.json') as f:
    data = json.load(f)

def check_disk_usage():
    """Check disk usage for the given path (default root)."""
    total, used, free = shutil.disk_usage("/")
    usage_percent = math.ceil(used / total * 100)

    print("\nDisk Usage:")
    print("-" * 20)

    print(f"Total: {round(total / (1024**3), 2)} GiB\nUsed: {round(used / (1024**3), 2)} GiB\nFree: {round(free / (1024**3), 2)} GiB\nUsed Percentage: ", end = "")

    if usage_percent <= 70:
        print(f"{Fore.GREEN}{usage_percent}%")
    elif usage_percent >= 90:
        print(f"{Fore.RED}{usage_percent}%")
    else:
        print(f"{Fore.YELLOW}{usage_percent}")

def check_cpu_usage():
    """
    Check CPU usage percentage over the given interval (seconds).
    """

    usage_percent = round(psutil.cpu_percent(interval= 1.0))

    print("\nCPU Usage:")
    print("-" * 20)

    print(f"Usage Percentage: ", end="")

    if usage_percent < 50:
        print(f"{Fore.GREEN}{usage_percent}%")
    elif usage_percent <= 70:
        print(f"{Fore.YELLOW}{usage_percent}%")
    else:
        print(f"{Fore.RED}{usage_percent}%")
    

def check_memory_usage():
    """Check system memory usage."""
    
    mem = psutil.virtual_memory()

    print("\nMemory Usage:")
    print("-" * 20)

    print(f"Total: {round(mem.total / (1024**3), 2)} GiB\nUsed: {round(mem.used / (1024**3), 2)} GiB\nFree: {round(mem.available / (1024**3), 2)} GiB\nUsed Percentage: ", end = "")
    usage_percent = round(mem.percent)

    if usage_percent <= 60:
        print(f"{Fore.GREEN}{usage_percent}%")
    elif usage_percent >= 80:
        print(f"{Fore.RED}{usage_percent}%")
    else:
        print(f"{Fore.YELLOW}{usage_percent}%")



def list_quota_usage():
    functions = [check_disk_usage, check_cpu_usage, check_memory_usage]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = {executor.submit(function): function.__name__ for function in functions}

        for future in concurrent.futures.as_completed(futures):
            check_name = futures[future]
            try:
                future.result()  
            except Exception as e:
                print(f"{Fore.RED}❌ Error running {check_name}: {e}")

