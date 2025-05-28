from fastapi import FastAPI
from app.api.v1 import endpoints

app = FastAPI(title="VPNIntel API")
app.include_router(endpoints.router, prefix="/v1")
