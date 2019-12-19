# -*- encoding:utf-8 -*-
import sys
sys.path.insert(0, '..')
try:
    from pub.functions import time_function, is_sorted
except:
    raise


# 比较相邻元素的大小， 如果前者比后者大， 则交换位置
@time_function
def buble_sort(l):
    leng = len(l)
    for i in range(leng):
        for j in range(leng - i -1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
    return l


if __name__ == "__main__":
    file_path = sys.argv[1]
    l = list()
    with open(file_path, 'rb') as r:
        for line in r:
            l.append(int(line.strip()))
    buble_sort(l)
    print(is_sorted(l))
