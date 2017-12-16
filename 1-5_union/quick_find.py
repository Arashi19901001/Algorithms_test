# -*- coding: utf-8 -*-
import re
import time
import sys


class Union(object):
    def __init__(self, n):
        # set count
        self.time_counter = 0
        self.ini_time = time.time()
        self.count = n
        # all numbers. when initialed, every number make a data set

        self.id = list(xrange(n))

    def connected(self, p, q):
        # if p, q is connected, p, q is in the same set of data
        return self.id[p] == self.id[q]

    def find(self, p):
        return self.id[p]

    def union(self, p, q):
        self.time_counter += 1
        if not self.time_counter % 100:
            print "data count: {}, time cost: {}".format(self.time_counter, time.time() - self.ini_time)
        # p, q given in method union mean p, q is conneted(in the same data set)
        p_id = self.find(p)
        q_id = self.find(q)
        if p_id == q_id:
            return
        # when a pair of number is gaven, and they are in different set, means this two set are connected yet, make these two data sets by making the id of numbers in this two set same, and decrease set count。
        for i in xrange(len(self.id)):
            if self.id[i] == p_id:
                self.id[i] = q_id
        self.count -= 1


FILE_NAME_TO_NUMBER = {
    'tinyUF.txt': 10,
    'mediumUF.txt': 625,
    'largeUF.txt': 1000000
}
un = Union(FILE_NAME_TO_NUMBER[sys.argv[1]])
t1 = time.time()
with open(sys.argv[1], 'rb') as r:
    for line in r:
        (p, q) = re.split('\s+', line.rstrip())
        p = int(p)
        q = int(q)
        un.union(p, q)
print 'id of list'
print un.id
print 'set count: {}'.format(un.count)
t2 = time.time()
print "time cost: {}".format(t2 - t1)
