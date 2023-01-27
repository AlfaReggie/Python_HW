'''sep = input("Enter separ. el. list ( , - default sep): , ; /")
if sep != ',' and sep != ';' and sep != '/':
    sep = ','
listEl = input('Enter elements list: ').split(sep)
print(listEl)

for i in range(len(listEl) - 1):
    if i < len(listEl):
        j = i + 1
        while j < len(listEl):
            if listEl[i] == listEl[j]:
                listEl.pop(j)
            else:
                j += 1

print(listEl)'''

num_1 = int(input('Enter number: '))
print(num_1)

