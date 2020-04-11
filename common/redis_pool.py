import redis

# try:
# Pool = redis.ConnectionPool(host='192.168.1.112', port=8003, max_connections=1000, password='aiator_zhisheng')
Pool = redis.ConnectionPool(host='192.168.1.197', port=6379, db=3, max_connections=1000,)
# except ConnectionError:
