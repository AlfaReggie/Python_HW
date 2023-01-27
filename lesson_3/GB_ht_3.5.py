# Программа запрашивает у пользователя строку чисел, разделённых пробелом.\
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить
# ввод чисел, разделённых пробелом и снова нажать Enter. Сумма вновь введённых чисел
# будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введён после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной
# ранее сумме и после этого завершить программу.

def insert_sum(*args):
    res = 0
    exit_flag = False
    for itm in args:
        try:
            res += float(itm) if itm else 0
        except ValueError as e:
            if itm == 'q':
                exit_flag = not exit_flag
                break
    return res, exit_flag

user_sum = 0
while True:
    user_inp = input('Enter nums with split: ').split(' ')
    res_sum, user_exit = insert_sum(*user_inp)
    user_sum += res_sum
    print(user_sum)

    if user_exit:
        print('Bye')
        break