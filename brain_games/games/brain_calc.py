from random import choice, randint

DESCRIPTION = 'What is the result of the expression?'


def question():
    operation = choice(['+', '-', '*'])
    number1 = randint(0, 20)
    number2 = randint(0, 20)
    question_str = f'{number1}{operation}{number2}'
    print(f'Question: {question_str}')
    return question_str


def get_right_answer(question_for_answer) -> str:
    return str(eval(question_for_answer))
