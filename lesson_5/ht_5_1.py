"""Создать программный файл в текстовом формате, записать в него построчно
 данные, вводимые пользователем. Об окончании ввода данных будет
 свидетельствовать пустая строка."""
import os.path

def create_file(name_file):
    return os.path.join(os.path.dirname(__file__), f'{name_file}.txt')

def writeInF(name_file, us_entr):
    with open(name_file, 'a+', encoding='UTF-8') as m_file:
        m_file.write(f'{us_entr}\n')
    return m_file


'''answ_user = input("Enter y if you want create file and write anything in file: ")
if answ_user.lower() == 'y':
    name_file = input('Enter name file: ')
    file_user = create_file(name_file)
    while True:
        user_enter = input('Enter surname and prem: ')
        if not user_enter:
            break
        else:
            writeInF(file_user, user_enter)'''


