# Задача 2, Sub six

def display_words(filename):
    """Выводит в новый файл все слова <= 6 из данного файла"""
    sub_six_file_name = filename.rstrip('.txt') + '6.txt'
    with open(filename, 'r') as file, open(sub_six_file_name, 'x') as file_six:
        words = file.read().split()
        words_to_write = [word for word in words if len(word) <= 6]
        file_six.write(' '.join(words_to_write))


display_words('poem.txt')
