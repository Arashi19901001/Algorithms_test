# -*- encoding:utf-8 -*-
import sys
import random
sys.path.insert(0, '..')
try:
    from pub.functions import time_function, is_sorted
except Exception:
    raise


# 将一个数组按一个基准(可以取数组中的第一个，或者随机从数组中选择一个)拆分成两部分

# 需要额外内存版本
@time_function
def quicksort(array, base="first"):
    array = _quicksort(array, base="first")
    return array


def _quicksort(array, base="first"):
    less = list()
    equal = list()
    more = list()

    if len(array) > 1:
        if base == "first":
            pivot = array[0]
        else:
            pivot = random.choice(array)
        for i in array:
            if i > pivot:
                more.append(i)
            elif i < pivot:
                less.append(i)
            else:
                equal.append(i)
        return _quicksort(less, base=base) + equal + _quicksort(more, base=base)
    else:
        return array


# 不需要额外内存版本
def partition(array, low, high):
    # low从0开算, high为列表的最后一个index, 以range遍历的时候需要 + 1
    pivot = low  # 选取low为基准，将数组分为两组，小于基准的放到基准左边，大于基准的放到基准右边; pivot的意义为两组的分界点的index
    for i in range(low + 1, high + 1):
        if array[i] <= array[low]:  # 与基准进行比较
            pivot += 1  # 保持基准的位置不变(这里的为low)，当列表元素值小于基准的时候，基准的index + 1(代表小的那组元素个数又多了一个), 并且交换两个元素的位置
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[low] = array[low], array[pivot]  # 交换基准和low组的一个元素, 基准处于两组数据的中间
    return pivot  # 返回边界的下标


def partition_random(array, low, high):
    pivot = random.randint(low, high)
    pivot_value = array[pivot]

    # 处理前半部分
    base = low - 1
    for i in range(low, pivot):
        if array[i] <= pivot_value:
            base += 1
            array[base], array[i] = array[i], array[base]
    # 将基准调整到正确的位置
    base += 1
    array[base], array[pivot] = array[pivot], array[base]
    # 现在基准的index为base
    old_pivot = pivot
    pivot = base

    # 处理后半部分
    for i in range(old_pivot + 1, high + 1):
        if array[i] <= pivot_value:
            base += 1
            array[base], array[i] = array[i], array[base]
    # 调整基准
    array[base], array[pivot] = array[pivot], array[base]

    return base


@time_function
def quicksort_in_place(array, low, high, base="first"):
    _quicksort_in_place(array, low, high, base)


def _quicksort_in_place(array, low, high, base="first"):
    if low < high:
        if base == "first":
            pivot = partition(array, low, high)
        else:
            pivot = partition_random(array, low, high)
        _quicksort_in_place(array, low, pivot - 1, base)
        _quicksort_in_place(array, pivot + 1, high, base)
    return array


if __name__ == "__main__":
    file_path = sys.argv[1]
    li = list()
    with open(file_path, 'rb') as r:
        for line in r:
            li.append(int(line.strip()))
    li1 = li[:]
    li2 = li[:]
    li3 = li[:]
    li4 = li[:]
    li1 = quicksort(li1, "first")
    print(is_sorted(li1))
    li2 = quicksort(li2, "random")
    print(is_sorted(li2))

    n = len(li3) - 1
    quicksort_in_place(li3, 0, n)
    print(is_sorted(li3))
    n = len(li4) - 1
    quicksort_in_place(li4, 0, n, "random")
    print(is_sorted(li4))
