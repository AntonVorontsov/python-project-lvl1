import random

game_task = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question():
    question = random.randint(1, 100)
    correct_answer = "no"
    k = 0
    for i in range(2, question // 2 + 1):
        if (question % i == 0):
            k = k + 1
    if (k <= 0):
        correct_answer = "yes"
    return question, correct_answer
