from random import randint

DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def question():
    number: int = randint(1, 20)
    print(f'Question: {number}')
    return number


def get_right_answer(question_for_answer: str):
    return 'yes' if int(question_for_answer) % 2 == 0 else 'no'
