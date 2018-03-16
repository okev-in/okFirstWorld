# -*- coding: UTF-8 -*-
print "Hello, Python!";

print 'hello';print 'runoob';
if True:
    print "True"
else:
  print "False"

if True:
      print "Answer"
      print "True"
else:
      print "Answer"
      print "False"

days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']
print days

'''
这是多行注释，使用单引号。
这是多行注释，使用单引号。
这是多行注释，使用单引号。
'''

"""
这是多行注释，使用双引号。
这是多行注释，使用双引号。
这是多行注释，使用双引号。
"""

word = 'word'
sentence = "这是一个句子。"
paragraph = """这是一个段落。
包含了多个语句"""

x="a"
y="b"
# 换行输出
print x
print y

print '---------'
# 不换行输出
print x,
print y,

# 不换行输出
print x,y

print paragraph


#raw_input("按下 enter 键退出，其他任意键显示...\n")

import sys; x = 'runoob'; sys.stdout.write(x + '\n')

# !/usr/bin/python
# -*- coding: UTF-8 -*-

counter = 100  # 赋值整型变量
miles = 1000.0  # 浮点型
name = "John"  # 字符串

print counter
print miles
print name

a = b = c = 1
print a,b,c
b = 2
c=3
print a,b,c
a, b, c = 1, 2, "john"
print a,b,c
s = 'ilovepython'
print  s[1:5]


list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']


print list               # 输出完整列表
print list[0]            # 输出列表的第一个元素
print list[1:3]          # 输出第二个至第三个元素
print list[2:]           # 输出从第三个开始至列表末尾的所有元素
print tinylist * 2       # 输出列表两次
print list + tinylist    # 打印组合的列表

"""
Python元组
元组是另一个数据类型，类似于List（列表）。
元组用"()"标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。
"""

tuple = ('runoob', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'john')

print tuple  # 输出完整元组
print tuple[1]  # 输出元组的第一个元素
print tuple[1:3]  # 输出第二个至第三个的元素
print tuple[2:]  # 输出从第三个开始至列表末尾的所有元素
print tinytuple * 2  # 输出元组两次
print tuple + tinytuple  # 打印组合的元组

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}

print dict['one']  # 输出键为'one' 的值
print dict[2]  # 输出键为 2 的值
print tinydict  # 输出完整的字典
print tinydict.keys()  # 输出所有键
print tinydict.values()  # 输出所有值
