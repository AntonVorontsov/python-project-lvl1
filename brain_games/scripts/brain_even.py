# Вызов основного движка игр, использование специализированного модуля
# !/usr/bin/env python3

from brain_games.engine import make_game_run
from brain_games.games import even


def main():
    make_game_run(even)


if __name__ == "__main__":
    main()
