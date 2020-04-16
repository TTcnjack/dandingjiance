import redis
from common import config
# try:
# Pool = redis.ConnectionPool(host='192.168.1.112', port=8003, max_connections=1000, password='aiator_zhisheng')
Pool = redis.ConnectionPool(host=config.REDIS_HOST, port=config.REDIS_PORT, db=config.REDIS_DB, password=config.REDIS_PASSWORD, max_connections=1000,)
# except ConnectionError:
