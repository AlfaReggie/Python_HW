# Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

def count_str_words(name_file):
    with open(name_file, 'r', encoding='UTF-8') as m_file:
        lines = 0
        words = 0
        symbols = 0
        for line in m_file:
            lines += 1
            words += len(line.split())
            symbols += len(line.strip('\n'))

    return f'Lines count: {lines}\nWords count: {words}\nSymbol count: {symbols}'

s_l = count_str_words('test_141_2.txt')
print(s_l)