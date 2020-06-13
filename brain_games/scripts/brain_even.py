from brain_games.cli import welcome_user
from brain_games.games_logics.brain_even import start_brain_even_game


def main():
    name = welcome_user('Answer "yes" if number even otherwise answer "no".')
    start_brain_even_game(name)


if __name__ == '__main__':
    main()
