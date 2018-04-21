import time


def time_function(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print("function name: {}|| Time cost: {}".format(func.__name__, t2 - t1))
        return result
    return wrapper


def binsearch(seq, target):
    min_ = 0
    max_ = len(seq) - 1
    while True:
        if max_ < min_:
            return -1
        m = (min_ + max_) // 2
        if seq[m] < target:
            min_ = m + 1
        elif seq[m] > target:
            max_ = m - 1
        else:
            return m


def is_sorted(l):
    return all(l[i] <= l[i + 1] for i in range(len(l) - 1))
