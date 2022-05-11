import random
from math import gcd

GAME_TASK = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    correct_answer = gcd(num1, num2)
    question = f"{num1} {num2}"
    return str(question), str(correct_answer)
