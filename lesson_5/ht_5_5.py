# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

import re
import os
from translate import Translator
translator = Translator(to_lang='Rus')


from ht_5_1 import create_file, writeInF

with open('test_test.txt', 'r', encoding='UTF-8') as m_file:
    for i in m_file:
        words = i.split()
        for j in words:
            file_name = create_file(j)
            x = re.findall(r'\w+\_', j)
            y = re.findall(r'\d+', j)
            translation = translator.translate(f'{j[:-2]}')
            writeInF(j, f'{translation}_{y[0]}')


