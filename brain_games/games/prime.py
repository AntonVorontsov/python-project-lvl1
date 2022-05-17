import random
import math

GAME_TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(k):
    """Функция, проверяющая, простое ли число"""
    if k < 2:
        return False
    for i in range(2, int(math.sqrt(k)) + 1):
        if k % i == 0:
            return False
    return True


def get_question_and_answer():
    """Функция, реализующая игру "Простое ли число?" """
    question = random.randint(1, 100)
    correct_answer = 'yes' if is_prime(question) else 'no'
    return question, str(correct_answer)
