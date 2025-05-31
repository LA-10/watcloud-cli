import shutil
import subprocess
from .quota import data

def nodes_status(nodes): 
    '''Pings all possible nodes and returns 1 if the node is online, and 0 otherwise'''
    nodes_stat = []

    for node in nodes:
        res = ping(node)

        nodes_stat.append(res)



    return nodes_stat
    

def ping(host):
    '''Pings a one host at a time'''
    # Define the command and arguments
    command = ['ping', '-c', '4', host]
    
    # Execute the command and capture the output
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)


    if result.returncode == 0:
       return 1
    else:
        return 0


def get_status(status):
    if status == 1:
        return "✅ Online"
    else:
        return "❌ Offline"


def get_cluster_status():
    '''Displays the summary of the status of all subprocesses'''
    from .maintaince import is_under_maintenance

    terminal_width = shutil.get_terminal_size().columns
    clusters = ["compute_nodes", "login_nodes", "General-Use Machines (Legacy)"]

    # Define fixed column widths
    name_width = 15
    hostname_width = 30
    status_width = 20

    total_width = name_width + hostname_width + status_width + 6  
    spacer = " " * 2

    for cluster in clusters:
        title = f"{cluster} Cluster Status:"
        print("\n" + title.center(total_width) + "\n")

        # Header
        header = (
            f"{'Node'.center(name_width)}{spacer}"
            f"{'Hostname'.center(hostname_width)}{spacer}"
            f"{'Status'.center(status_width)}"
        )
        print(header)
        print("-" * total_width)

        nodes = data["cluster"].get(cluster, [])

        for node in nodes:
            name = node["name"]
            hostnames = node.get("hostnames", [])

            for hostname in hostnames:
                if is_under_maintenance(name):
                    status = "🛠️ Maintenance"
                else:
                    is_running = ping(hostname)
                    status = get_status(is_running)

                row = (
                    f"{name.center(name_width)}{spacer}"
                    f"{hostname.center(hostname_width)}{spacer}"
                    f"{status.center(status_width)}"
                )
                print(row)