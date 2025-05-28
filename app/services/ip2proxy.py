import ip2proxy
from app.core.config import IP2PROXY_DB_PATH

_reader = ip2proxy.IP2Proxy(IP2PROXY_DB_PATH)

def check_proxy(ip):
    return _reader.get_all(ip)
