# coding:utf-8
from io import StringIO, BytesIO

# 打开文件
with open('C:/Users/Administrator.SC-201907251023/Desktop/test.txt', 'r') as f:
    data = f.read()
    print(data)
# StringIO
# 写入
a = StringIO()
a.write('hello ')
a.write('world')

b = a.getvalue()  # getvalue()方法用于获得写入后的str。
print(b)

# 读取
c = StringIO('哈喽，哈哈哈')
d = c.readline()
print(d)

# BytesIO 转换成二进制
e = BytesIO()
e.write('中国'.encode('utf-8'))
print(e.getvalue())

f = BytesIO(b'\xe4\xb8\xad\xe5\x9b\xbd')
f.read()
print(f)
