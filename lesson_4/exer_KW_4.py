from sys import argv

def my_sum(*args):
    return sum(args)

def devis(a, b):
    return a / b

def help():
    result = '''Command:
    \tdivisor принимает 2 аргумент
    \tsum принимает 2 и более аргументов'''
    print(result)

menu = {
    'devisor': devis,
    'sum': my_sum,
}

_, command, *args = argv

if command == 'help':
    help()
    exit(0)

args_good = True
for idx, itm in enumerate(args):
    try:
        args[idx] = float(itm)
    except ValueError:
        print('Enter error')
        args_good = not args_good
        break

if args_good:
    result = menu[command](*args)
    print(result)

print(command)
print(args)