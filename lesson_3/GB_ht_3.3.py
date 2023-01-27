'''Реализовать функцию my_func(),
 которая принимает три позиционных аргумента и
  возвращает сумму наибольших двух аргументов.'''

def f_min(*args):
    result = float('inf')
    for itm in args:
        if itm < result:
            result = itm
    return result

def max_sum(*args):
    return sum(args) - min(args)

f2_sum = lambda *args: sum(args) - min(args)

res_f = f2_sum(3, 6, 2)
print(res_f)

assert f_min(3, 6, 2) == 2, 'False'
assert f_min(3, 6, 2) == 2, 'False'

assert max_sum(3, 6, 2) == 2, 'False'
assert max_sum(3, 6, 2) == 9, 'False'

assert f2_sum(3, 6, 2) == 2, 'False'
assert f2_sum(3, 6, 2) == 9, 'False'