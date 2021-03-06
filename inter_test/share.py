# coding:utf-8
from inter_test import head, interway
import time
import requests

header = head.Headers
hd = header.headinfo()

inter = interway.InterWay


class Tabs(object):
    # detail
    @staticmethod
    def detail():
        url = 'http://192.168.3.155/rest/home/data/tabs?mp=true'
        r = requests.get(url, hd)
        info = r.json()
        length = len(info['dat'])
        b = []
        for i in range(length):
            tabId = info['dat'][i]['tabId']
            url1 = 'http://192.168.3.155/rest/home/data/detail?tabId=%s' % tabId
            r = requests.get(url1, hd)
            tap = r.json()
            time.sleep(0.1)
            length1 = len(tap['dat']['contents'][0]['data']['datas'])
            for j in range(length1):
                # 将shareId放入b列表
                b.append(tap['dat']['contents'][0]['data']['datas'][j]['content'])
        return b

    # detail-share
    @staticmethod
    def share():
        # 取shareId列表
        shareId = Tabs.detail()
        length = len(shareId)
        for i in range(length):
            print(i+1)
            url = 'http://192.168.3.155/rest/share?id=%s&channel=4&action=share.group' % shareId[i]
            shareInfo = inter.get(url, hd)
            time.sleep(0.2)
            assert shareInfo['err'] == '00000'


if __name__ == '__main__':
    Tabs.share()
