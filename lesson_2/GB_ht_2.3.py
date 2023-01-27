# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.\n
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).\n
# Напишите решения через list и dict.
my_ses = ('Wnt', 'Spr',
          'Smr', 'Atm')

while True:
    month_user = input('Enter month number: ')
    if month_user.isdigit():
        month_user = int(month_user)
        print(my_ses[month_user // 3 % 4])
    else:
        break



