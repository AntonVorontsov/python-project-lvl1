import random

GAME_TASK = 'What number is missing in the progression?'


def get_question_and_answer():
    prog_start = random.randint(1, 10)
    step = random.randint(1, 10)
    prog_finish = ((step * 10) + prog_start)
    question = list(range(prog_start, prog_finish, step))
    hidden_number = random.randrange(len(question))
    correct_answer = question[hidden_number]
    question[hidden_number] = 'X'
    return str(question), str(correct_answer)
