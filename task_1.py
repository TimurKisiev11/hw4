# Задача 1, Frequency

def frequency(filename):
    """Считает частоту вхождения слов в файл, возвращает словарь"""
    word_frequency = {}  # словарь для хранения частоты слов
    with open(filename, 'r') as file:
        for line in file:
            words = line.lower().strip().split()  # разделяем строку на слова
            for word in words:
                word = word.strip('.?,;:()[]\/'"")
                word_frequency[word] = word_frequency.get(word, 0) + 1  # увеличиваем счетчик для каждого слова
    return word_frequency


word_frequency = frequency('poem.txt')
print(word_frequency)
