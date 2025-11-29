"""Command-line interface for pentoolkit."""
import argparse
from pathlib import Path
from .port_scanner import scan_ports
from .brute_forcer import try_basic_auth


def _cmd_portscan(args):
    """Execute port scan command."""
    host = args.host
    start = args.start
    end = args.end
    ports = range(start, end + 1)
    print(f"[*] Scanning {host} ports {start}-{end}...")
    open_ports = scan_ports(host, ports, timeout=args.timeout, workers=args.workers)
    if open_ports:
        print(f"[+] Open ports: {', '.join(map(str, open_ports))}")
    else:
        print("[-] No open ports found in range.")


def _cmd_bruteforce(args):
    """Execute brute-force command."""
    url = args.url
    username = args.username
    wordlist = Path(args.wordlist)
    if not wordlist.exists():
        print(f"[-] Wordlist not found: {wordlist}")
        return
    print(f"[*] Attempting HTTP Basic Auth on {url} as {username}...")
    with wordlist.open() as fh:
        passwords = (line.strip() for line in fh)
        found, resp = try_basic_auth(url, username, passwords, timeout=args.timeout)
        if found:
            print(f"[+] Success! username={username} password={found}")
        else:
            print("[-] No valid password found in wordlist.")


def main(argv=None):
    """Main entry point."""
    parser = argparse.ArgumentParser(
        prog="pentoolkit",
        description="Penetration Testing Toolkit"
    )
    sub = parser.add_subparsers(dest="cmd")

    # Port scanner command
    ps = sub.add_parser("portscan", help="Scan TCP ports on a host")
    ps.add_argument("--host", required=True, help="Target hostname or IP")
    ps.add_argument("--start", type=int, default=1, help="Starting port (default: 1)")
    ps.add_argument("--end", type=int, default=1024, help="Ending port (default: 1024)")
    ps.add_argument("--timeout", type=float, default=1.0, help="Socket timeout (default: 1.0s)")
    ps.add_argument("--workers", type=int, default=100, help="Worker threads (default: 100)")
    ps.set_defaults(func=_cmd_portscan)

    # Brute-force command
    bf = sub.add_parser("bruteforce", help="Brute-force HTTP Basic Auth")
    bf.add_argument("--url", required=True, help="Target URL")
    bf.add_argument("--username", required=True, help="Username to attempt")
    bf.add_argument("--wordlist", required=True, help="Path to password wordlist")
    bf.add_argument("--timeout", type=float, default=5.0, help="Request timeout (default: 5.0s)")
    bf.set_defaults(func=_cmd_bruteforce)

    args = parser.parse_args(argv)
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
