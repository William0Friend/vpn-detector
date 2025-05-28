from fastapi import APIRouter, Query
from app.services.ip2proxy import check_proxy
from app.services.geoip import lookup_asn
from app.services.whois_lookup import lookup_whois

router = APIRouter()

@router.get("/intel")
async def get_intel(ip: str = Query(...)):
    return {
        "proxy": check_proxy(ip),
        "asn": lookup_asn(ip),
        "whois": lookup_whois(ip)
    }
