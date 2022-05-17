import prompt
ROUNDS_COUNT = 3


def make_game_run(game):
    """Функция, определяющая основную логику игр:
    - приветствие участника, запрос имени,
    - количество правильных ответов до окончания игры,
    - реакцию системы, в случае, если ответ верный или не верный"""
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")

    print(game.GAME_TASK)

    for _ in range(ROUNDS_COUNT):
        question, correct_answer = game.get_question_and_answer()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")

        if user_answer == correct_answer:
            print("Correct!")

        else:
            print(
                f"'{user_answer}' is wrong answer ;(."
                f" Correct answer was '{correct_answer}'."
                f"\nLet's try again, {name}!")
            break

    else:
        print(f"Congratulations, {name}!")
