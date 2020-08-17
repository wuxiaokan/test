# coding:utf-8
import requests
import time
from inter_test import UpRedis
host = "http://47.101.168.243:89/rest/act/exam/request?groupId=6641513969838329864"

header = {'Content-Type': 'application/json;charset=UTF-8',
           'Authorization': 'Bearer 3 eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyYW5kb20iOiJiUlYwR1RrMkEyTjJyemttIiwiaWQiOiI2Njk4Nzc0OTUyNjM3NzY3NjgwIiwiaXNzIjoiMjU4NzYuY29tIiwiZXhwIjoxNTk3OTU4NDA1fQ._AKdQ3RsW32c951V20XjXswc0rCiwxuoZhD2B-oZDYQ',
          'sycm': '1_1597112406927_e2c61'
          }

r = requests.get(url=host, headers=header)
t = time.time()*1000
re = r.json()
print(r.status_code)
print(re)
host1 = 'http://47.101.168.243:89/rest/act/exam/mark'

a = len(re['dat']['questions'])
answers = []
for i in range(a):
    dict1 = {}
    dict1['exam'] = int(t)+1000*i
    dict1['hand'] = int(t)+1000*(i+1)
    dict1['id'] = re['dat']['questions'][i]['id']
    dict1['option'] = re['dat']['questions'][i]['oks']
    dict1['status'] = 2
    answers.append(dict1)


date = {'deviceId': "",
        'exam': int(t),
        'hand': int(t)+1000,
        'id': re['dat']['id'],
        'status': 1,
        'type': 1,
        'answers': answers}

re1 = requests.post(url=host1, headers=header, json=date)
result = re1.json()
print(result)

# 清Redis缓存
UpRedis.delete_rs()

