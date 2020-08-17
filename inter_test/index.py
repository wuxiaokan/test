# coding:utf-8
import time

from inter_test import head
from inter_test import interway

# 调用头部信息头部信息
h = head.Headers
hd = h.headinfo()

# 调用接口方法
inter = interway.InterWay


class Interface(object):
    # pick接口
    @staticmethod
    def handerpick():
        print('pick:')
        url = 'http://192.168.3.155/rest/home/data/handpick?mp=true'
        info = inter.get(url, hd)
        assert info['err'] == '00000'

    # button接口
    @staticmethod
    def button():
        print('button:')
        url = 'http://192.168.3.155/rest/home/bottom'
        info = inter.get(url, hd)
        assert info['err'] == '00000'

    # tabs接口
    @staticmethod
    def tabs():
        print('tabs:')
        url = 'http://192.168.3.155/rest/home/data/tabs?mp=true'
        info = inter.get(url, hd)
        return info
        assert info['err'] == '00000'

    # invite接口
    @staticmethod
    def invite():
        print('invite:')
        url = 'http://192.168.3.155/rest/share/invite?channel=4'
        info = inter.get(url, hd)
        assert info['err'] == '00000'

    # detail
    @staticmethod
    def detail():
        info = Interface.tabs()
        length = len(info['dat'])
        for i in range(length):
            print(info['dat'][i]['label'], ':')
            tabId = info['dat'][i]['tabId']
            url = 'http://192.168.3.155/rest/home/data/detail?tabId=%s' % tabId
            inter.get(url, hd)

            time.sleep(1)

        assert info['err'] == '00000'




if __name__ == '__main__':
    Interface.handerpick()
    Interface.tabs()
    Interface.invite()
    Interface.button()
    Interface.detail()

