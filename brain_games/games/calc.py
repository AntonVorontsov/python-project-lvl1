import random

game_task = 'What is the result of the expression?'


def get_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operators = ["+", "-", "*"]
    operator = random.choice(operators)
    if operator == "+":
        correct_answer = num1 + num2
    elif operator == "-":
        correct_answer = num1 - num2
    else:
        correct_answer = num1 * num2
    question = f"{num1} {operator} {num2}"
    return question, correct_answer
