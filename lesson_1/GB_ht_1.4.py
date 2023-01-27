# Спортсмен занимается ежедневными пробежками.\n
# В первый день его результат составил a километров.\n
# Каждый день спортсмен увеличивал результат на 10% относительно предыдущего.\n
# Требуется определить номер дня, на который результат спортсмена\n
# составит не менее b километров. Программа должна принимать\n
# значения параметров a и b и выводить одно натуральное число — номер дня.

while True:
    first_d_res = input('Enter first day result: ')
    second_d_res = input('Enter secound day result: ')
    if first_d_res.isdigit() & second_d_res.isdigit() or first_d_res >= second_d_res:
        first_d_res = int(first_d_res); second_d_res = int(second_d_res)
        break
    print('Error enter!')

day = 1
while first_d_res < second_d_res:
    first_d_res = first_d_res + first_d_res * 0.1
    day += 1

print(first_d_res, day)


