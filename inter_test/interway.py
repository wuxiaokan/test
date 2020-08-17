# coding:utf-8
import requests


class InterWay:
    # get请求
    @staticmethod
    def get(url, headers):
        r = requests.get(url=url, headers=headers)
        result = r.json()
        print(result)
        return result

    # post请求
    @staticmethod
    def post(url, headers, json):
        r = requests.post(url=url, headers=headers, json=json)
        result = r.json()
        print(result)
        return result
