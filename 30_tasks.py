#имя проекта: 30 задач
#номер версии: 1.0
#имя файла: 30_tasks.py
#автор и его учебная группа: И. Поллак, ЭУ-120
#дата создания: 22.05.2020
# дата последней модификации: 22.05.2020
#связанные файлы: numpy
# описание: решение СЛАУ с использованием библиотеки numpy
#версия Python: 3.8
import numpy as np


def task1(a, n, m):
    b = np.fabs(a)                          # получаем положительные значения массива а
    index = np.argmax(b.max(axis=0))        # получаем индекс наибольших элементов столбца массива
    print((a[:, index]).max())              # выводим максимальный элемент (без учета модуля) столбца массива


def task2(a, n, m):
    print(max(a.mean(axis=1)))              # наибольшее среднее значение для каждой строки


def task3(a, n, m):
    b = np.fabs(a)                          # получаем положительные значения массива а
    index = np.argmax(b.max(axis=0))        # получаем индекс наибольших элементов столбца массива
    print((a[:, index]).min())              # выводим минимальный элемент (без учета модуля) столбца массива


def task4(a, n, m):
    print(min(a.mean(axis=1)))              # наименьшее среднее значение для каждой строки


def task5(a, n, m):
    col = a.mean(axis=0)                    # среднее по столбцам
    col = (col[np.newaxis, :])              # приведение к двумерному массиву
    # print(np.vstack([a, col]))
    a = (np.vstack([a, col]))               # присоединяем новую строку
    row = a.mean(axis=1)                    # среднее по строкам
    row = (row[np.newaxis, :])              # приведение к двумерному массиву
    row = row.reshape(n + 1, 1)             # переопределяем размерность
    a = (np.hstack([a, row]))               # присоединяем новый столбец
    print(a)


def task6(a, n, m):
    sum_elem = a.sum()                                       # сумма всех элементов матрицы
    list_sum_col = []
    for i in range(m):                                       # обход по столбцам
        sum_col = sum(a[:, i])                               # сумма элементов столбца
        list_sum_col.append(sum_col * 100 / sum_elem)        # записываем в список долю от общей суммы
    npa = np.asarray(list_sum_col)                           # приводим список к ndarray
    npa = (npa[np.newaxis, :])                               # делаем двумерным
    a = (np.vstack([a, npa]))                                # присоединяем эту строку в массив а
    print(a)


def task7(a, n, m):
    sum_elem = a.sum()                                       # сумма всех элементов матрицы
    list_sum_row = []
    for i in range(n):                                       # обход по строкам
        sum_row = sum(a[i, :])                               # сумма элементов строки
        list_sum_row.append(sum_row * 100 / sum_elem)        # записываем в список долю от общей суммы
    row = np.asarray(list_sum_row)                           # приводим список к ndarray
    row = (row[:, np.newaxis])                               # записываем в столбец
    a = np.append(a, row, axis=1)                            # добавляем столбец
    print(a)


def task8(a, n, m):
    col = []
    row = []
    for i in range(m):                                       # обход по столбцам
        b = a[:, i]                                          # значения столбца
        col.append(sum(i < 0 for i in b))                    # считаем сколько отрицательных элементов
    col = np.asarray(col)                                    # приводим список к ndarray
    col = (col[np.newaxis, :])                               # приводим к двумерному
    a = np.append(a, col, axis=0)                            # присоединяем строку

    for i in range(n + 1):                                   # обход по строкам ( n + 1 т.к. их стало больше)
        b = a[i, :]                                          # значения строки
        row.append(sum(i < 0 for i in b))                    # считаем сколько отрицательных элементов
    row = np.asarray(row)                                    # приводим список к ndarray
    row = (row[:, np.newaxis])                               # записываем в столбец
    a = np.append(a, row, axis=1)                            # добавляем этот столбец
    print(a)


def task9(a, n, m, l, k):
    count_top = 0
    count_left = 0
    b = a[:l, :].copy()                                                     # берем верхние l- строки матрицы
    for index, value in np.ndenumerate(b):
        if value == 0:                                                      # если значение равно 0
            count_top += 1                                                  # добавляем в счетчик + 1
    print("The first " + str(l) + " lines: " + str(count_top) + " zeros")

    c = a[:, :k].copy()                                                     # матрица из левых k-строк
    for index, value in np.ndenumerate(c):
        if value == 0:                                                      # если значение равно 0
            count_left += 1                                                 # добавляем в счетчик + 1
    print("The first " + str(k) + " columns: " + str(count_top) + " zeros")


def task10(a, n, m, k):
    col = a[:, k]                   # берем к-ый столбец
    for i in range(m):              # перебираем каждый столбец
        if i == k:                  # к-ый пропускаем
            continue
        a[:, i] = col * a[:, i]     # умножаем i-ый столбец на к-ый
    print(a)


