from datetime import datetime, timedelta, date
import shutil
import os

# Configuration
DEFAULT_LIMIT_GI = 10  # Default quota limit in GiB (Placeholder for now)
SOFT_THRESHOLD = 15    # in GiB (Placeholder for now)
HARD_THRESHOLD = 30    # in GiB (Placeholder for now)

DUE_DATE_FILE = "watcloud/data/soft_threshold_due.txt"

def check_quota(directory, limit_gi=DEFAULT_LIMIT_GI):
    """Check if the disk usage of a directory exceeds the quota."""
    total, used, free = shutil.disk_usage(directory)
    used_gi = used / (1024 ** 3)  # Convert bytes to GiB

    print(f"\nChecking quota for: {directory}")
    print(f"Used: {used_gi:.2f} GiB / Limit: {limit_gi:.2f} GiB")

    if used_gi > HARD_THRESHOLD:
        print(f"❌ CRITICAL: Quota of {HARD_THRESHOLD} GiB exceeded!")
        raise Exception("disk quota exceeded")

    elif used_gi > SOFT_THRESHOLD:
        print(f"⚠️  WARNING: Soft threshold of {SOFT_THRESHOLD} GiB reached.")

        if not os.path.exists(DUE_DATE_FILE):
            due_date = (date.today() + timedelta(days=7)).strftime("%Y-%m-%d")
            with open(DUE_DATE_FILE, "w") as f:
                f.write(due_date)
            return "warning"

        else:
            with open(DUE_DATE_FILE, "r") as f:
                due_date_str = f.readline().strip()
                due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
                if date.today() >= due_date.date():
                    raise Exception("disk quota exceeded")


    else:
        print("✅ Quota within safe limits.")
        if os.path.exists(DUE_DATE_FILE):
            os.remove(DUE_DATE_FILE)  # Reset if usage is back to safe
        return "ok"



