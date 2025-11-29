# Penetration Testing Toolkit (PenToolkit)

A lightweight, modular Python toolkit for basic penetration testing tasks. Designed for security professionals, ethical hackers, and penetration testers to perform authorized security assessments.

## 📋 Table of Contents

1. [Features](#features)
2. [Project Description](#project-description)
3. [Installation](#installation)
4. [Quick Start](#quick-start)
5. [Commands & Usage](#commands--usage)
6. [Modules](#modules)
7. [Project Structure](#project-structure)
8. [Development Commands](#development-commands)
9. [Safety & Ethics](#safety--ethics)
10. [License](#license)

---

## 🎯 Features

- **Port Scanner** – Fast TCP port scanning with concurrent worker threads
- **HTTP Brute-Forcer** – Wordlist-based HTTP Basic Auth credential testing
- **CLI Interface** – Easy-to-use command-line interface with subcommands
- **Modular Design** – Import modules directly in Python scripts
- **Configurable** – Adjustable timeouts, worker threads, and retry logic

---

## 📖 Project Description

**PenToolkit** is a Python-based penetration testing framework that provides security testing capabilities in a lightweight package. It includes:

1. **Port Scanner** – Identifies open TCP ports on target systems
2. **Brute-Forcer** – Attempts to crack HTTP Basic Authentication
3. **CLI Tool** – Command-line interface for easy access
4. **Python API** – Direct module imports for custom scripts

This toolkit is designed for **authorized security testing only** on systems you own or have explicit permission to test.

---

## 📥 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (optional, for cloning)

### Step 1: Download the Project

**Option A: Clone from GitHub**
```powershell
git clone https://github.com/Jaynavghane/pentoolkit.git
cd pentoolkit
```

**Option B: Download ZIP**
```powershell
# Download from GitHub and extract
Expand-Archive pentoolkit-main.zip
cd pentoolkit-main
```

### Step 2: Create Virtual Environment

```powershell
# Create virtual environment
python -m venv .venv

# Activate virtual environment (Windows PowerShell)
.\.venv\Scripts\Activate.ps1

# Activate virtual environment (Windows CMD)
.\.venv\Scripts\activate.bat

# Activate virtual environment (Linux/Mac)
source .venv/bin/activate
```

### Step 3: Install Dependencies

```powershell
# Install required packages
pip install -r requirements.txt

# Or install in editable mode for development
pip install -e .
```

### Step 4: Verify Installation

```powershell
# Test the toolkit
python -m pentoolkit --help
```

---

## 🚀 Quick Start

### Port Scanner Example

```powershell
# Scan ports 1-1024 on localhost
python -m pentoolkit portscan --host 127.0.0.1 --start 1 --end 1024

# Scan specific ports on remote host
python -m pentoolkit portscan --host example.com --start 80 --end 443
```

### Brute-Forcer Example

```powershell
# Attempt to crack HTTP Basic Auth
python -m pentoolkit bruteforce --url http://localhost:8080/admin --username admin --wordlist passwords.txt
```

---

## 💻 Commands & Usage

### Port Scanner Command

**Syntax:**
```powershell
python -m pentoolkit portscan [OPTIONS]
```

**Required Options:**
- `--host` – Target hostname or IP address

**Optional Options:**
- `--start` (default: 1) – Starting port number
- `--end` (default: 1024) – Ending port number
- `--timeout` (default: 1.0) – Socket timeout in seconds
- `--workers` (default: 100) – Number of concurrent worker threads

**Examples:**
```powershell
# Basic port scan
python -m pentoolkit portscan --host 127.0.0.1

# Scan specific port range
python -m pentoolkit portscan --host example.com --start 80 --end 443

# Scan with custom timeout and workers
python -m pentoolkit portscan --host 192.168.1.1 --start 1 --end 10000 --timeout 2.0 --workers 200

# Help
python -m pentoolkit portscan --help
```

### Brute-Force Command

**Syntax:**
```powershell
python -m pentoolkit bruteforce [OPTIONS]
```

**Required Options:**
- `--url` – Target URL requiring HTTP Basic Auth
- `--username` – Username to attempt
- `--wordlist` – Path to password wordlist file

**Optional Options:**
- `--timeout` (default: 5.0) – Request timeout in seconds

**Examples:**
```powershell
# Basic brute-force
python -m pentoolkit bruteforce --url http://localhost:8080/admin --username admin --wordlist passwords.txt

# With custom timeout
python -m pentoolkit bruteforce --url http://example.com/login --username root --wordlist wordlist.txt --timeout 10.0

# Help
python -m pentoolkit bruteforce --help
```

### Create Wordlist File

**PowerShell:**
```powershell
@"
password
123456
admin
admin123
letmein
welcome
password123
"@ | Out-File -FilePath wordlist.txt -Encoding UTF8
```

**CMD:**
```cmd
(
echo password
echo 123456
echo admin
echo admin123
) > wordlist.txt
```

---

## 🔧 Modules

### Port Scanner Module (`pentoolkit/port_scanner.py`)

**Description:** Performs concurrent TCP port scanning

**Functions:**
- `scan_port(host, port, timeout=1.0)` – Scan single port
- `scan_ports(host, ports, timeout=1.0, workers=100)` – Scan multiple ports

**Python Usage:**
```python
from pentoolkit.port_scanner import scan_ports

# Scan ports 1-1024
open_ports = scan_ports("127.0.0.1", range(1, 1025), timeout=1.0, workers=100)
print("Open ports:", open_ports)
```

### Brute-Forcer Module (`pentoolkit/brute_forcer.py`)

**Description:** Tests HTTP Basic Authentication with wordlist

**Functions:**
- `try_basic_auth(url, username, passwords, timeout=5.0)` – Attempt authentication

**Python Usage:**
```python
from pentoolkit.brute_forcer import try_basic_auth

passwords = ["admin123", "password", "test123"]
found, response = try_basic_auth(
    "http://localhost:8080/protected",
    "admin",
    passwords
)

if found:
    print(f"✓ Password found: {found}")
else:
    print("✗ No password matched")
```

### CLI Module (`pentoolkit/cli.py`)

**Description:** Command-line interface handler

**Functions:**
- `main(argv=None)` – Main entry point

**Python Usage:**
```python
from pentoolkit.cli import main

# Run from Python
main(['portscan', '--host', '127.0.0.1', '--end', '100'])
```

### Utilities Module (`pentoolkit/utils.py`)

**Description:** Helper functions

**Functions:**
- `resolve_host(host)` – Resolve hostname to IP address

**Python Usage:**
```python
from pentoolkit.utils import resolve_host

ip = resolve_host("example.com")
print(f"IP: {ip}")
```

---

## 📁 Project Structure

```
pentoolkit/
├── __init__.py              # Package initialization
├── __main__.py              # Entry point (python -m pentoolkit)
├── cli.py                   # Command-line interface
├── port_scanner.py          # TCP port scanning module
├── brute_forcer.py          # HTTP Basic Auth brute-force
└── utils.py                 # Utility functions

docs/
└── USAGE.md                 # Detailed usage documentation

examples/
└── quick_start.py           # Example usage script

tests/
└── README.md                # Testing guidelines

.gitignore                   # Git ignore patterns
pyproject.toml               # Project metadata & config
requirements.txt             # Python dependencies
passwords.txt                # Sample password wordlist
README.md                    # This file
```

---

## ⚙️ Development Commands

### Setup Development Environment

```powershell
# Clone repository
git clone https://github.com/Jaynavghane/pentoolkit.git
cd pentoolkit

# Create virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Install development dependencies
pip install -e ".[dev]"
```

### Run Tests

```powershell
# Run all tests
python -m pytest tests/

# Run with coverage
python -m pytest --cov=pentoolkit tests/
```

### Code Formatting

```powershell
# Format code with black
black pentoolkit/

# Check code style
flake8 pentoolkit/
```

### Git Commands Used in Creation

```powershell
# Initialize git repository
git init

# Stage files
git add .

# Commit changes
git commit -m "Initial commit: pentoolkit scaffold"

# Add remote repository
git remote add origin https://github.com/Jaynavghane/pentoolkit.git

# Set branch name
git branch -M main

# Push to GitHub
git push -u origin main

# View commit history
git log --oneline
```

### Build & Distribution

```powershell
# Build package
python -m build

# Install locally
pip install -e .

# Upload to PyPI (requires credentials)
twine upload dist/*
```

---

## 🔒 Safety & Ethics

**⚠️ IMPORTANT:**

- **Only use this toolkit on systems you own or have explicit written authorization to test**
- Unauthorized access to computer systems is illegal in most jurisdictions
- Always follow applicable laws, regulations, and ethical guidelines
- Respect privacy and confidentiality of data
- Use for legitimate security testing and educational purposes only
- Disclaimer: Authors are not responsible for misuse

---

## 📦 Dependencies

- **requests** (≥2.25.0) – HTTP library for brute-forcing
- **setuptools** (≥45) – Build system
- **wheel** – Python packaging

**Development Dependencies:**
- pytest – Unit testing
- pytest-cov – Code coverage
- black – Code formatting
- flake8 – Style checker

---

## 🤝 Contributing

To contribute improvements:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit changes (`git commit -am "Add feature"`)
4. Push to branch (`git push origin feature/improvement`)
5. Open a Pull Request

---

## 📝 purpose

Educational and internship project for authorized security testing only.

----------------------------------------------------------------

## Output
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/5e97db9f-4bc5-45d4-8c92-44a44625fc59" />


----------------------------------------------

## 🎓 Learning Resources

- **Port Scanning:** https://en.wikipedia.org/wiki/Port_scanner
- **HTTP Authentication:** https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication
- **Ethical Hacking:** https://www.comptia.org/certifications/security
- **Python Security:** https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/

---

## ✉️ Support

For issues or questions:
1. Check existing GitHub issues
2. Review documentation in `docs/USAGE.md`
3. Create a new GitHub issue with details

---

**Last Updated:** November 29, 2025  
**Version:** 0.1.0  
**Author:** 
* Company: CODTECH IT SOLUTIONS
* Name: Jay Navghane
* Intern ID: COD08111
* Domain: Cyber security & Ethical Hacking
* Duration: 6 weeks
* Mentor: Neela Santosh


