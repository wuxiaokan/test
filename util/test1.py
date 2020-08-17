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


def answers():
    ti = time.time()
    a = len(re['dat']['questions'])
    answers1 = []
    for i in range(a):
        dict1 = {}
        dict1['exam'] = int(ti) + 1000 * i
        dict1['hand'] = int(ti) + 1000 * (i + 1)
        dict1['id'] = re['dat']['questions'][i]['id']
        dict1['option'] = re['dat']['questions'][i]['oks']
        dict1['status'] = 2
        answers1.append(dict1)
    return answers1


def open():
    t = time.time() * 1000
    date = {'deviceId': "",
            'exam': int(t),
            'hand': int(t) + 1000,
            'id': re['dat']['id'],
            'status': 1,
            'type': 1,
            'answers': answers()}
    i = 0
    while i < 5:
        re1 = requests.post(url=host1, headers=header, json=date)
        result = re1.json()
        print("result:", result)
        i = i + 1


t = threading.Thread(target=open, name='openThread')
t.start()
t.join()
