# -*- encoding:utf-8 -*-
import sys
import time
sys.path.insert(0, '..')
try:
    from pub.functions import binsearch, time_function
except:
    raise


@time_function
def three_sum(l):
    c = 0
    length = len(l)
    for i in range(length):
        for j in range(i + 1, length):
            for k in range(j + 1, length):
                if l[i] + l[j] + l[k] == 0:
                    c += 1
    print 'three_sum result: {}'.format(c)


@time_function
def two_sum(l):
    c = 0
    length = len(l)
    for i in range(length):
        for k in range(i + 1, length):
            if l[i] + l[k] == 0:
                # print "{} + {} = 0".format(l[i], l[k])
                c += 1
    print 'two_sum result: {}'.format(c)


@time_function
def two_sum_fast(l):
    c = 0
    length = len(l)
    t1 = time.time()
    l.sort()
    t2 = time.time()
    print 'sort time cost: {}'.format(t2 - t1)
    for i in range(length):
        if binsearch(l, - l[i]) > i:
            c += 1
    print 'two_sum_fast result: {}'.format(c)


@time_function
def three_sum_fast(l):
    c = 0
    length = len(l)
    t1 = time.time()
    l.sort()
    t2 = time.time()
    print 'sort time cost: {}'.format(t2 - t1)
    for i in range(length):
        for j in range(i + 1, length):
            if binsearch(l, -l[i] - l[j]) > j:
                c += 1
    print 'three_sum_fast result: {}'.format(c)


file_path = sys.argv[1]
l = list()
with open(file_path, 'rb') as r:
    for line in r:
        l.append(int(line.strip()))

two_sum_fast(l)
two_sum(l)
three_sum_fast(l)
three_sum(l)
