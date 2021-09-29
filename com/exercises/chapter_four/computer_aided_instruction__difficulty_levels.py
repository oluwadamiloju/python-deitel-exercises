# 4.16 (Computer-Assisted Instruction: Difficulty Levels) Modify the previous exercise to allow the
# user to enter a difficulty level. At a difficulty level of 1, the program should use only single-digit
# numbers in the problems and at a difficulty level of 2, numbers as large as two digits.


import random


def random_number_generation():
    user_input = int(input("Enter a difficulty level: "))

    if user_input == 1:
        first_number = random.randrange(1, 10)
        second_number = random.randrange(1, 10)
    elif user_input == 2:
        first_number = random.randrange(1, 100)
        second_number = random.randrange(1, 100)
    else:
        raise ValueError("Enter 1 or 2 for a difficulty level")
    return first_number, second_number


def display_question(numbers):
    first_number, second_number = numbers
    print(f'How much is {first_number} times {second_number}?')


def correct_answer(numbers):
    first_number, second_number = numbers
    return first_number * second_number


def collect_answer():
    return int(input("Enter your answer: "))


def correct_answer_responses():
    x = ["Very good!", "Nice work!", "Keep up the good work!"]
    return random.choice(x)


def wrong_answer_responses():
    y = ["No. Please try again.", "Wrong. Try once more.", "No. Keep trying"]
    return random.choice(y)


def responses():
    if projected == actual:
        print(correct_answer_responses())
    else:
        print(wrong_answer_responses())


rnd = random_number_generation()
display_question(rnd)
actual = correct_answer(rnd)
projected = collect_answer()
responses()


for i in range(1, 10):
    while projected != actual:
        projected = collect_answer()
        responses()
    else:
        rnd = random_number_generation()
        display_question(rnd)
        actual = correct_answer(rnd)
        projected = collect_answer()
        responses()
