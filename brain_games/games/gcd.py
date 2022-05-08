import random
from math import gcd

game_task = 'Find the greatest common divisor of given numbers.'


def get_question():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    correct_answer = gcd(num1, num2)
    question = f"{num1} {num2}"
    return question, correct_answer
