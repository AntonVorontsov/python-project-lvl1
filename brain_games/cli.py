import prompt


def welcome_user():
    """Get an user name and promt user."""
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
