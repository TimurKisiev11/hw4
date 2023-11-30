# Задача 4, JackHouse


def lines_to_add(lines):
    """На каждой итерации возвращает список строк для добавления к новому четверостишью
    и первую строку нового четверостишья"""
    lines_to_add = ['В доме,', 'Который построил Джек'] # Вводим вручную, т.к. нужно изменить строки
    for i in range(2, len(lines) - 10, 2):
        lines_to_add.insert(0, lines[i + 1])
        first_line_of_quatrain = lines[i]
        yield lines_to_add, first_line_of_quatrain


def generate_a_file(filename):
    """Создает файл, и выводит в него сгенерированное стихотворение"""
    newlygenerated_filename = filename.rstrip('.txt') + 'newlygenerated.txt'
    with open(filename, 'r', encoding='utf-8') as file, open(newlygenerated_filename, 'x', encoding='utf-8') as newlygenerated_file:
        lines = [line.rstrip() for line in file if line.strip()]
        newlygenerated_file.write(lines[0] + "\n" + lines[1] + "\n\n")  # в lines_to_add первые 2 строки другие
        for j in lines_to_add(lines):
            newlygenerated_file.write(j[1] + "\n")  # первая строка четверостишья
            for line in j[0]:
                newlygenerated_file.write(line + "\n")  # остальная часть, она каждый раз длиннее
            newlygenerated_file.write("\n")


generate_a_file('JackHouse2021.txt')
