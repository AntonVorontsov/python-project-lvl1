import random
import math

GAME_TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(k):
    """Функция, проверяющая, простое ли число"""
    if k == 2 or k == 3:
        return True
    if k % 2 == 0 or k < 2:
        return False
    for i in range(3, int(math.sqrt(k)) + 1):   #удалил аргумент 2, как было указано в Вашем примере. С ним была бы проверялись только четные часла - функция работала бы быстрее
        if k % i == 0:
            return False
    return True


def get_question_and_answer():
    """Функция, реализующая игру "Простое ли число?" """
    question = random.randint(1, 100)
    correct_answer = 'yes' if is_prime(question) else 'no'
    return str(question), str(correct_answer)
