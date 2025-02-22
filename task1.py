# Данная реализация основана на побитовом умножении вместо вычисления остатка от деления.
# Такая реализация будет выполнять проверку чётности медленее для малых чисел, но будет работать быстрее на больших
# числах и медленнее на малых числах. Это связано с более быстрой работой функции побитового умножения и наличием в
# Python оптимизации оператора % (modulo) для небольших чисел.

def isEven(value):
    if value & 1:  # Проверка чётности с помощью бинарной операции
        return False
    else:
        return True
