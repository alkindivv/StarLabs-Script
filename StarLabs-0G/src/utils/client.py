import primp
from noble_tls import Session, Client
import ssl
import os
import urllib3

# Disable SSL warnings globally
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Set environment variables to disable SSL verification globally
os.environ['PYTHONHTTPSVERIFY'] = '0'
os.environ['CURL_CA_BUNDLE'] = ''
os.environ['REQUESTS_CA_BUNDLE'] = ''

# Monkey patch SSL context to disable verification globally
original_create_default_context = ssl.create_default_context

def create_unverified_context(*args, **kwargs):
    context = original_create_default_context(*args, **kwargs)
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    return context

ssl.create_default_context = create_unverified_context
ssl._create_default_https_context = create_unverified_context


async def create_client(
    proxy: str, skip_ssl_verification: bool = True, chrome_version: int = 131
) -> primp.AsyncClient:
    session = primp.AsyncClient(
        impersonate=f"chrome_{chrome_version}", verify=False  # Always disable SSL verification
    )

    if proxy:
        session.proxy = proxy

    session.timeout = 60

    session.headers.update(HEADERS)

    return session


async def create_insecure_client(proxy: str = "") -> primp.AsyncClient:
    """Create a primp client with SSL verification completely disabled"""
    session = primp.AsyncClient(
        impersonate="chrome_131",
        verify=False  # Disable SSL verification
    )

    if proxy and proxy.strip():
        session.proxy = proxy

    session.timeout = 60

    # Set headers that mimic a real browser
    session.headers.update({
        "accept": "*/*",
        "accept-language": "en-GB,en-US;q=0.9,en;q=0.8,ru;q=0.7,zh-TW;q=0.6,zh;q=0.5",
        "content-type": "application/json",
        "priority": "u=1, i",
        "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    })

    return session


HEADERS = {
    "accept": "*/*",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8,ru;q=0.7,zh-TW;q=0.6,zh;q=0.5",
    "content-type": "application/json",
    "priority": "u=1, i",
    "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
}


import secrets


async def create_twitter_client(proxy: str, auth_token: str) -> Session:
    session = Session(client=Client.CHROME_131)
    session.random_tls_extension_order = True

    # Only set proxy if provided and not empty
    if proxy and proxy.strip():
        session.proxies.update(
            {
                "http": "http://" + proxy,
                "https": "http://" + proxy,
            }
        )

    session.timeout_seconds = 60  # Increased timeout from 30 to 60 seconds

    generated_csrf_token = secrets.token_hex(16)

    cookies = {"ct0": generated_csrf_token, "auth_token": auth_token}
    headers = {"x-csrf-token": generated_csrf_token}

    session.headers.update(headers)
    session.cookies.update(cookies)

    session.headers["x-csrf-token"] = generated_csrf_token

    session.headers = get_headers(session)

    return session


def get_headers(session: Session, **kwargs) -> dict:
    """
    Get the headers required for authenticated requests
    """
    cookies = session.cookies

    headers = kwargs | {
        "authorization": "Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs=1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA",
        # "cookie": "; ".join(f"{k}={v}" for k, v in cookies.items()),
        "referer": "https://x.com/",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "x-csrf-token": cookies.get("ct0", ""),
        # "x-guest-token": cookies.get("guest_token", ""),
        "x-twitter-auth-type": "OAuth2Session" if cookies.get("auth_token") else "",
        "x-twitter-active-user": "yes",
        "x-twitter-client-language": "en",
    }
    return dict(sorted({k.lower(): v for k, v in headers.items()}.items()))
