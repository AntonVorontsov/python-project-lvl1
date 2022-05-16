import random

GAME_TASK = 'What number is missing in the progression?'


def get_question_and_answer():
    """Функция, реализующая игру "Арифметическая прогрессия" """
    progression_start = random.randint(1, 10)
    step = random.randint(1, 10)
    progression_finish = ((step * 10) + progression_start)
    progression = list(range(progression_start, progression_finish, step))
    random_index = random.randrange(len(progression))
    correct_answer = progression[random_index]
    progression[random_index] = '..'
    question = " ".join(map(str, progression))
    return str(question), str(correct_answer)
