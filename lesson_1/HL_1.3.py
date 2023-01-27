a = []
b = []
lists = [a, b]
for x in range(len(lists)):
    num_f = input('Введите 1 если хотите выбрать разделитель, если нет что-то другое: ')
    try:
        num_f = int(num_f)
    except ValueError:
        continue
    if num_f == 1:
        sep = input("Enter separ. el. list ( , - default sep): , ; /")
        if sep != ',' and sep != ';' and sep != '/':
            sep = ','
    lists[x] = input('Enter elements list: ').split(sep)
    '''if num_f != 1:
        while True:
            inp_num = input('Ent number, or "s" that STOP: ')
            if inp_num == 's' or inp_num == 'S':
                break
            try:
                num = int(inp_num)
            except ValueError:
                continue
            lists[x].append(num)'''
print(a, b)

