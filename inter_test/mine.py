# coding:utf-8
from inter_test import head
from inter_test import interway
from time import sleep
from util import phone, name
import random, requests

# 调用头部信息头部信息
h = head.Headers
hd = h.headinfo()

# 调用接口方法
inter = interway.InterWay

# 随机生成一个手机号
phoneNumber = phone.create_phone()
# 随机生成一个名字
rename = name.names()


class Mine(object):
    # 我的-profile(身份认证)
    @staticmethod
    def profile():
        url = 'http://192.168.3.155/rest/user/profile'
        print('profile:')
        info = inter.get(url, hd)
        assert info['err'] == '00000'

    # 我的-config
    @staticmethod
    def config():
        print('config:')
        url = 'http://192.168.3.155/rest/user/miniprogram/lucky/config'
        info = inter.get(url, hd)
        return info
        assert info['err'] == '00000'

    # 我的-幸运大抽奖-sponsor(底部声明)
    @staticmethod
    def sponsor():
        print('sponsor')
        url = 'http://192.168.3.155/rest/act/enter/theme/sponsor'
        info = inter.get(url, hd)
        assert info['err'] == '00000'

    # 我的-幸运大抽奖-rule(规则)
    @staticmethod
    def rule():
        print('rule')
        url = 'http://192.168.3.155/rest/user/miniprogram/lucky/rule'
        info = inter.get(url, hd)
        assert info['err'] == '00000'

    # 取config中actId
    @staticmethod
    def get_actId():
        config = Mine.config()
        actId = config['dat']['activityId']
        return actId

    # 我的-幸运大抽奖-detail(奖品列表)
    @staticmethod
    def detail():
        # 调用get_actId
        actId = Mine.get_actId()
        print('detail')
        url = 'http://192.168.3.155/rest/user/miniprogram/lucky/detail?act=%s' % actId
        info = inter.get(url, hd)
        assert info['err'] == '00000'

    # 我的-我的奖品 status=1未使用，2已使用,4使用中；
    @staticmethod
    def prizes():
        status = [1, 2, 4]
        for i in range(3):
            print(status[i], ':')
            url = 'http://192.168.3.155/rest/user/miniprogram/prizes?status=%s&page=0&pageSize=10' % status[i]
            info = inter.get(url, hd)
            sleep(0.5)
            assert info['err'] == '00000'

    # 我的-我的道具
    @staticmethod
    def prop():
        url = 'http://192.168.3.155/rest/user/prop/list'
        info = inter.get(url, hd)
        assert info['err'] == '00000'

    # 我的-我的收货地址
    @staticmethod
    def addressList():
        url = 'http://192.168.3.155/rest/user/address/list'
        info = inter.get(url, hd)
        assert info['err'] == '00000'

    # 我的-我的收货地址-添加收货地址
    @staticmethod
    def add_address():

        url = 'http://192.168.3.155/rest/user/address/add'
        data = {
            'city': "110100",
            'cityName': "北京市",
            'county': "110106",
            'countyName': "丰台区",
            'detail': "三里屯",
            'isDefault': 1,
            'province': "11",
            'provinceName': "北京市",
            'userName': rename,
            'userPhone': phoneNumber
        }
        info = inter.post(url=url, headers=hd, json=data)
        assert info['err'] == '00000'

    # 我的-我的收货地址-编辑收货地址
    @staticmethod
    def modify_address():
        # 获取收货地址列表以json格式返回
        url1 = 'http://192.168.3.155/rest/user/address/list'
        r = requests.get(url=url1, headers=hd)
        addressList = r.json()

        # 列表a用来存储收货地址列表中的id
        a = []
        length = len(addressList['dat'])
        for i in range(length):
            a.append(addressList['dat'][i]['id'])
        # 随机获取列表a中的数据
        b = random.choice(a)
        url = 'http://192.168.3.155/rest/user/address/modify'
        data = {
            'city': "110100",
            'cityName': "北京市",
            'county': "110101",
            'countyName': "东城区",
            'detail': "三里屯",
            'userName': rename,
            'id': b,
            'isDefault': 0,
            'province': "11",
            'provinceName': "北京市",
            'userPhone': phoneNumber
        }
        info = inter.post(url=url, headers=hd, json=data)
        assert info['err'] == '00000'

    # 我的-我的收货地址-删除收货地址
    @staticmethod
    def delete():
        # 获取收货地址列表以json格式返回
        url1 = 'http://192.168.3.155/rest/user/address/list'
        r = requests.get(url=url1, headers=hd)
        addressList = r.json()

        # 列表a用来存储收货地址列表中的id
        a = []
        length = len(addressList['dat'])
        for i in range(length):
            a.append(addressList['dat'][i]['id'])
        # 随机获取列表a中的数据
        b = random.choice(a)
        url = 'http://192.168.3.155/rest/user/address/delete?addressId=%s' % b
        info = inter.get(url, hd)
        assert info['err'] == '00000'


if __name__ == '__main__':
    # Mine.sponsor()
    # Mine.profile()
    # Mine.detail()
    Mine.modify_address()
