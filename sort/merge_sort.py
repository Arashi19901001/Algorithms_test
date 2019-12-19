# -*- coding: utf-8 -*-
import sys
from pub.functions import is_sorted


class MergeSort:
    def sort(self, li, test=""):
        print(test)
        if len(li) <= 1:
            return li
        mid = len(li) // 2
        left = self.sort(li[:mid], "left")
        right = self.sort(li[mid:], "right")
        return self.merge(left, right)

    def merge(self, left, right):
        i = 0
        j = 0
        result = list()
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
        return result


if __name__ == "__main__":
    file_path = sys.argv[1]
    li = list()
    with open(file_path, 'rb') as r:
        for line in r:
            li.append(int(line.strip()))

    m = MergeSort()
    new_li = m.sort(li)
    print(is_sorted(new_li))
