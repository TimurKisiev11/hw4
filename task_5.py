import numpy as np


def delete_empty_lines(filename):
    """Возвращает список со всеми непустыми строками из исходного файла"""
    lines = []
    with open(filename, 'r', encoding='utf-8') as file:
        while line := file.readline():
            if not line.strip(): continue
            lines.append(line.rstrip())
    return lines


file_name = 'qustions.txt'
newly_generated_filename = file_name.rstrip('.txt') + '_newly_generated.txt'
lines = delete_empty_lines(file_name)


def game(lines):
    questions = []  # тут лежат строки с вопросами
    answers = []  # тут лежат списки с вариантами ответов (по 4 в каждом)
    right_answers = []  # тут лежат правильные ответы
    for j in range(0, 72, 6):
        questions.append(lines[j])
        part_answers = []
        for k in range(1, 5):
            part_answers.append(lines[j + k])
        answers.append(part_answers)
        right_answers.append(lines[j + 5])
    i = 0
    game_status = True
    while game_status:
        print(questions[i])  # выводим вопрос
        for j in range(4):   # выводим 4 варианта ответа
            print(str(j + 1) + "). " + answers[i][j])
        solution = input("Введите номер верного ответа -> ")
        if solution.__eq__(right_answers[i]) and not i == 11:  # если ответ верный и ещё не конец игры
            print("Верно")
            i += 1
        elif solution.__eq__("0"):  # если ввели "0" - игра закончена
            print("Не хотите играть, и не надо. Игра окончена.")
            break
        elif i == 11:  # если все ответы верны игра закончена
            print("Игра пройдена")
            game_status = False
        elif solution in right_answers:  # если ответ неверен, но он 1, 2, 3 или 4, уходим в начало
            print("Неверно, начните игру заново")
            i = 0
        else:  # если введен некорректный ответ (не 1, 2, 3, 4), уходим в начало
            print("Ошибка, введите ответ заново")
            pass


game(lines)
