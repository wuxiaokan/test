# coding:utf-8
class Animal(object):
    def run(self):
        print('run')


class Dog(Animal):
    def eac(self):
        print('eat')
    pass


class Cat(Animal):
    pass


d = Dog()
c = Cat()

d.run()
d.eac()
c.run()

import random
list1 = ['佛山', '南宁', '北海', '杭州', '南昌', '厦门', '温州']
a = random.choice(list1)
print(a)
