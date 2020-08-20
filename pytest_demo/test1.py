# coding:utf-8
'''
import pytest


@pytest.mark.parametrize("test_input,expected",
                         [("3+5", 8),
                          ("2+4", 6),
                          ("6 * 9", 42),
                          ])
def test_eval(test_input, expected):
    assert eval(test_input) == expected


if __name__ == "__main__":
    pytest.main(["-s", "test1.py"])


import pytest


@pytest.fixture(scope="function", autouse=True)
def start(request):
    print('\n-----开始执行function----')


def test_a():
    print("-------用例a执行-------")


class Test_aaa():

    def test_01(self):
        print('-----------用例01--------------')

    def test_02(self):
        print('-----------用例02------------')


if __name__ == "__main__":
    pytest.main(["-s", "test1.py"])



def multiply(a, b):
    """
    fuction: 两个数相乘
    >>> multiply(4, 3)
    12
    >>> multiply('a', 3)
    'aaa'
    >>> multiply(1, 2)
    3
    """
    return a * b


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
'''
import os
print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(os.path.split(os.path.dirname(os.path.abspath(__file__)))[0])
