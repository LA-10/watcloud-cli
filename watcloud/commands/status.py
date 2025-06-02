import subprocess
from .quota import data
import concurrent.futures

    
def ping(host):
    '''Pings a one host at a time'''
    # Define the command and arguments
    command = ['ping', '-c', '2', host]
    
    
    # Execute the command and capture the output
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)


    return result.returncode == 0



def get_status(status):
    if status == 1:
        return "✅ Online"
    else:
        return "❌ Offline"


def get_cluster_status():
    '''Displays the summary of the status of all subprocesses'''
    from .maintaince import is_under_maintenance
    
    def check_node_status(node):
            name = node["name"]
            hostnames = node.get("hostnames", [])
            if not hostnames:
                return f"{name.center(name_width)}{spacer}{'❓ No Hostname'.center(status_width)}"

            if is_under_maintenance(name):
                status = "🛠️ Maintenance"
            else:
                is_running = ping(hostnames[0])
                status = get_status(is_running)

            return (
                f"{name.center(name_width)}{spacer}"
                f"{status.center(status_width)}"
            )

    clusters = ["compute_nodes", "login_nodes", "General-Use Machines (Legacy)"]


    # Fixed column widths
    name_width = 15
    status_width = 20
    total_width = name_width + status_width + 6  
    spacer = " " * 2

    for cluster in clusters:
        title = f"{cluster} Cluster Status:"
        print("\n" + title.center(total_width) + "\n")

        # Header
        header = (
            f"{'Node'.center(name_width)}{spacer}"
            f"{'Status'.center(status_width)}"
        )
        print(header)
        print("-" * total_width)

        nodes = data["cluster"].get(cluster, [])

        

        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(check_node_status, node) for node in nodes]
            for future in concurrent.futures.as_completed(futures):
                print(future.result())