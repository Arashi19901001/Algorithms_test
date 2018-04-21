# -*- encoding:utf-8 -*-
import sys
sys.path.insert(0, '..')
try:
    from pub.functions import time_function, is_sorted
except:
    raise


@time_function
def insert_sort(l):
    leng = len(l)
    for i in range(leng):
        tmp = l[i]
        for j in range(i, 0, -1):
            if tmp < l[j]:
                l[j + 1] = l[j]
                l[j] = tmp
            else:
                break
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
