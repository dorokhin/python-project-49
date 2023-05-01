#!/usr/bin/env python3
import prompt
import random


def get_username():
    print('Welcome to the Brain Games!')
    return prompt.string('May I have your name? ')


def print_help():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def print_welcome_message(user_name):
    print(f'Hello, {user_name}!')


def generate_number():
    return random.randint(0, 1000)


def print_question(num):
    print(f'Question: {num}')


def check_answer(user_ans, correct_ans):
    return user_ans == correct_ans


def is_even(number):
    return not bool(number % 2)


def get_correct_ans(number):
    if is_even(number):
        return 'yes'
    return 'no'


def get_user_input():
    answer = prompt.string('Your answer:')
    return answer


def validate_user_input(user_input):
    if (user_input == 'yes') or (user_input == 'no'):
        return True
    return False


def print_fail(user_name, user_ans, correct_ans):
    print(f"'{user_ans}' is wrong answer ;"
          f"(. Correct answer was '{correct_ans}'.")
    print(f"Let's try again, {user_name}!")


def print_congratulation(user_name):
    print(f"Congratulations, {user_name}!")


def main():
    user_name = get_username()
    print_help()
    for i in range(3):
        number = generate_number()
        print_question(number)
        ans = get_user_input()
        correct_ans = get_correct_ans(number)
        if not validate_user_input(ans):
            print_fail(user_name, ans, correct_ans)
            exit(0)
        if not check_answer(ans, correct_ans):
            print_fail(user_name, ans, correct_ans)
            exit(0)
        print('Correct!')
    print_congratulation(user_name)


if __name__ == '__main__':
    main()
