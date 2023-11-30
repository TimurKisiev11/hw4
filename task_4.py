# Задача 4, JackHouse


def delete_empty_lines(filename):
    """Возвращает список со всеми непустыми строками из исходного файла"""
    lines = []
    with open(filename, 'r', encoding='utf-8') as file:
        while line := file.readline():
            if not line.strip(): continue
            lines.append(line.rstrip())
    return lines


def lines_to_add(lines):
    """На каждой итерации возвращает список строк для добавления к новому четверостишью
    и первую строку нового четверостишья"""
    lines_to_add = []
    lines_to_add.insert(0, 'Который построил Джек')  # Вводим вручную, т.к. нужно изменить строки
    lines_to_add.insert(0, 'В доме,')
    i = 2
    while i < len(lines) - 10:  # -10 т.к. последнее четверостишье в исходнике уже полное
        lines_to_add.insert(0, lines[i + 1])
        first_line_of_quatrain = lines[i]
        list = (lines_to_add, first_line_of_quatrain)
        yield list
        i += 2


def generate_a_file(filename, lines):
    """Создает файл, и выводит в него сгенерированное стихотворение"""
    newly_generated_filename = filename.rstrip('.txt') + '_newly_generated.txt'
    with open(newly_generated_filename, 'x', encoding='utf-8') as newly_generated_file:
        newly_generated_file.write(lines[0] + "\n" + lines[1] + "\n\n")  # в lines_lines_to_add первые 2 строки другие
        for j in lines_to_add(lines):
            newly_generated_file.write(j[1] + "\n")  # первая строка четверостишья
            for i in range(len(j[0])):
                newly_generated_file.write(j[0][i] + "\n")  # остальная часть, она каждый раз длиннее
            newly_generated_file.write("\n")


file_name = 'JackHouse2021.txt'
generate_a_file(file_name, delete_empty_lines(file_name))
