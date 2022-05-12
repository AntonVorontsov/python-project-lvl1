import random

GAME_TASK = 'What number is missing in the progression?'


def get_question_and_answer():
    """Функция, реализующая игру "Арифметическая прогрессия" """
    prog_start = random.randint(1, 10)
    step = random.randint(1, 10)
    prog_finish = ((step * 10) + prog_start)
    progression = list(range(prog_start, prog_finish, step))
    hidden_number = random.randrange(len(progression))
    correct_answer = progression[hidden_number]
    progression[hidden_number] = '..'
    question = " ".join(map(str, progression))
    return str(question), str(correct_answer)
