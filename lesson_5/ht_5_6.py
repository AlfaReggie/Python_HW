# Создать (программно) текстовый файл, записать в него
# программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле
# и выводить её на экран.

from ht_5_1 import create_file, writeInF

name_f = input('Enter file name: ')
create_file(name_f)
nums = input("")
writeInF(name_f, nums)

def add_nmbr_f(name):
    sum = 0
    with open(name, 'r', encoding='UTF-8') as m_file:
        for line in m_file:
            nums = line.split()
            for j in nums:
                sum += int(j)
    return sum

sum_f = add_nmbr_f('123')
print(sum_f)


