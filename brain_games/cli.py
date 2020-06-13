import prompt


def welcome_user(game_description: str = ''):
    print('Welcome to the Brain Games!')
    if game_description:
        print(game_description + '\n')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name
