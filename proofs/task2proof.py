import timeit


class Fifo0:

    def __init__(self, lgh):
        self.buffer = []
        self.lgh = lgh

    def put(self, n):
        if len(self.buffer) < self.lgh:
            self.buffer.append(n)
        else:
            self.buffer.pop(0)
            self.buffer.append(n)
        return n

    def pop(self):
        if len(self.buffer) > 0:
            return self.buffer.pop(0)
        else:
            return None

    def __getBuf__(self):
        return self.buffer

    def __getLgh__(self):
        return self.lgh

    def __getStr__(self):
        return None

    def __getEnd__(self):
        return None


class Fifo1:

    def __init__(self, lgh):
        self.iterStart = 0
        self.iterEnd = 0
        self.lgh = lgh
        self.buffer = [None, ] * lgh
        self.circled = False

    def put(self, n):
        self.buffer[self.iterEnd] = n
        if self.iterEnd == self.iterStart and self.circled:
            self.iterStart += 1
        self.iterEnd += 1
        if self.iterEnd >= self.lgh:
            self.iterEnd = 0
            self.circled = True
        return n

    def pop(self):
        if not self.circled:
            return None
        temp = self.buffer[self.iterStart]
        self.iterStart += 1
        if self.iterStart >= self.lgh:
            self.iterStart = 0
        if self.iterStart == self.iterEnd:
            self.circled = False
        return temp

    def __getBuf__(self):
        return self.buffer

    def __getLgh__(self):
        return self.lgh

    def __getStr__(self):
        return self.iterStart

    def __getEnd__(self):
        return self.iterEnd


def fifoTestingSpeed(fifoClass):
    n = 50000
    fifo = fifoClass(n)
    fifo.pop()
    for i in range(n + 2):
        fifo.put(i + 1)
    for i in range(n + 2):
        fifo.pop()
    for i in range(n - 1):
        fifo.put(i + 3 + n)
    for i in range(n):
        fifo.pop()


print(timeit.timeit('fifoTestingSpeed(Fifo0)', 'from __main__ import fifoTestingSpeed, Fifo0', number=400))
print(timeit.timeit('fifoTestingSpeed(Fifo1)', 'from __main__ import fifoTestingSpeed, Fifo1', number=400))
