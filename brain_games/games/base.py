import prompt


def get_user_answer():
    answer = prompt.string('Your answer: ')
    return answer


def check_answer(answer: str, right_answer: str):
    return True if answer == right_answer else False


def start_game(game, username: str) -> None:
    print(game.DESCRIPTION)
    right_answers = 0
    while right_answers < 3:
        question = game.question()
        answer = get_user_answer()
        right_answer = game.get_right_answer(question)
        is_right_answer = check_answer(answer, right_answer)
        if not is_right_answer:
            print(f" '{answer}' is wrong answer ;"
                  f"(. Correct answer was '{right_answer}'.")
            break
        else:
            print('Correct!')
            right_answers += 1
    if right_answers == 3:
        print(f'Congratulations, {username}!')
