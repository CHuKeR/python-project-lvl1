from brain_games.cli import welcome_user
from brain_games.games import brain_even
from brain_games.games.base import start_game


def main():
    name = welcome_user()
    start_game(brain_even, name)


if __name__ == '__main__':
    main()
