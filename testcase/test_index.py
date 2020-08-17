# coding:utf-8
import time
import allure
import pytest

from inter_test import head
from inter_test import interway

# 调用头部信息头部信息
h = head.Headers
hd = h.headinfo()

# 调用接口方法
inter = interway.InterWay


@allure.feature("测试index接口")
class TestInterface(object):
    # pick接口
    @staticmethod
    @allure.story("pick接口")
    def test_handerpick():
        print('pick:')
        url = 'http://192.168.3.155/rest/home/data/handpick?mp=true'
        info = inter.get(url, hd)
        assert info['err'] == '00000'

    # button接口
    @staticmethod
    @allure.story("button接口")
    def test_button():
        print('button:')
        url = 'http://192.168.3.155/rest/home/bottom'
        info = inter.get(url, hd)
        assert info['err'] == '00000'

    # tabs接口
    @staticmethod
    @allure.story("tabs接口")
    def test_tabs():
        print('tabs:')
        url = 'http://192.168.3.155/rest/home/data/tabs?mp=true'
        info = inter.get(url, hd)
        return info
        assert info['err'] == '00000'

    # invite接口
    @staticmethod
    @allure.story("invite接口")
    def test_invite():
        print('invite:')
        url = 'http://192.168.3.155/rest/share/invite?channel=4'
        info = inter.get(url, hd)
        assert info['err'] == '00000'

    # detail
    @staticmethod
    @allure.story("detail接口")
    def test_detail():
        time.sleep(1)
        info = TestInterface.test_tabs()
        length = len(info['dat'])
        for i in range(length):
            print(info['dat'][i]['label'], ':')
            tabId = info['dat'][i]['tabId']
            url = 'http://192.168.3.155/rest/home/data/detail?tabId=%s' % tabId
            inter.get(url, hd)
            time.sleep(1)

        assert info['err'] == '00000'


if __name__ == '__main__':
    TestInterface.test_handerpick()
    TestInterface.test_tabs()
    TestInterface.test_invite()
    TestInterface.test_button()
    TestInterface.test_detail()
