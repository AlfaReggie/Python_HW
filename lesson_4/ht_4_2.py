# Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
# Для его формирования используйте генератор.

from sys import argv

def test_iter(*args):
    prev = float('inf')
    for num in args:
        if num > prev:
            yield num
        prev = num

_, *args = argv

if __name__ == '__main__':
    assert list(test_iter(1, 2, 3, 4, 5, 3, 4, 5)) == [2, 3, 4, 5, 4, 5], 'False'
    assert list(test_iter(-1, 3, 3, 12, -5, 3, 4, 5)) == [3, 12, 3, 4, 5]

def test_iter_2(*args):
    res = [itm for idx, itm in enumerate(args) if idx and itm > args[idx - 1]]
    print(res)





