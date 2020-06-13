from random import randint

import prompt


def question(number: int):
    print(f'Question: {number}')
    answer = prompt.string('Your answer: ')
    return answer


def check_answer(answer: str, right_answer: str):
    return True if answer == right_answer else False


def get_right_answer(number: int):
    return 'yes' if number % 2 == 0 else 'no'


def start_brain_even_game(name: str):
    right_answers = 0
    while right_answers < 3:
        number = randint(1, 20)
        answer = question(number)
        right_answer = get_right_answer(number)
        is_right_answer = check_answer(answer, right_answer)
        if not is_right_answer:
            print(f" '{answer}' is wrong answer ;(. Correct answer was '{right_answer}'.")
            break
        else:
            print('Correct!')
            right_answers += 1
    if right_answers == 3:
        print(f'Congratulations, {name}!')
