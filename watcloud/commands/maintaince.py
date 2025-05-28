from log import set_node_status, get_node_status
from status import ping, get_status

maintaince_msg = "🛠️ Maintenance"

def mark_maintenance(node_name, until_time = None):
    set_node_status(node_name, "🛠️ Maintenance", until_time)
    
def remove_maintenance(node_name):
    res = ping(node_name)

    set_node_status(node_name, get_status(res))
    
def is_under_maintenance(node_name):
    return get_node_status(node_name) == "🛠️ Maintenance"