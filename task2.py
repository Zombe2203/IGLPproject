# Первая реализация основана на встроенных в Python списках и возможности динамически менять их длину с помощью функций
# append() и pop().
# Вторая реализация основана на использовании списка фиксированной длины и индексов для ввода и вывода.
# Поскольку первая реализация использует встроенные в Python функции работы с листами, которые создают копии листов при
# использовании, вторая реализация оказывается быстрее при работе с буфферами большого размера

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
