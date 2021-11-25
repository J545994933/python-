# todo 反转义
# print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
# print(r'hello\\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义
# print('hello\\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义
# print('hello\\\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义
# print('hello\\\\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义
# todo  字符串切片
# str1 = '123456'
# int1 = 123456
# print(str1[-1])
# print(str1.find('235'))
# print(int1[:])
# todo  列表 字典
# list1 = []
# dict1 = {}
# print(list1 is [])  # False
# print(list1 == [])  # True
# print(list1 is None)  # False
# print(dict1 is None)  # False
# # 一行语句执行多个操作
# # import sys;  x = 'runoob'; sys.stdout.write(x + '\n')
# todo sys模块获取地址
# import sys
# print('================Python import mode==========================')
# print('命令行参数为:')
# for i in sys.argv:
#     print(i)
# print('\n python 路径为', sys.path)
# from sys import argv, path  # 导入特定的成员

# print('================python from import===================================')
# for i in argv:
#     print(i)
# print('path:', path)  # 因为已经导入path成员，所以此处引用时不需要加sys.path
# *args, **kwargs参数
# def func1(*args, **kwargs):
#     print(type(args))
#     print(args)
#     print(set(args))
#     print(kwargs['school'])
# func1(1, 2, 2, 3, school=4)
# todo 连续赋值
# a = b = c = 1
# a += 1
# print(a, b, c)
# a = b = c = {}  # dict使用这种方法赋值时会统一变化,为什么?
# a['测试'] = 1
# print(a, b, c)
# b['测试'] = 2
# print(a, b, c)
# a, b, c = [], [], []
# print(a, b, c)
# todo 关于 isinstance 和 type
"""
type()不会认为子类是一种父类类型。
isinstance()会认为子类是一种父类类型  返回 True 和 False
"""
#
#
# class A(object):
#     pass
#
#
# class B(A):
#     pass
#
#
# print(isinstance(B(), A))  # B 是 A 的子类  # 可用于类型判断
# print(type(A()) == A)  # type
# print(type(A) == A)  # type
# print(type(B) == A)  # type
# print(issubclass(B, A))  # 仅可用于对比类
# todo 集合 可变类似
"""
 s.update( {"字符串"} ) 将字符串添加到集合中，有重复的会忽略。
 s.update( "字符串" ) 将字符串拆分单个字符后，然后再一个个添加到集合中，有重复的会忽略。
"""
# list1 = [1, 2, 3]
# list2 = [4, 2, 3]
# set1 = set(list1)
# print(set1[0])
# print(list(set(list2) - set(list1)))  # 只有集合可以做集合运算 | - & ^
# todo 算数运算符
# a = 20
# b = 10
# print(a/b)  # 为float
# print(a%b)  # 取余数
# print(a//b)  # 向下取整
# todo 位运算符
# a = 60  # 60 = 0011 1100
# b = 13  # 13 = 0000 1101
#
# c = a & b  # 12 = 0000 1100
# print("1 - c 的值为：", c)
#
# c = a | b  # 61 = 0011 1101
# print("2 - c 的值为：", c)
#
# c = a ^ b  # 49 = 0011 0001 当两对应的二进位相异时，结果为1
# print("3 - c 的值为：", c)
#
# c = ~a  # -61 = 1100 0011 对数据的每个二进制位取反
# print("4 - c 的值为：", c)
#
# c = a << 2  # 240 = 1111 0000
# print("5 - c 的值为：", c)
#
# c = a >> 2  # 15 = 0000 1111
# print("6 - c 的值为：", c)
# todo 数学函数
# from math import ceil, exp
#
# print(abs(-10))  # 绝对值函数
# print(ceil(-10.5))  # 向上取整函数
# print(exp(2))  # 返回e的2次幂
# todo 随机数函数
# from random import choice, random, uniform, shuffle, randrange
#
# x, y = -10, 10
# lst = [1, 2, 3, 4]
# print(choice(range(10)))  # 取0-9的随机数
# print(random())  # 随机生成下一个实数，它在[0,1)范围内
# print(uniform(x, y))  # 随机生成下一个实数，它在[x,y]范围内。
# shuffle(lst)  # 将序列的所有元素随机排序
# print(lst)
# print(randrange(100, 1000, 5))  # 100 为开始, 1000为结束 ,每次随机可增加的步数为5
# todo str 常用内置函数
#
# str1 = '  ads123   \n '
# list1 = ['1', '2', '3']
# print(str1.capitalize())  # 首字符大写
# print(str1.count('as', 0, 5))  # 查找as在str1 0-5位置的次数
# print(str1.encode('utf-8').decode('utf-8'))  # 转码再解码
# print(str1.find('asd'))  # 查找有误指定内容 有 1 无 -1
# print(str1.rfind('asd'))  # 查找有误指定内容 有 1 无 -1 从右边开始找
# print(str1.isalnum())
# print(':'.join(list1))  # 根据:分割拼接
# print(str1.strip())  # 去空格
# print(str1.replace('ads', 'a'))  # 替换
# print(str1.split('s'))  # 分割
# print(str1.splitlines())  # 根据换行符分割
# todo list 常用内置函数
# list1 = [1, 2, 3, 4, 5]
# list2 = [6, 7, 8, 9]
# del list1[0]  # 删除索引的那个值
# print(list1)
# list1.remove(2)  # 删除确切的值
# print(list1)
# list3 = list1 + list2  # 列表拼接
# print(list3)
# print(list1.count(5))  # 5在list中出现的次数
# print(list1.index(5))  # 找出某一个值
# print(list1.insert(0, 1))  # 在0号为插入元素1
# print(list1.pop())  # 默认最后一个 ,可添加索引
# list1.reverse()  # 反转list
# print(list1)
# list1.append(2)
# print(list1)
# list1.sort(reverse=True)  # list排序  默认False升序
# print(list1)
#  todo 深浅复制
# import copy
# list1 = [1, 2, 3, [4, 5]]
# list2 = list1.copy()  # 浅复制 内层还可以改变  == [:]
# list3 = copy.deepcopy(list1)  # 深复制 完全不变
# list1[3].append(6)
# print(list1)
# print(list2)
# print(list3)
# list1.append(5)
# print(list1)
# print(list2)
# print(list3)
# list1[3] = 6
# print(list1)
# print(list2)
# print(list3)
# todo 元组 tuple 不可变类型 可用的为 count len() index  内容不可改变,可用 + 连接两个元组  元素可重复
# tup1 = ('Google', 'Runoob', 1997, 2000)
# tup2 = (1, 2, 3, 4, 5)
# tup3 = "a", "b", "c", "d"   # 不需要括号也可以
# tup4 = 1, 2, 3, 4   # 不需要括号也可以
# print(tup1)
# print(tup2)
# print(tup3)
# print(tup4)
# print(tup4.index(1))  # 返回索引
# print(tup4 + tup2)
# todo dict 常用内置函数
# dict = {'Name': 'Runoob', 'Age': 7, 'Class': ['First']}
# dict['School'] = "菜鸟教程"  # 添加信息
# print("dict['Age']: ", dict['Age'])
# print("dict['School']: ", dict['School'])
# del dict['Name']
# print(dict)
# dict.clear()  # 清空字典
# print(dict)
# dict1 = dict.copy()  # 浅复制 内容值不改变 class 中的值会改变
# dict['Age'] = 8  # 更新 Age
# dict['Class'].append('Second')
# print(dict)
# print(dict1)
# # print(dict.fromkeys(seq,value))  # 创建字典
# print(dict.keys())  # 健
# print(dict.values())  # 值
# print(dict.items())  # 键值对
# print(dict.get(1, None))  # 获取dict中健为1的 如无返回None
# print(dict.pop(1, None))  # 加个None可以解决键不存在的问题
# print(dict.	popitem())  # 返回最后一对
# dict1 = {'Name': 'Runoob', 'Age': 7, '1': ['First']}
# dict.update(dict1)  # 将dict1的值更新至dict中  没有的则增加
# print(dict)
# todo 循环
# count = 0
# while count < 5:
#     print(count, " 小于 5")
#     count = count + 1
# else:
#     print(count, " 大于或等于 5")
# n = 5
# while n > 0:
#     n -= 1
#     if n == 2:
#         continue  # 仅结束本次循环
#     print(n)
# print('循环结束。')
# n = 5
# while n > 0:
#     n -= 1
#     if n == 2:
#         break  # 跳出循环
#     print(n)
# print('循环结束。')
# for n in range(2, 10):
#     for x in range(2, n):  # for else 形式可以用于有判断循环完之后如果还没找到到则使用else判断
#         print(x)
#         if n % x == 0:
#             print(n, '等于', x, '*', n//x)
#             break  # 如果先break了便不会执行
#     else:  # 循环中的最后一个
#         # 循环中没有找到元素
#         print(n, ' 是质数')
# import datetime
#
#
# def paixu(li) :
#
#     max = 0
#     for ad in range(len(li) - 1):
#         for x in range(len(li) - 1 - ad):
#             if li[x] > li[x + 1]:
#                 max = li[x]
#                 li[x] = li[x + 1]
#                 li[x + 1] = max
#             else:
#                 max = li[x + 1]
#     print(li)
# list1 = [i for i in range(10000)]
# list1.reverse()
# print(list1)
# now1 = datetime.datetime.now()
# paixu(list1)
# print(datetime.datetime.now() - now1)
# # list1 = [41,23344,9353,5554,44,7557,6434,500,2000,1,5,9,7,4,3,6,8,45,123,465,987,4656,1234,123478]
# now2 = datetime.datetime.now()
# list1.sort()
# print(datetime.datetime.now() - now2)
# print(list1)
# todo 生成器 迭代器 可迭代对象
"""
列表 集合 元组均为可迭代对象 但不是迭代器
迭代器除了可以用for in 外,还可以使用next
生成器 yeild 为一个迭代器
"""
# list1 = iter([1, 2, 3])# 强转至迭代器对象
# print(next(list1))
# print(next(list1))
# print(next(list1))
# todo 读写文件
"""
file = open(filename, mode)
filename: 文件名
mode: 模式
读: r r+ 指针在开始 从头开始读取
写: w w+ 指针在开始 从开开始写,如无该文件则会自动创建 如有则会覆盖以前的内容
写: a a+ 指针在末位 从上次最后记录的地方追加内容 如无该文件则会自动创建
其他参数: +,b b代表以二进制的方式进行读写 + 代表可同时进行读写操作 但会根据其指针的位置来判别
"""
# file = open('./test.txt', 'a+')
# # datas = file.read()  # 直接获取全部内容
# # print(datas)
# # file.close()  # 打开之后需要关闭
# # datas = file.readline()  # 只获取一行的内容
# # datas = file.readlines()  # 获取所以行的内容 并转换成一个list
# # for data in datas:
# #     print(data)
# # print(datas)
# # for line in file:  # 逐一提取每行内容
# #     print(line)
# value = ('www.runoob.com', 14)
# s = str(value)
# file.write(s)
# print(file.tell())  # 获取当前所在字节数
# file.close()
# with open('./test.txt', 'r+') as f:
#     read_data = f.readlines()
# print(read_data)
# todo class
"""
类的专有方法：
__init__ : 构造函数，在生成对象时调用
__del__ : 析构函数，释放对象时使用
__repr__ : 打印，转换
__setitem__ : 按照索引赋值
__getitem__: 按照索引获取值
__len__: 获得长度
__cmp__: 比较运算
__call__: 函数调用
__add__: 加运算
__sub__: 减运算
__mul__: 乘运算
__truediv__: 除运算
__mod__: 求余运算
__pow__: 乘方
静态方法: 用 @staticmethod 装饰的不带 self 参数的方法叫做静态方法，类的静态方法可以没有参数，可以直接使用类名调用。
普通方法: 默认有个self参数，且只能被对象调用。
类方法: 默认有个 cls 参数，可以被类和对象调用，需要加上 @classmethod 装饰器。
"""

