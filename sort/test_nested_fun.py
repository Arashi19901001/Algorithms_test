def parent(l):
    print("parent, len(l): {}".format(len(l)))
    print(l)
    def child(s):
        s.pop()
        print("child, len(s): {}".format(len(l)))
    child(l)
    print("parent, len(l): {}".format(len(l)))
    print(l)


l = list(range(10))
parent(l)
print("=" * 20)
# l = list(range(10))
parent(l)
