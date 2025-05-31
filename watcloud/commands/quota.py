import json
import shutil
import subprocess
import psutil

# Configuration
DEFAULT_LIMIT_GI = 20  # Default quota limit in GiB
DUE_DATE_FILE_NAME = "soft_threshold_due.txt"
DATA_DIR = "watcloud/data"

with open('watcloud/data/cluster_info.json') as f:
    data = json.load(f)

def check_disk_usage(path="/"):
    """Check disk usage for the given path (default root)."""
    total, used, free = shutil.disk_usage(path)
    usage_percent = used / total * 100
    return {
        "total_gb": total / (1024**3),
        "used_gb": used / (1024**3),
        "free_gb": free / (1024**3),
        "usage_percent": usage_percent
    }

def check_cpu_usage(interval=1):
    """
    Check CPU usage percentage over the given interval (seconds).
    """
    usage_percent = psutil.cpu_percent(interval=interval)
    return usage_percent

def check_memory_usage():
    """Check system memory usage."""
    mem = psutil.virtual_memory()
    return {
        "total_gb": mem.total / (1024**3),
        "used_gb": mem.used / (1024**3),
        "free_gb": mem.available / (1024**3),
        "usage_percent": mem.percent
    }


def list_quota_usage():
    nodes = (
          data["cluster"]["compute_nodes"]
        + data["cluster"]["login_nodes"]
        + data["cluster"]["General-Use Machines (Legacy)"]
    )

    print(f"{'Node':<20} {'Disk':<10} {'Used (GiB)':<12} {'Soft Limit':<12} {'Hard Limit':<12}")
    print("-" * 70)

    for node in nodes:
        node_name = node["name"]
        disks = node.get("specs", {}).get("quota", {}).get("node-local_disk", [])

        for disk in disks:
            disk_name = disk.get("name", "unknown")

            soft_limit = next((limit["size"] for limit in disk.get("size_limit", []) if limit["name"] == "soft"), "N/A")
            hard_limit = next((limit["size"] for limit in disk.get("size_limit", []) if limit["name"] == "hard"), "N/A")

            try:
                total, used, _ = shutil.disk_usage(node_name)
                used_gib = used / (1024 ** 3)
                used_str = f"{used_gib:.2f}"
            except Exception:
                used_str = "N/A"

            print(f"{node_name:<20} {disk_name:<10} {used_str:<12} {soft_limit:<12} {hard_limit:<12}")
