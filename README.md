# WATcloud CLI

A command-line interface (CLI) tool to monitor and manage WATcloud cluster services. 

This tool allows users to:

- Check the status of the cluster and its nodes
- View quota usage for disk, CPU, and memory
- Monitor the status of user daemons like Docker rootless

## Features

- `watcloud status`: Check the status of the cluster, including node health and maintenance status.
- `watcloud quota list`: List the user’s current quota usage for disk, CPU, and memory.
- `watcloud daemon status`: Check the status of key user daemons like Docker.

## Installation

To install this tool:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/watcloud-cli.git
   cd watcloud-cli
