# coding:utf-8
import yaml
import os
import json

current_path = os.path.abspath(".")
superior_path = os.path.dirname(current_path) + "\Yaml"


yaml_path = os.path.join(superior_path, 'b.yaml')
print(yaml_path)

f = open(yaml_path, 'r', encoding='utf-8')
# 文件读取
cont = f.read()
# 用load方法转字典
x = yaml.load(cont, Loader=yaml.FullLoader)
print(x)
# 字典转json格式
y = json.dumps(x)
print(y)
