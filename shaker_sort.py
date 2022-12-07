def shaker_sort(A):
    length = len(A)
    swapped = True
    start_index = 0
    end_index = length - 1

    while (swapped == True):

        swapped = False

        # проход слева направо
        for i in range(start_index, end_index):
            if (A[i] > A[i + 1]):
                # обмен элементов
                A[i], A[i + 1] = A[i + 1], A[i]
                swapped = True

        # если не было обменов прерываем цикл
        if (not (swapped)):
            break

        swapped = False

        end_index = end_index - 1

        # проход справа налево
        for i in range(end_index - 1, start_index - 1, -1):
            if (A[i] > A[i + 1]):
                # обмен элементов
                A[i], A[i + 1] = A[i + 1], A[i]
                swapped = True

        start_index = start_index + 1
    return A