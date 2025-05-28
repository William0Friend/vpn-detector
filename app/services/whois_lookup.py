from ipwhois import IPWhois

def lookup_whois(ip):
    try:
        obj = IPWhois(ip)
        return obj.lookup_rdap(depth=1)
    except Exception as e:
        return {"error": str(e)}
