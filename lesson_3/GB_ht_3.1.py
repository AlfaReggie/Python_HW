'''Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
обработку ситуации деления на ноль.'''

def devid_nums(a: float, b: float) -> float:
    '''
    funk devided user numbers
    :param a:
    :param b:
    :return:
    '''
    try:
        return a / b
    except ZeroDivisionError as e:
        print("Can't devided on zero!")

assert devid_nums(4, 2) == 2, 'Error!'
assert devid_nums(0, 2) == 1, '!!Error!!'
