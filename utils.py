"""Utility helpers for pentoolkit."""
import socket


def resolve_host(host: str) -> str:
    """Resolve hostname to IP address (returns input if already an IP)."""
    try:
        return socket.gethostbyname(host)
    except Exception:
        return host
