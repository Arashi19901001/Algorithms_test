# -*- encoding:utf-8 -*-
import sys
sys.path.insert(0, '..')
try:
    from pub.functions import time_function, is_sorted
except:
    raise


# 从第一个元素起，往前遍历， 若上一个元素比他大，则交换位置，直至上一个元素比他小, break, 下一重循环
# 最糟糕情况n ^ 2次比较， n ^ 2次交换
# 理想情况系n次比较，0次交换
@time_function
def insert_sort(l):
    leng = len(l)
    for i in range(0, leng):
        tmp = l[i]
        j = i
        while(j >= 0) and (tmp < l[j - 1]):
            l[j] = l[j - 1]
            j -= 1
        l[j] = tmp
    return l


if __name__ == "__main__":
    file_path = sys.argv[1]
    l = list()
    with open(file_path, 'rb') as r:
        for line in r:
            l.append(int(line.strip()))
    l = insert_sort(l)
    # print(l)
    print(is_sorted(l))
