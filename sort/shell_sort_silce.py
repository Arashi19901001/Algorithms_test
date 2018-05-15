# -*- encoding:utf-8 -*-
import sys
import copy
sys.path.insert(0, '..')
try:
    from pub.functions import time_function, is_sorted
except:
    raise


# 对一个列表进行切片，第一次切成slice片，每片长度为gap(gap * (slice -1)<=len(l)<= gap * slice）假定认为每一片内部都是有序的，不做排序， 仅对不同分片间同一个位置上的元素做排序
# silce -1，重复上面步骤
@time_function
def shell_sort_slice(l, slice_):
    leng = len(l)
    gap = 1
    while(gap < leng / slice_):
        gap = gap * slice_ + 1
    while(gap >= 1):
        # slice与silce之间进行插入排序
        for i in range(gap, leng):
            tmp = l[i]
            j = i
            while j >= gap and l[j - gap] > tmp:
                l[j] = l[j - gap]
                j -= gap
            l[j] = tmp
        gap = gap // slice_
    return l


if __name__ == "__main__":
    file_path = sys.argv[1]
    l = list()
    with open(file_path, 'rb') as r:
        for line in r:
            l.append(int(line.strip()))
    tmp_l = copy.deepcopy(l)
    for slice_ in range(2, 100):
        tmp_l = shell_sort_slice(tmp_l, slice_)
        print(is_sorted(tmp_l))
