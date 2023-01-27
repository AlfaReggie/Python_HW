#Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.\n
#Для решения используйте цикл while и арифметические операции.

while True:
    user_num = input('Enter number: ')
    if user_num.isdigit():
        user_num = int(user_num)
        break
    print('Error enter!(alpha or number < 0')

tmp = user_num
max = 0
while tmp:
    tmp //= 10
    if tmp % 10 > max:
        max = tmp % 10

print(max)