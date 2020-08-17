import redis


def delete_rs():
    ip = '192.168.3.155'
    pw = 'A2fe37de95456fbc'
    # 连接Redis
    r = redis.Redis(host=ip, password=pw, port=6379, db=3)
    length = len(r.keys('day*'))
    # 清理Redis中关于day的缓存
    for i in range(length):
        r.delete(r.keys('day*')[0])
