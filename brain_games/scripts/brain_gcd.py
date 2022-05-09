# Вызов основного движка игр, использование специализированного модуля
# !/usr/bin/env python3

from brain_games.engine import greeting
from brain_games.games import gcd


def main():
    greeting(gcd)


if __name__ == "__main__":
    main()
