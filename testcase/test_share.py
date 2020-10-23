# coding:utf-8
from inter_test import head, interway
import time
import requests
import allure
from util import logtest
import pytest

header = head.Headers
hd = header.headinfo()

inter = interway.InterWay
logger = logtest.logger

@allure.feature("分享接口")
class TestTabs(object):
    # detail
    @staticmethod
    @allure.story("detail接口")
    def test_detail():
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
    @allure.story("share")
    def test_share():
        # 取shareId列表
        time.sleep(1)
        shareId = TestTabs.test_detail()
        length = len(shareId)
        for i in range(length):
            print(i + 1)
            url = 'http://192.168.3.155/rest/share?id=%s&channel=4&action=share.group' % shareId[i]
            shareInfo = inter.get(url, hd)
            time.sleep(0.5)
            assert shareInfo['err'] == '00000'
            logger.info("err"+shareInfo['err'])


if __name__ == '__main__':
    TestTabs.test_share()