# 类定义
# class people:
#     # 定义基本属性
#     # name = ''
#     # age = 0
#     # # 定义私有属性,私有属性在类外部无法直接进行访问
#     # __weight = 0
#
#     # 定义构造方法
#     def __init__(self, n, a, w):
#         self.name = n
#         self.age = a
#         self.__weight = w
#
#     def speak(self):
#         print("%s 说: 我 %d 岁。" % (self.name, self.age))
#
# # 单继承示例
# class student(people):
#     # grade = ''
#
#     def __init__(self, n, a, w, g):
#         # 调用父类的构函
#         people.__init__(self, n, a, w)
#         self.grade = g
#
#     # 覆写父类的方法
#     def speak(self):
#         print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))
#
#
# s = student('ken', 10, 60, 3)
# s.speak()
# todo 队列

# from queue import Queue
# import threading
# import time
# q = Queue()
#
#
# def product(name):
#     count = 1
#     while True:
#         dict1 = {'1': 1, '2': 2}
#         print(q.qsize())
#         q.put(dict1)
#         print(q.qsize())
#         print('{}训练气球兵{}只'.format(name, count))
#         count += 1
#         time.sleep(5)
#
#
# def consume(name):
#     while True:
#         data = q.get()
#         print(data,type(data))
#         print('{}使用了{}'.format(name, data))
#         time.sleep(1)
#         q.task_done()
#
#
# t1 = threading.Thread(target=product, args=('wpp',))
# t2 = threading.Thread(target=consume, args=('ypp',))
# t3 = threading.Thread(target=consume, args=('others',))
#
# t1.start()
# t2.start()
# t3.start()
# todo 局部变量与作用域
# def outer():
#     num = 10
#     def inner():
#         nonlocal num   # nonlocal关键字声明
#         num = 100
#         print(num)
#     inner()
#     print(num)
# outer()
#
# num = 1
# def fun1():
#     global num  # 需要使用 global 关键字声明
#     print(num)
#     num = 123
#     print(num)
# fun1()
# print(num)
# todo 文本切割算法
# import re
# introduce = """那今天的福利呢就是珂拉琪口红珂拉琪。所有女生人手一支两支八支十支都不为过的贼好用的唇釉猫猫店六十九米一支，线下门店四十九一支，
# 其他直播再便宜也要三十九点九米一支，今天在呦呦的直播间六十九米不要，四十九米不要，三十九点九米也不要了。
# 所有想要珂拉琪的姐妹，左上角关注点起来，然后把唇釉，两个字抠在公屏上，所有点了关注，抠了唇釉的姐妹，今天直接二十八点八米带走了。"""
# # sentences = re.split('[，。;]', introduce)
# # print(sentences)
# # for sentence in sentences:
# #     if len(sentence) > 50:
# #         print(False)
# #     else:
# #         print(sentence)
#
# def str_split(sentences):
#     index = 0
#     while index != len(sentences):
#         print(index)
#         if len(sentences[index]) > 60:
#             print(sentences[index])
#             sentences_list = sentence_split(sentences[index])
#             for i in range(len(sentences_list)):
#                 sentences.insert(index + i, sentences_list[i])
#             index += len(sentences_list)
#             sentences.remove(sentences[index])
#         else:
#             index += 1
#
# def sentence_split(introduce):
#     sentences = re.split('[，。;]', introduce)
#     sentence_list = []
#     initial_str = sentences[0]
#     for sentence_index in range(1, len(sentences)):
#         # print(sentence_index, len(sentences))
#         if len((initial_str + sentences[sentence_index])) > 60 or sentence_index == len(sentences) - 1:
#             sentence_list.append(initial_str)
#             initial_str = sentences[sentence_index]
#             if sentence_index == len(sentences) - 1:
#                 sentence_list.append(initial_str)
#         else:
#             initial_str = initial_str + ',' + sentences[sentence_index]
#     return sentence_list
#
# sentences = introduce.split('。')
# str_split(sentences)
# print(sentences)
# todo docker
"""
docker ps -a 查看已经在运行的容器
docker images 查看镜像
docker exec -it 
"""
# todo git
"""
git config --global http.sslVerrify "false" 连接失败或者超时时可以执行该命令
git config --global user.name "jiangyujie" 名字
git config --global user.email "545994933@qq.com" 邮箱
ssh-keygen 生成公钥   
"""
# todo re正则表达式
# import re
# pattern = ''
# context = ''
# re.match(pattern, context)
# test = '123,456,789'
# print(test.split(',')[0])
# list_test = [1]
# for i in range(len(list_test)):
#     print(i)
A = [1, 2, 3, 4, 4]
B = [1, 1, 2, 5]

for a in A.copy():
    if a in B:
        A.remove(a)
        B.remove(a)

print(A+B)
