# Задача 5, Console Quiz


def game(lines):
    questions = [lines[j] for j in range(0, len(lines), int(len(lines)/12))]  # тут лежат строки с вопросами
    answers = [[lines[j + k] for k in range(1, 5)] for j in range(0, len(lines), int(len(lines) / 12))]  # тут лежат списки с вариантами ответов (по 4 в каждом)
    right_answers = [lines[j+5] for j in range(0, len(lines), int(len(lines)/12))]  # тут лежат правильные ответы
    i = 0
    game_status = True
    while game_status:
        print(questions[i])  # выводим вопрос
        for j in range(4):  # выводим 4 варианта ответа
            print(str(j + 1) + "). " + answers[i][j])
        solution = input("Введите номер верного ответа -> ")
        if right_answers[i] == solution and not i == 11:  # если ответ верный и ещё не конец игры
            print("Верно")
            i += 1
        elif solution == "0":  # если ввели "0" - игра закончена
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


with open('qustions.txt', 'r', encoding='utf-8') as file:
    lines = [line.rstrip() for line in file if line.strip()]

game(lines)
