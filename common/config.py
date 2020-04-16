
machine_num = 2
# 企业应用ID
agent_id = 677118324
# APP_KEY
appkey = r"ding0qsys3hwvuehgm3y"
appsecret = r"Kj_irB0mNvxffh7zbwSMt-nEyKIG_9AueII0QfEn2G5drg_OO5qxw0cp5cx - KYGz"
corpId="dingaa331c200723006a35c2f4657eb6378f"

secret_key = "zhishengzhihuigongchang"
salt = "aiator"


# REDIS_HOST = '192.168.1.196'
# REDIS_PORT = 6379

REDIS_HOST = 'test.aiator.com'
REDIS_PORT = 9003
REDIS_DB = 0
REDIS_PASSWORD = 'aiator_zhisheng'
LOCATION = "redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}".format(REDIS_HOST=REDIS_HOST,
                                                                 REDIS_PORT=REDIS_PORT,
                                                                 REDIS_DB=REDIS_DB)