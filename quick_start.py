"""Quick start example – direct module usage."""
from pentoolkit.port_scanner import scan_ports
from pentoolkit.brute_forcer import try_basic_auth

if __name__ == "__main__":
    # Example 1: Port scan localhost
    print("[*] Example 1: Port Scanner")
    print("Scanning common ports on 127.0.0.1...")
    host = "127.0.0.1"
    ports = list(range(1, 1025))
    open_ports = scan_ports(host, ports, timeout=0.5, workers=200)
    if open_ports:
        print(f"[+] Open ports: {open_ports}")
    else:
        print("[-] No open ports found.")

    # Example 2: Brute-force (commented – do NOT run against remote targets without permission)
    print("\n[*] Example 2: HTTP Basic Auth Brute-Force (commented out)")
    # url = "http://localhost:8080/protected"
    # username = "admin"
    # with open('examples/wordlist_sample.txt') as fh:
    #     pwds = [p.strip() for p in fh if p.strip()]
    # found, response = try_basic_auth(url, username, pwds)
    # if found:
    #     print(f"[+] Found password: {found}")
