import timeit


def isEven(value):
    return value % 2 == 0


def isEven2(value):
    if value % 2:
        return False
    else:
        return True


def isEven3(value):
    if value & 1:
        return False
    else:
        return True


def isEven4(value):
    return not (bool(value & 1))


print(timeit.timeit('isEven(6)', 'from __main__ import isEven', number=10000))
print(timeit.timeit('isEven2(6)', 'from __main__ import isEven2', number=10000))
print(timeit.timeit('isEven3(6)', 'from __main__ import isEven3', number=10000))
print(timeit.timeit('isEven4(6)', 'from __main__ import isEven4', number=10000))
print()
print(timeit.timeit('isEven(66666666666666666666666666666666666666666666666666)', 'from __main__ import isEven',
                    number=10000))
print(timeit.timeit('isEven2(66666666666666666666666666666666666666666666666666)', 'from __main__ import isEven2',
                    number=10000))
print(timeit.timeit('isEven3(66666666666666666666666666666666666666666666666666)', 'from __main__ import isEven3',
                    number=10000))
print(timeit.timeit('isEven4(66666666666666666666666666666666666666666666666666)', 'from __main__ import isEven4',
                    number=10000))
