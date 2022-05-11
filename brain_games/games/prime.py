import random

GAME_TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def isprime(k):
    if k==2 or k==3: return True
    if k%2==0 or k<2: return False
    for i in range(3, int(k**0.5)+1, 2):
        if k%i==0:
            return False
    return True


def get_question_and_answer():
    question = random.randint(1, 100)
    correct_answer = "no"
    if isprime(question) is True:
        correct_answer = "yes"
    return str(question), str(correct_answer)
