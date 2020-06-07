# coding:utf-8

"""
使用生成器生成斐波那契数列
"""


def fibo(number):
    n, a, b = 0, 0, 1
    while n < number:
        a, b = b, a + b
        yield b
        n += 1


f = fibo(5)
"""
使用生成器生成杨辉三角
"""


def triangles(line):
    a = [1]
    n = 0
    while n < line:
        yield a[:len(a)]
        a.append(0)
        a = [a[i - 1] + a[i] for i in range(len(a))]
        n += 1


g = triangles(5)
for i in g:
    print(i)
