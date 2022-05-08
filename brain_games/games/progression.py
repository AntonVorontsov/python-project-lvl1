import random

game_task = 'What number is missing in the progression?'


def get_question():
    num1 = random.randint(1, 10)
    num3 = random.randint(1, 10)
    num2 = ((num3 * 10) + num1)
    question = list(range(num1, num2, num3))
    list_number = random.randrange(len(question))
    correct_answer = question[list_number]
    question[list_number] = 'X'
    return question, correct_answer
