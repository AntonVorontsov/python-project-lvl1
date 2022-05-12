import random

GAME_TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():
    """Функция реализующая игру "Проверка на четность" """
    question = random.randint(1, 100)
    correct_answer = "no"
    if question % 2 == 0:
        correct_answer = "yes"
    return str(question), str(correct_answer)
