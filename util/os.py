import os

'''
# 查看操作系统
print(os.name)

# 查看操作系统中定义的环境变量
print(os.environ)

# 获取某个环境变量的值
print(os.environ.get('PATH'))

# 查看当前目录的绝对路径:
a = os.path.abspath('.')
print(a)

# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
os.path.join('C:/Users/Administrator.SC-201907251023/Desktop', 'test')
# 然后创建一个目录:
os.mkdir('C:/Users/Administrator.SC-201907251023/Desktop/test')
# 删除一个目录：
os.rmdir('C:/Users/Administrator.SC-201907251023/Desktop/test')

# 列出当前目录下所有的文件
b = [x for x in os.listdir('.') if os.path.isdir(x)]
print(b)

# 列出当前目录下所有的.py文件
c = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
print(c)


# 序列化
import pickle

d = dict(name='Bob', age=20, score=88)
# pickle.dumps()方法把任意对象序列化成一个bytes
pickle.dumps(d)
# pickle.dump()直接把对象序列化后写入
f = open('C:/Users/Administrator.SC-201907251023/Desktop/test.txt', 'wb')
pickle.dump(d, f)
f.close()

# 反序列化
f = open('C:/Users/Administrator.SC-201907251023/Desktop/test.txt', 'rb')
d = pickle.load(f)
f.close()

'''
import json
# 以json格式返回
d = dict(name='Bob', age=20, score=88)
a = json.dumps(d)
print(a)
