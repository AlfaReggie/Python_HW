# Для списка реализовать обмен значений соседних элементов.\n
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.\n
# При нечётном количестве элементов последний сохранить на своём месте.\n
# Для заполнения списка элементов нужно использовать функцию input().

a = [3, 4, 6, 7, 8]

idx = 0

while idx < len(a)-1:
    a[idx], a[idx + 1] = a[idx + 1], a[idx]
    idx += 2
print(a)