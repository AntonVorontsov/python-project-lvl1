import prompt


def greeting(game):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")

    print(game.game_task)

    NUMBER_OF_ROUNDS = 3
    correct_answers = 0

    while correct_answers < NUMBER_OF_ROUNDS:
        question, correct_answer = game.get_question()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")

        if user_answer == str(correct_answer):
            print("Correct!")
            correct_answers += 1

        else:
            correct_answers = 0
            print(
                f"'{user_answer}' is wrong answer ;(."
                f" Correct answer was '{correct_answer}'."
                f"\nLet's try again, {name}!")

    return print(f"Congratulations, {name}!")
