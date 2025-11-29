"""Simple TCP port scanner with concurrency."""
import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Iterable, List


def scan_port(host: str, port: int, timeout: float = 1.0) -> bool:
    """Return True if TCP port is open on host."""
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except Exception:
        return False


def scan_ports(host: str, ports: Iterable[int], timeout: float = 1.0, workers: int = 100) -> List[int]:
    """Scan an iterable of ports and return sorted list of open ports.

    Args:
        host: hostname or IP address
        ports: iterable of port numbers
        timeout: socket timeout in seconds
        workers: maximum concurrent worker threads

    Returns:
        Sorted list of open port numbers
    """
    open_ports = []
    ports = list(ports)
    with ThreadPoolExecutor(max_workers=min(workers, len(ports) or 1)) as ex:
        future_to_port = {ex.submit(scan_port, host, p, timeout): p for p in ports}
        for fut in as_completed(future_to_port):
            p = future_to_port[fut]
            try:
                if fut.result():
                    open_ports.append(p)
            except Exception:
                pass
    return sorted(open_ports)
