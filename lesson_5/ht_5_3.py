# Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч,
# вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.

import os.path

def count_str_words(n_f):
    with open(n_f, 'r', encoding='UTF-8') as m_file:
        my_dict = dict()
        for i in m_file:
            words = i.split()
            for j in words:
                if j.isalpha():
                    t_key = j
                if j.isdigit():
                    t_value = int(j)
            my_dict[t_key] = t_value
    return my_dict

def prem(name_file):
    a = count_str_words(name_file)
    for key, value in a.items():
        if value >= 20000:
            yield key, value


u = list(prem('person_prem.txt'))
print(u)