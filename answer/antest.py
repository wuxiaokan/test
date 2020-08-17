import requests
import time
import threading

host = "http://47.101.168.243:89/rest/act/exam/request?groupId=70"
host1 = 'http://47.101.168.243:89/rest/act/exam/mark'
header = {'Content-Type': 'application/json;charset=UTF-8',
          'Authorization': 'Bearer 3 eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyYW5kb20iOiJiUlYwR1RrMkEyTjJyemttIiwiaWQiOiI2Njk4Nzc0OTUyNjM3NzY3NjgwIiwiaXNzIjoiMjU4NzYuY29tIiwiZXhwIjoxNTk3OTU4NDA1fQ._AKdQ3RsW32c951V20XjXswc0rCiwxuoZhD2B-oZDYQ',
          'sycm': '1_1597112406927_e2c61'
          }


def answer():
    r = requests.get(url=host, headers=header)
    return r.json()



re = answer()

print(re)
def answers():
    ti = time.time()
    a = len(re['dat']['questions'])
    answers = []
    for i in range(a):
        dict1 = {}
        dict1['exam'] = int(ti) + 1000 * i
        dict1['hand'] = int(ti) + 1000 * (i + 1)
        dict1['id'] = re['dat']['questions'][i]['id']
        dict1['option'] = re['dat']['questions'][i]['oks']
        dict1['status'] = 2
        answers.append(dict1)
    return answers


def open():
    t = time.time() * 1000

    date = {'deviceId': "",
            'exam': int(t),
            'hand': int(t) + 1000,
            'id': re['dat']['id'],
            'status': 1,
            'type': 1,
            'answers': answers()}

    re1 = requests.post(url=host1, headers=header, json=date)
    result = re1.json()
    print("result:", result)
    return result


def get_time_ms():
    ct = time.time()  # 时间戳
    local_time = time.localtime(ct)  # 本地化时间
    cart_time_strftime = time.strftime("%Y-%m-%d %H:%M:%S", local_time)  # 格式化时间
    cart_time_strftime_ms = (ct - int(ct)) * 1000
    ms = "%s.%03d" % (cart_time_strftime, cart_time_strftime_ms)
    return ms


if __name__ == '__main__':
    threads = []
    for i in range(0, 5):
        s = threading.Thread(target=open, args=())  # 把请求函数加入多线程中去
        threads.append(s)
    print(threads)
    for t in threads:
        #t.setDaemon(True)  # 把多线程设置为守护线程
        t.start()  # 开始执行多线程
        print(('%s 执行时间为 %s') % (t, get_time_ms()))  # 输出执行时间
    #t.join()  # 阻塞主线程执行
    print("all over %s" % get_time_ms())
    exit()
