import geoip2.database
from app.core.cache import cache_get, cache_set

reader = geoip2.database.Reader('GeoLite2-ASN.mmdb')

def lookup_asn(ip):
    cached = cache_get(f"asn:{ip}")
    if cached:
        return cached.decode()
    try:
        response = reader.asn(ip)
        result = {"asn": response.autonomous_system_number, "org": response.autonomous_system_organization}
        cache_set(f"asn:{ip}", str(result))
        return result
    except:
        return {"error": "Lookup failed"}
