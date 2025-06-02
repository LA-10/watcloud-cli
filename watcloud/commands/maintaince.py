from .log_cmd import delete_node, create_node, show_node_status
from .status import ping
from .log import get_node_status, node_exists
from .quota import data
from colorama import Fore

maintenance_msg = "🛠️ Maintenance"

def node_found(node_name):
    clusters = ["compute_nodes", "login_nodes", "General-Use Machines (Legacy)"]

    for cluster in clusters:
        nodes = data["cluster"].get(cluster, [])
    
        for node in nodes:
            if node["name"] == node_name:
                return node
    return None

def mark_maintenance(node_name, note = None):

    if node_exists(node_name):
        print(f"{Fore.YELLOW}⚠️ The node '{node_name}' had been marked under maintenance previously")
    elif node_found(node_name):
        create_node(node_name, maintenance_msg, note)
    else:
        print(f"{Fore.RED}❌ '{node_name}' does not exist in the cluster.")
        print(f"{Fore.YELLOW}⚠️ Please double-check the spelling, or look through https://cloud.watonomous.ca/machines.")


def remove_maintenance(node_name):
    
    if node_exists(node_name):
        hostnames = node_found(node_name).get("hostnames", [])

        if not hostnames:
            print(f"{Fore.RED}❌ Cannot determine if the node is up and running.")
            delete_node(node_name)
        else:
            if ping(hostnames[0]):
                delete_node(node_name)
            else: print(f"{Fore.RED}❌ The node '{node_name}' is still down.")
    else:
        print(f"{Fore.RED}❌ '{node_name}' does not exist in the cluster.")
        print(f"{Fore.YELLOW}⚠️ Please double-check the spelling, or look through https://cloud.watonomous.ca/machines.")

def is_under_maintenance(node_name):
    return get_node_status(node_name) == maintenance_msg

def print_under_maintenance(node_name):
    show_node_status(node_name)