def task11(a, n, m, l):
    row = a[l, :]                   # берем l-ую строку
    for i in range(n):              # перебираем каждую строку
        if i == l:                  # l-ую пропускаем
            continue
        a[i, :] = row + a[i, :]     # суммируем i-ую строку со строкой l
    print(a)


def task12(a, n, m):
    #.astype()
    max_elem = a.max(axis=1)        # максимальный элемент каждой строки
    print(max_elem)
    for i in range(n):
        for j in range(m):
            a[i][j] /= max_elem[i]  # делим элемент массива на соответствующий макс элемент строки
    print(a)


def task13(a, n, m):
    for i in range(m):
        max_elem = max(a[:, i])      # макс элемент каждого столбца
        #print(max_elem)
        a[:, i] /= max_elem          # делим элемент столбца на макс элемент этого столбца и записывам в этот же массив
    print(a)


def task14(a, n, m):
    a = a / (a.max())                   # каждое значение массива делим на максимальный
    print(a)


def task15(a, n, m, h):
    contains = []
    not_contains = []
    for i in range(m):                  # бежим по столбцам
        if h in a[:, i]:                # если число h содержится в столбце i
            contains.append(i)          # добавляем в список contains номер столбца
        else:
            not_contains.append(i)      # иначе добавляем в список not_contains
    print('Contains: {}, Not contains: {}, value: {}'.format(contains, not_contains, h))


def task16(a, n, m, l):
    a = np.delete(a, l, axis=0)         # исключаем строку с номером l (axis=0 - строка)
    print(a)


def task17(a, n, m, l):
    a = np.insert(a, [l], [1], axis=0)  # добавляем строку из 1 под номером l
    print(a)


def task18(a, n, m):
    # n must less then m
    sumMain = 0                             # храним сумму главной диагонали
    sumSecondary = 0                        # храним сумму побочной диагонали
    for i in range(N):
        sumMain += a[i][i]                  # сумма элементов на главной диагонали
        sumSecondary += a[i][n - i - 1]     # сумма элементов на побочной диагонали
    print(sumMain)
    print(sumSecondary)


def task19(a, n):
    sum_elem_down = 0                       # храним сумму элементов параллельно главной диагонали (ниже нее)
    sum_elem_up = 0                         # храним сумму элементов параллельно главной диагонали (выше нее)
    for i in range(1, n):                   # с 1 индекса до номера n -1
        sum_elem_down += a[i][i - 1]        # сумма элементов параллельно главной диагонали (ниже нее)
        sum_elem_up += a[i - 1][i]          # сумма элементов параллельно главной диагонали (выше нее)
    print(sum_elem_down + sum_elem_up)      # общая сумма


def task20(a, n):
    sum_elem_down = 1
    sum_elem_up = 1
    for i in range(0, n-1):
        sum_elem_down *= a[n-i-1][i+1]      # элементы параллельно побочной диагонали (под)
        sum_elem_up *= a[i][n-i-2]          # элементы параллельно побочной диагонали (над)
    print(sum_elem_down * sum_elem_up)


