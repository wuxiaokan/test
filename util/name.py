# coding:utf-8
import random as r


def names():
    a = ['张', '李', '王', '赵', '金', '胡', '飞']
    b = ['明', '小', '龙', '浩', '六', '芳', '军', '琳', '飞']
    c = ['力', '建', '', '国', '杰', '宏', '顺', '嘎', '拉', '']

    name = r.choice(a) + r.choice(b) + r.choice(c)
    return name

