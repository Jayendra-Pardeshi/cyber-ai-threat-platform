import redis
from config.settings import settings

redis_client = redis.Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    decode_responses=True
)

def save_chat(user_id, message):
    redis_client.rpush(user_id, message)

def get_chat(user_id):
    return redis_client.lrange(user_id, 0, -1)