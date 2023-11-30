# Задача 3, Black Cat


def only_capital(filename):
    """Выводит в новый файл только слова с заглавной буквы из данного файла"""
    newly_generated_filename = filename.rstrip('.txt') + '_newly_generated.txt'
    with open(filename, 'r') as file, open(newly_generated_filename, 'x') as newly_generated_file:
        words_to_write = list(filter(lambda x: not x.islower() and not x == "--", file.read().split()))
        newly_generated_file.write('\n'.join(words_to_write))


only_capital('black_cat.txt')