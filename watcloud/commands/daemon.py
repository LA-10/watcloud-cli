import psutil
import os
from colorama import init, Fore

def get_user_daemon_processes():
    user = os.getlogin()
    daemons = []

    for proc in psutil.process_iter(['pid', 'name', 'username', 'cmdline', 'terminal']):
        try:
            if proc.info['username'] == user:
                # Likely a daemon if it has no terminal (i.e., not interactive)
                if proc.info['terminal'] is None:
                    # Skip common noise
                    if not any(x in proc.info['name'] for x in ['bash', 'zsh', 'fish', 'python', 'login']):
                        daemons.append(proc)
        except (psutil.NoSuchProcess, psutil.AccessDenied, KeyError):
            continue

    return daemons

def print_daemon_status():
    init(autoreset=True)
    print("Daemon Status:\n--------------------")

    daemons = get_user_daemon_processes()

    if daemons:
        for proc in daemons:
            print(f"{Fore.GREEN}{proc.info['name']} (PID {proc.pid}): Running")
    else:
        print(f"{Fore.YELLOW}No user daemons running.")
