import redis
from app.core.config import REDIS_URL

r = redis.Redis.from_url(REDIS_URL)

def cache_get(key):
    return r.get(key)

def cache_set(key, value, ttl=3600):
    r.set(key, value, ex=ttl)
