# Реализовать структуру данных «Товары». Она должна представлять собой \n
# список кортежей. Каждый кортеж хранит информацию об отдельном товаре.\n
# В кортеже должно быть два элемента — номер товара и словарь с параметрами,\n
# то есть характеристиками товара:
# название, цена, количество, единица измерения. \n
# Структуру нужно сформировать программно, запросив все данные у пользователя.

prod_template = {
    'name': ('prod. name', str),
    'price': ('price', int),
    'count': ('count', int),
    'unts': ('units', str)
}

next_enter = True

auto_inc = 1
prod_list = []

while next_enter:
    product = {}

    for key, value in prod_template.items():
        while True:
            user_value = input(f'{value[0]}\n')
            try:
                user_value = value[1](user_value)
            except ValueError as e:
                print(f"{e}\nNot correct error data")
                continue
            product[key] = user_value
            break

    prod_list.append((auto_inc, product))
    auto_inc += 1

    while True:
        next_add = input("Enter next data? Y/N\n")
        if next_add.lower() in ('y', 'n'):
            next_enter = next_add.lower() == 'y'
            break
        else:
            print('Not correct enter!')

print(prod_list)

prouct_analist = {}

for key in prod_template:
    result = []
    for itm in prod_list:
        result.append(itm[1][key])
    prouct_analist[key] = result

print(prouct_analist)