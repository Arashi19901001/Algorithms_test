# -*- encoding:utf-8 -*-
import sys
sys.path.insert(0, '..')
try:
    from pub.functions import time_function
except:
    raise


@time_function
def buble_sort(l):
    leng = len(l)
    for i in range(leng - 1):
        for j in range(i + 1, leng):
            if l[j - 1] > l[j]:
                (l[j - 1], l[j]) = (l[j], l[j - 1])
    return l


if __name__ == "__main__":
    file_path = sys.argv[1]
    l = list()
    with open(file_path, 'rb') as r:
        for line in r:
            l.append(int(line.strip()))
    buble_sort(l)
