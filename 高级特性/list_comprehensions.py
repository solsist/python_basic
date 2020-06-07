# coding:utf-8

"""
列表表达式
"""
one_list = [x*x for x in range(10)]
print(one_list)

two_list = [x*x for x in range(10) if x % 2 == 0]
print(two_list)

"""
如果list中包含整数和字符串，使用lower()方法会出错
"""
three_list = ['Hello', 'Apple', 'Banana', 'World', 22]
third_list = [s.lower() for s in three_list if isinstance(s, str)]
print(third_list)
 


