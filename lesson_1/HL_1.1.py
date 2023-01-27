a = []
while True:
    inp_num = input('Ent: ')
    if inp_num == 's' or inp_num == 'S':
        break
    try:
        num = int(inp_num)
    except ValueError:
        continue
    size = len(a)

    if size == 0:
        a.append(num)
    else:
        for i in range(size):
            if num < a[i]:
                a.insert(i, num)
                break
    if len(a) == size:
        a.append(num)

print(a)