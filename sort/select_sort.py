# -*- encoding:utf-8 -*-
import sys
sys.path.insert(0, '..')
try:
    from pub.functions import time_function, is_sorted
except:
    raise


# 遍历，找到最小的元素，排到前面
@time_function
def select_sort(l):
    leng = len(l)
    for i in range(leng):
        min_ = i
        for j in range(i, leng):
            if l[j] < l[min_]:
                min_ = j
        l[min_], l[i] = l[i], l[min_]
    return l


if __name__ == "__main__":
    file_path = sys.argv[1]
    l = list()
    with open(file_path, 'rb') as r:
        for line in r:
            l.append(int(line.strip()))
    l = select_sort(l)
    # print(l)
    print(is_sorted(l))
