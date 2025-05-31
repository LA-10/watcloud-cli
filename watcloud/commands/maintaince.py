from .log import get_node_status, add_node, remove_node
from .status import ping

maintenance_msg = "🛠️ Maintenance"

def mark_maintenance(node_name):
    add_node(node_name, maintenance_msg)

def remove_maintenance(node_name):
    if ping(node_name) == 1:
        remove_node(node_name)
        print(f"{node_name} is up and running!")
    else:
        print(f"Maintenance status for {node_name} cannot be removed until the node is up and running.")

def is_under_maintenance(node_name):
    return get_node_status(node_name) == maintenance_msg

def print_under_maintenance(node_name):
    print(f"{node_name} is ", end = "")
    res = is_under_maintenance(node_name)

    if res:
        print("under maintenance")
    else:
        print("not under maintenance")
