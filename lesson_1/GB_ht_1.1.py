#Пользователь вводит время в секундах. Переведите время в часы\n
#минуты, секунды и выведите в формате чч:мм:сс.Используйте форматирование строк.

while True:
    user_sec = input('Enter second count: ')
    if user_sec.isdigit():
        user_sec = int(user_sec)
        break
    else:
        print('Enter not correct! ')

print(f'time: {user_sec // 3600}:{user_sec % 3600 // 60}:{user_sec % 3600 % 60}')
