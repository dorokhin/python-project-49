#!/usr/bin/env python3
import prompt
import random


def get_username():
    print('Welcome to the Brain Games!')
    return prompt.string('May I have your name? ')


def print_help():
    print('What is the result of the expression?')


def print_welcome_message(user_name):
    print(f'Hello, {user_name}!')


def generate_question():
    operation = ['-', '+']
    return random.randint(0, 1000), random.randint(0, 1000), random.choice(operation)


def print_question(value_one, value_two, operation):
    print(f'Question: {value_one} {operation} {value_two}')


def check_answer(user_ans, correct_ans):
    return user_ans == correct_ans


def make_calc(value_one, value_two, operation):
    if operation == "-":
        return value_one - value_two
    elif operation == '+':
        return value_one + value_two


def get_correct_ans(value_one, valuer_two, operation, user_input):
    return make_calc(value_one, valuer_two, operation)


def get_user_input():
    answer = prompt.string('Your answer:')
    return answer


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
        value_one, value_two, operation = generate_question()
        print_question(value_one, value_two, operation)
        user_answer = int(get_user_input())
        correct_ans = get_correct_ans(value_one, value_two, operation, user_answer)
        if not check_answer(user_answer, correct_ans):
            print('check_answer >>>')
            print_fail(user_name, user_answer, correct_ans)
            exit(0)
        print('Correct!')
    print_congratulation(user_name)


if __name__ == '__main__':
    main()
