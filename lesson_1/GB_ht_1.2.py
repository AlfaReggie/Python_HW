#Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.\n
#Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

while True:
    user_num = input('Enter number: ')
    if user_num.isdigit():
        user_num = int(user_num)
        break
    print('Enter not correct: ')

cnt = 0
tmp = user_num

while tmp:
    tmp //= 10
    cnt += 1

nn_div = 10 ** cnt + 1
nnn_div = (10 ** (cnt * 2) + nn_div)

result = user_num + (user_num * nn_div) + (user_num * nnn_div)
print(result)

