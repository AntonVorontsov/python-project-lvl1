# Вызов основного движка игр, использование специализированного модуля
# !/usr/bin/env python3

from brain_games.engine import make_game_run
from brain_games.games import prime


def main():
    make_game_run(prime)


if __name__ == "__main__":
    main()
