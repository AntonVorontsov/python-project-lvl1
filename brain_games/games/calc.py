import random

game_task = 'What is the result of the expression?'


def get_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
# Определяем 2 случайных числа
    operators = ["+", "-", "*"]
# Определяем операторы для вычислений
    operator = random.choice(operators)
# Определяем случайный оператор
    if operator == "+":
        correct_answer = num1 + num2
    elif operator == "-":
        correct_answer = num1 - num2
    else:
        correct_answer = num1 * num2
    question = f"{num1} {operator} {num2}"
# формируем вопрос
    return question, correct_answer
