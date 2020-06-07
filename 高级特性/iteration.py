# coding:utf-8

dictionary = {'name': 'Ana', 'age': 22}
for i in dictionary:
    print(i)

for v in dictionary.values():
    print(v)

for i, v in dictionary.items():
    print(i, v)

"""
利用迭代找到列表中的最小值和最大值，得到一个元组
"""


def find_max_min(seq):
    min_value = 0
    max_value = 0
    for i in seq:
        if i > max_value:
            max_value = i
        elif i < min_value:
            min_value = i
    tuple_number = (min_value, max_value)
    return tuple_number


number = find_max_min([1, -1, 2, -3, 0])
print(number)