def task21(a, n):
    for i in range(1, n):
        _sum = a[i][i - 1] + a[i - 1][i]    # пара симметричных элементов относительно главной диагонали
        a.itemset((i, i-1), _sum // 2)      # присваиваем полусумму
        a.itemset((i-1, i), _sum // 2)      # присваиваем полусумму
    print(a)


def task22(a, n, m):
    b = a.sum(axis=1)                       # находим сумму элементов строки
    b %= 2                                  # делим по модулю на 2, останется либо 1 либо 0
    b = (b[np.newaxis, :])                  # делаем массив двумерным
    b = b.reshape(n, 1)                     # меняем размерность массива
    print(np.hstack([a, b]))                # добавляем столбец b в массив a


def task23(a, n):
    sum_elem = 0
    mul_elem = 1
    for i in range(0, n):
        sum_elem += a[i, i + 1:].sum()      # сумма элементов выше главной диагонали

    for i in range(0, n - 1):
        for j in range(0, n - i - 1):
            mul_elem *= a[i][j]             # произведение элементов выше побочной диагонали
    print("Sum_elem= " + str(sum_elem) + " Mul_elem= " + str(mul_elem))


def task24(a, n, m, l, k):
    # суммирование элементов четвертей
    print(a[:l, :k].sum())
    print(a[:l, k:].sum())
    print(a[l:, :k].sum())
    print(a[l:, k:].sum())


def task25(a, n, m):
    col = []
    row = []

    for i in range(m):                                      # обход по столбцам
        col.append(np.count_nonzero(a[:, i] == 0))          # считаем количество нулевых элементов в столбцах
    col = np.asarray(col)                                   # приводим список к ndarray
    col = (col[np.newaxis, :])                              # приводим к двумерному [[]]
    a = np.append(a, col, axis=0)                           # добавляем строку

    for i in range(n + 1):                                  # обход по строкам
        row.append(np.count_nonzero(a[i, :] == 0))          # считаем количество нулевых элементов в строках
    row = np.asarray(row)                                   # приводим список к ndarray
    row = (row[:, np.newaxis])                              # приводим к двумерному [[][][]...]
    a = np.append(a, row, axis=1)                           # добавляем столбец
    print(a)


def task26(a, n, m, l, k):
    # среднее арифметическое четвертей
    print(a[:l, :k].mean())
    print(a[:l, k:].mean())
    print(a[l:, :k].mean())
    print(a[l:, k:].mean())


def task27(a, n, m, h):
    contains = []                           # изначально пустые списки
    not_contains = []
    for i in range(n):
        if h in a[i, :]:                    # берем каждую строку и проверяем содержится ли в ней h
            contains.append(i)              # добавляем номер строки в contains если содержится
        else:
            not_contains.append(i)          # добавляем номер строки в not_contains если не содержится
    print('Contains: {}, Not contains: {}, value: {}'.format(contains, not_contains, h))


def task28(a, n, m, k):
    a = np.delete(a, (k), axis=1)           # исключаем столбец с номером k
    print(a)


def task29(a, n, m, k):
    b = np.random.randint(-15, 15, size=(n, 1))
    c = np.insert(a, k, values=b[:, 0], axis=1)     # вставляем столбец рандомных чисел под номером k
    print(c)


def task30(a, n, m):
    col = []
    for i in range(m):                      # идем по столбцам
        b = a[:, i]                         # берем столбец
        sum_abs = 0
        sum = 0
        for j in range(n):                  # обходим элементы этого столбца
            if b[j] < 0:
                sum_abs += abs(b[j])        # считаем сумму отрицательных значений как положительных
            else:
                sum += b[j]                 # считаем сумму положительных значений
        col.append(sum_abs - sum)           # вычитаем и добавляем в список (для каждого столбца)
    col = np.asarray(col)                   # приводим список к ndarray
    col = (col[np.newaxis, :])              # приводим к двумерному [[]]
    a = np.append(a, col, axis=0)           # добавляем новую строку в матрицу
    print(a)


def task31(a, n, m):
    row = []
    for i in range(n):                      # идем по строкам
        b = a[i, :]                         # берем строку
        sum_abs = 0
        sum = 0
        for j in range(m):                  # обходим элементы этой строки
            if b[j] < 0:
                sum_abs += abs(b[j])
            else:
                sum += b[j]
        row.append(sum_abs - sum)
    row = np.asarray(row)
    row = (row[:, np.newaxis])
    a = np.append(a, row, axis=1)           # добавляем новый столбец в матрицу
    print(a)


if __name__ == '__main__':
    N = 5
    M = 6

    A = np.random.randint(-15, 15, size=(N, M))
    print("task1")
    task1(A, N, M)
    print("task2")
    task2(A, N, M)
    print("task3")
    task3(A, N, M)
    print("task4")
    task4(A, N, M)
    print("task5")
    task5(A, N, M)
    print("task8")
    task8(A, N, M)
    print("task9")
    task9(A, N, M, 2, 3)
    print("task10")
    task10(A, N, M, 2)
    print("task11")
    task11(A, N, M, 2)
    # print("task12")
    # task12(A, N, M)

    print("task15")
    task15(A, N, M, 4)
    print("task16")
    task16(A, N, M, 1)
    print("task17")
    task17(A, N, M, 2)
    print("task18")
    task18(A, N, M)
    print("task24")
    task24(A, N, M, 2, 3)
    print("task25")
    task25(A, N, M)
    print("task26")
    task26(A, N, M, 2, 3)
    print("task27")
    task27(A, N, M, 3)
    print("task28")
    task28(A, N, M, 1)
    print("task29")
    task29(A, N, M, 2)
    print("task30")
    task30(A, N, M)
    print("task31")
    task31(A, N, M)

    A = np.random.randint(1, 25, size=(N, M))
    print("task6")
    task6(A, N, M)
    print("task7")
    task7(A, N, M)

    B = np.random.random(size=(N, M))
    B *= 100
    B = np.around(B, decimals=2)
    print("task12")
    task12(B, N, M)
    print("task13")
    task13(B, N, M)
    print("task14")
    task14(B, N, M)

    A = np.random.randint(-15, 15, size=(N, N))
    print("task19")
    task19(A, N)
    print("task20")
    task20(A, N)
    print("task21")
    task21(A, N)
    print("task23")
    task23(A, N)

    A = np.random.randint(0, 2, size=(N, M))
    print("task22")
    task22(A, N, M)
