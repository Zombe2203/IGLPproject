# Trimsort - комбинация Insertion sort и Merge sort, выигрывюающая на частично отстортированных массивах и являющаяся
# стандартным алгоритмом сортировки Python. Подходит для задачи поскольку количество и размер чисел в массиве
# неизвестны, а их порядок случаен и может содержать отстортированные подмассивы.
# В лучшем случае O(n), в среднем O(n logn), в худшем O(n logn).

# Quick sort - подходит для любых массивов, в худшем случае имеет время выполнения O(n^2). При выборе в качестве
# опорного элемента "медианы трёх" массива (медианы первого, среднего и последнего элементов), худшее время выполнения
# сокращается до O(n log). На сильно отсортированных массивах такая сортировка будет проигрывать Trimsort (сотрировка
# по умолчанию в Python), однако согласно заданию порядок чисел в массиве может быть абсолютно случайным. В отличие от
# Trimsort Quicksort не является устойчивым, но это не необходимо для задачи сортировки чисел.
# В лучшем случае O(n logn), в среднем O(n logn), в худшем O(n logn).

def findMedian(value1, value2, value3):
    if value1[0] < value2[0]:
        if value1[0] < value3[0]:
            if value2[0] < value3[0]:
                return value2[0], value2[1]
            else:
                return value3[0], value3[1]
        else:
            return value1[0], value1[1]
    else:
        if value1[0] > value3[0]:
            if value2[0] > value3[0]:
                return value2[0], value2[1]
            else:
                return value3[0], value3[1]
        else:
            return value1[0], value1[1]


def quickSort(data, start, end, ascending=True):
    if start < end:
        median, medIndex = findMedian((data[start], start),
                                      (data[(start + end - 1) // 2], (start + end - 1) // 2),
                                      (data[end - 1], end - 1))
        data[start], data[medIndex] = data[medIndex], data[start]
        pointer = start + 1
        for i in range(start + 1, end):
            if (ascending and data[i] < median) or (not ascending and data[i] > median):
                data[pointer], data[i] = data[i], data[pointer]
                pointer += 1
        data[start], data[pointer - 1] = data[pointer - 1], data[start]
        quickSort(data, start, pointer - 1, ascending)
        quickSort(data, pointer, end, ascending)
    return None


test = [4.9504, -1393.4, 1. / 156, 3.1415, 3.1415, 35.445]
quickSort(test, 0, len(test), True)
