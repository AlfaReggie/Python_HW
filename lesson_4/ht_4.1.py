# Реализовать скрипт, в котором должна быть предусмотрена функция расчёта
# заработной платы сотрудника. Используйте в нём формулу:
# (выработка в часах*ставка в час) + премия.
# Во время выполнения расчёта для конкретных значений необходимо
# запускать скрипт с параметрами.
from sys import argv

def unit_salary(name: str, surname: str, prodInHours: float, payPerHour: float, prem: float) -> set:
        return name, surname, prodInHours * payPerHour + prem

_, name, surname, prodInHours, payPerHour, prem, *__ = argv

try:
    result = unit_salary(str(name), str(surname), float(prodInHours), float(payPerHour), float(prem))
    print(result)
except ValueError as e:
        print("Enter ")
        print(e)
