# Задача 2, Sub six

def display_words(filename):
    """Выводит в новый файл все слова <= 6 из данного файла"""
    sub_six_file_name = filename.rstrip('.txt') + '6.txt'
    with open(filename, 'r') as file, open(sub_six_file_name, 'x') as file_six:
        file_six.write(' '.join(list(filter(lambda x: len(x) <= 6, file.read().split()))))


display_words('poem.txt')
