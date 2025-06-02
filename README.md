# 🧠 WATCloud CLI

A Python-based command-line interface for inspecting user-specific resource usage and daemon status on WATCloud systems.

---

## 📦 Features

- View disk, memory, and CPU quota usage in a human-readable format
- List user daemons such as Docker rootless or Jupyter
- Works locally or when connected to a WATCloud server (e.g., via SSH)
- Lightweight and dependency-minimal

---

## 🚀 Setup & Installation

> ⚠️ Python 3.12+ recommended

1. **Clone the repository**:
```bash
   git clone https://github.com/LA-10/watcloud-cli.git
   cd watcloud-cli
```

2. **(Optional) Connect to a virtual environment**:
```bash
   python3 -m venv venv
   source venv/bin/activate
```

3. **Install the CLI in editable mode**:
```bash
   pip install -e .
```

## 💻 Usage
Once installed, you can run the CLI like this:
   `watcloud <command> <subcommand>`

## 🧭 WatCloud CLI – Command Overview

Below are all available top-level commands and their subcommands, organized in separate tables.

💡 **Tip:** You can type `watcloud -h` or `watcloud <command> -h` to see detailed help for any command or subcommand.

---

### 🔧 `watcloud status`

| Subcommand     | Description                                      |
|----------------|--------------------------------------------------|
| *(none)*       | Shows the status of the cluster (up/down/maintenance). |

---

### 📊 `watcloud quota`

| Subcommand     | Description                                      |
|----------------|--------------------------------------------------|
| `list`         | Lists all quota usage (disk, memory, CPU).       |
| `disk`         | Shows your disk usage percentage and free space. |
| `cpu`          | Displays CPU usage percentage.                   |
| `memory`       | Shows memory usage statistics.                   |

---

### 🌀 `watcloud daemon`

| Subcommand     | Description                                      |
|----------------|--------------------------------------------------|
| `status`       | Lists all non-interactive background user processes (daemons). |

---

### 🛠 `watcloud maintenance`

| Subcommand     | Description                                                    |
|----------------|----------------------------------------------------------------|
| `mark <node>`  | Marks a given node as under maintenance (optional `--until`). |
| `remove <node>`| Removes the maintenance flag from a given node.                |
| `check <node>` | Checks whether a specific node is under maintenance.          |

---

💡 **Reminder:**  
Run `watcloud -h`, `watcloud quota -h`, or any `watcloud <command> -h` to see descriptions and usage examples in your terminal.
