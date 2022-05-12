# Вызов основного движка игр, использование специализированного модуля


# !/usr/bin/env python3

from brain_games.engine import game_logic
from brain_games.games import progression


def main():
    game_logic(progression)


if __name__ == "__main__":
    main()
