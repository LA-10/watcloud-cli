from .log import *
from colorama import Fore
from .status import ping, get_status

def list_all_nodes():
    data = load_log()
    if not data:
        print(f"{Fore.YELLOW}⚠️ No nodes found in the log.")
        return

    print(f"{Fore.CYAN}📋 Node Log")
    print(f"{'-'*40}")
    for node, entry in data.items():
        status = entry.get('status', 'unknown')
        note = entry.get('note')
        print(f"{node}: {status}", end="")
        if note:
            print(f"  📝 {note}")
        else:
            print()

def show_node_status(node_name):
    from .maintaince import node_found

    if node_exists(node_name):
        status = get_node_status(node_name)
    elif node_found(node_name):
        status = ping(node_name)
    else:
        print(f"{Fore.RED}❌ '{node_name}' does not exist in the cluster.")
        print(f"{Fore.YELLOW}⚠️ Please double-check the spelling, or look through https://cloud.watonomous.ca/machines.")
        return False
    
    print(f"{Fore.CYAN}{node_name} status: {get_status(status)}")

def update_node_status(node_name, status, note=None):
    set_node_status(node_name, status, note)
    print(f"{Fore.GREEN}✅ Set '{node_name}' status to '{status}'.")

def create_node(node_name, status="unknown", note=None):
    add_node(node_name, status, note)
    print(f"{Fore.GREEN}✅ Added node '{node_name}' to log.py with status '{status}'.")

def delete_node(node_name):
    if node_exists(node_name):
        remove_node(node_name)
        print(f"{Fore.GREEN}✅ Removed node '{node_name}'.")
    else:
        print(f"{Fore.YELLOW}⚠️ Node '{node_name}' not found.")
