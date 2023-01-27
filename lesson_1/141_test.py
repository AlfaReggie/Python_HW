n = int(input('Enter weekday: '))

weekday_user = (n//6)
if weekday_user == 1:
    print('Holiday!')
else:
    print('Working day!')