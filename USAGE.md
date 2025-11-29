# Usage Guide

## Port Scanner

Scan TCP ports on a target host with concurrency:

```bash
python -m pentoolkit portscan --host 127.0.0.1 --start 1 --end 1024
```

**Options:**
- `--host` (required) – Target hostname or IP
- `--start` (default: 1) – Starting port number
- `--end` (default: 1024) – Ending port number
- `--timeout` (default: 1.0) – Socket timeout in seconds
- `--workers` (default: 100) – Number of concurrent worker threads

## Brute-Forcer (HTTP Basic Auth)

Attempt to crack HTTP Basic Auth credentials:

```bash
python -m pentoolkit bruteforce --url http://localhost:8080/protected --username admin --wordlist passwords.txt
```

**Options:**
- `--url` (required) – Target URL requiring Basic Auth
- `--username` (required) – Username to attempt
- `--wordlist` (required) – Path to password wordlist file (one per line)
- `--timeout` (default: 5.0) – Request timeout in seconds

## Direct Module Usage

### Port Scanner

```python
from pentoolkit.port_scanner import scan_ports

open_ports = scan_ports("example.com", range(1, 1025), timeout=1.0, workers=100)
print("Open ports:", open_ports)
```

### Brute-Forcer

```python
from pentoolkit.brute_forcer import try_basic_auth

passwords = ["admin123", "password", "test123"]
found_password, response = try_basic_auth(
    "http://example.com/protected",
    "admin",
    passwords
)

if found_password:
    print(f"Success! Password: {found_password}")
```

## Safety & Ethics

⚠️ **IMPORTANT:**

- Only use on targets you **own or have explicit written permission** to test
- Unauthorized access is **illegal** in most jurisdictions
- Always follow applicable laws and organizational policies
- This toolkit is for **educational and authorized security testing only**
