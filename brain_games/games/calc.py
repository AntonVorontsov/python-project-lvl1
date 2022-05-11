import random

GAME_TASK = 'What is the result of the expression?'


def get_question_and_answer():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operators = ["+", "-", "*"]
    random_operator = random.choice(operators)
    if random_operator == "+":
        correct_answer = num1 + num2
    elif random_operator == "-":
        correct_answer = num1 - num2
    elif random_operator == "*":
        correct_answer = num1 * num2
    question = f"{num1} {random_operator} {num2}"
    return str(question), str(correct_answer)
