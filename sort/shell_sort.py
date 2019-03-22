# -*- encoding:utf-8 -*-
import sys
sys.path.insert(0, '..')
try:
    from pub.functions import time_function, is_sorted
except Exception:
    raise


# 对一个序列按照一个特定的序列切片，不同的序列有不同的时间效率, 这里使用gap = (3^n - 1) / 2, 切需要保证gap / 3 不大于这个列表长度的三分之一， n为第几次切片，gap为每一片的长度, 最后一轮需要保证gap长度是1，即最后一轮进行一轮标准的插入排序
# 假定每个gap长度的内部都是有序的，不做排序, 仅对不同分片间同一个位置上的元素做排序
# n - 1，重新计算gap (这里为gap = gap // 3)
@time_function
def shell_sort(li):
    leng = len(li)
    gap = 1
    while(gap < leng / 3):
        gap = gap * 3 + 1
    while(gap >= 1):
        print(gap)
        # slice与silce之间进行插入排序
        for i in range(gap, leng):
            tmp = li[i]
            j = i
            while (j - gap) >= 0 and li[j - gap] > tmp:
                li[j] = li[j - gap]
                j -= gap
            li[j] = tmp
        gap = gap // 3
    return li


if __name__ == "__main__":
    file_path = sys.argv[1]
    li = list()
    with open(file_path, 'rb') as r:
        for line in r:
            li.append(int(line.strip()))
    li = shell_sort(li)
    print(is_sorted(li))
