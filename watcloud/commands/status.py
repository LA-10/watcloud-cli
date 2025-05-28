# import requests
# from bs4 import BeautifulSoup
import subprocess
import os
import platform
import re
from log import node_exists, add_node

def nodes_status(nodes): 
    '''Pings all possible nodes and returns 1 if the node is online, and 0 otherwise'''
    nodes_status = []

    for node in nodes:
        res = ping(node)

        nodes_status.append(res)



    return nodes_status
    

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
    '''Displays the summary of the staus of all subproccesses'''

    nodes_status = nodes_status(nodes)

    print(f"Cluster Status:\n")

    print("\nNodes:")

    for i in range(len(nodes)):

        if not node_exists(nodes[i]):
            add_node(nodes[i], get_status(nodes_status[i]))
        
        print(f"- {nodes[i]}: {get_status(nodes_status[i])}")
     


# Retriving the nodes from  (never run, just commented out for future development)
# url = 'https://cloud.watonomous.ca/machines'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')

# # Find the first h1 element
# li_element = soup.findAll('li')

# hosts = []

# for li in li_element:
#     text = li.get_text()
#     if not(re.search("watonomous.ca", text) == "None"):
#         hosts.append(text)

# Retriving nodes manually 
nodes = ["delta-ubuntu2.ext.watonomous.ca", "delta-ubuntu2.cluster.watonomous.ca",
          "tr-ubuntu3.cluster.watonomous.ca", "tr-ubuntu3.ts.watonomous.ca",
          "derek3-ubuntu2.cluster.watonomous.ca", "derek3-ubuntu2.ts.watonomous.ca",
          "bastion.cluster.watonomous.ca", "bastion.watonomous.ca",
          "wato-login1.ext.watonomous.ca", "wato-login1.cluster.watonomous.ca", "wato-login1.ts.watonomous.ca",
          "wato-login2.ext.watonomous.ca", "wato-login2.cluster.watonomous.ca", "wato-login2.ts.watonomous.ca",
          "trpro-slurm2.cluster.watonomous.ca", "trpro-slurm2.ts.watonomous.ca", 
          "wato2-slurm1.cluster.watonomous.ca", "wato2-slurm1.ts.watonomous.ca",
          "trpro-slurm1.cluster.watonomous.ca", "trpro-slurm1.ts.watonomous.ca",
          "tr-slurm2.cluster.watonomous.ca", "tr-slurm2.ts.watonomous.ca",
          "thor-slurm1.cluster.watonomous.ca", "thor-slurm1.ts.watonomous.ca"]

