'''Выполнить функцию, которая принимает несколько параметров, описывающих
данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Осуществить вывод данных о пользователе одной строкой'''

def user_data(**kwargs) -> str:
    '''
    :param name: str
    :param surname: str
    :param birth_year: int
    :param city: str
    :param email: str
    :param phone: int
    :return: str
    '''

    name = kwargs.get('name', '')
    surname = kwargs.get('surname', '')
    birth_year = kwargs.get('birth_year', '')
    city = kwargs.get('city', '')
    email = kwargs.get('email', '')
    phone = kwargs.get('phone', '')

    return f'{name} {surname} {birth_year} {city} {email} {phone}'