import os
from pathlib import Path

file_name = 'tes.txt'
file_path = os.path.join(os.path.dirname(__file__), file_name)

file_path_lib = Path(__file__).parent.joinpath(file_name)

print(f'Path - {file_path}')
print(f'Path_lib - {file_path_lib}')

file = open(file_path_lib, 'r', encoding='UTF-8')

'''for i in file:
    print(i, end='')'''

'''try:
    tmp = file.read()
except IOError as e:
    print(e)
finally:
    file.close()
'''

'''with open(file_path_lib):
    file.seek(8)
    print(file.read(2))
    print(file.read(2))
    print(file.tell())
    file.seek(4)
    print(file.tell())'''

'''file_str = '+++++'

with open(file_path_lib, 'r+', encoding = 'UTF-8') as file:
    file.seek(3)
    print(file.tell())
    file.write(file_str)'''

import json

some_list = ['sm', 1, 2, 3, 4, 'хзщхйцщухзйщфдлыжвббючяьсбм', [1, 2, 5, 2], True, {'k1': 1, 'k2': 2}, (1, 2, 4, 5)]
'''j_data = json.dumps(some_list)
print(j_data)'''

'''with open(file_path_lib.parent.joinpath('test.json'), 'w', encoding='UTF-8') as file:
    file.write(j_data)'''

'''with open(file_path_lib.parent.joinpath('test.json'), 'r', encoding='UTF-8') as file:
    read_f = json.loads(file.read())

print(type(read_f))
print(read_f)'''

'''with open(file_path_lib.parent.joinpath('test.json'), 'w', encoding='UTF-8') as file:
    json.dump(some_list, file, ensure_ascii=False)'''

import requests

responce = requests.get('https://geekbrains.ru/')

'''with open(file_path_lib.parent.joinpath('ya.htm'), 'w', encoding='UTF-8') as file:
    file.write(responce.text)
'''

img_url = 'https://www.callofduty.com/content/dam/atvi/callofduty/cod-touchui/mw2/home/reveal/new-era/new_era-mw2.jpg'

responce_2 = requests.get(img_url)
with open(file_path_lib.parent.joinpath('141.jpg'), 'wb') as file:
    file.write(responce_2.content)