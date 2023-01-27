# Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел,\n
# который не возрастает. У пользователя нужно запрашивать новый элемент рейтинга.\n
# Если в рейтинге существуют элементы с одинаковыми значениями,\n
# то новый элемент с тем же значением должен разместиться после них.

rait_list = [22, 6, 5]

while True:
    user_inp = input('Enter new rait: ')

    try:
        new_rait = abs(int(user_inp))
    except ValueError as error:
        if user_inp.lower() == 'q':
            print('Bye!')
            break
        print('Error enter!')
        continue

    new_rait_cnt = rait_list.count(new_rait)

    if not new_rait_cnt:
        if new_rait > rait_list[0]:
            rait_list.insert(0, new_rait)
        elif new_rait < rait_list[-1]:
            rait_list.append(new_rait)
        else:
            for idx, itm in enumerate(rait_list):
                if itm < new_rait:
                    rait_list.insert(idx, new_rait)
                    break
    else:
        end_idx = rait_list.index(new_rait) + new_rait_cnt
        rait_list.insert(end_idx, new_rait)

    print(rait_list)

