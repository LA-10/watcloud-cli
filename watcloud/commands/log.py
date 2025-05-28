import json
import os

# Path to the log file
LOG_PATH = os.path.join(os.path.dirname(__file__), 'watcloud/data/log.json')

# Load the log file into a dictionary
def load_log():
    if not os.path.exists(LOG_PATH):
        return {}
    try:
        with open(LOG_PATH, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {}

# Save the log dictionary to the file
def save_log(log_data):
    with open(LOG_PATH, 'w') as f:
        json.dump(log_data, f, indent=2)

# Add a new node with default status if it doesn't exist
def add_node(node_name, status="unknown", note=None):
    log_data = load_log()
    if node_name not in log_data:
        log_data[node_name] = {'status': status}
        if note:
            log_data[node_name]['note'] = note
        save_log(log_data)

# Check if a node already exists in the log
def node_exists(node_name):
    log_data = load_log()
    return node_name in log_data


# Get the status of a specific node
def get_node_status(node_name):
    log_data = load_log()
    entry = log_data.get(node_name)
    if entry:
        return entry.get('status', 'unknown')
    return 'unknown'

# Set or update the status of a specific node
def set_node_status(node_name, status, note=None):
    log_data = load_log()
    log_data[node_name] = {'status': status}
    if note:
        log_data[node_name]['note'] = note
    save_log(log_data)

# Optionally remove a node from the log
def remove_node(node_name):
    log_data = load_log()
    if node_name in log_data:
        del log_data[node_name]
        save_log(log_data)
