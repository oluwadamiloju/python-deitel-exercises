# 4.17 (Computer-Assisted Instruction: Varying the Types of Problems) Modify the previous exercise to
# allow the user to pick a type of arithmetic problem to study — 1 means addition problems only, 2 means
# subtraction problems only, 3 means multiplication problems only, 4 means division problems only
# (avoid dividing by 0) and 5 means a random mixture of all these types.


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


def question_types():
    return int(input("""Enter 1 for addition problems,
      2 for subtraction problems,
      3 for multiplication problems,
      4 for division problems,
      5 for all: """))


question_type = question_types()


def display_question(numbers):
    first_number, second_number = numbers

    if question_type == 1:
        print(f'How much is {first_number} plus {second_number}?')
    elif question_type == 2:
        print(f'How much is {first_number} minus {second_number}?')
    elif question_type == 3:
        print(f'How much is {first_number} times {second_number}?')
    elif question_type == 4:
        print(f'How much is {first_number} divided by {second_number}?')
    elif question_type == 5:
        print(f'How much is {first_number} plus {second_number}?')
        print(f'How much is {first_number} minus {second_number}?')
        print(f'How much is {first_number} times {second_number}?')
        print(f'How much is {first_number} divided by {second_number}?')


def correct_answer(numbers):
    first_number, second_number = numbers

    if question_type == 1:
        return first_number + second_number
    elif question_type == 2:
        return first_number - second_number
    elif question_type == 3:
        return first_number * second_number
    elif question_type == 4:
        return first_number / second_number
    elif question_type == 5:
        return first_number + second_number, first_number - second_number, \
               first_number * second_number, first_number // second_number


def collect_answer():
    if question_type == 1 or question_type == 2 or question_type == 3 or question_type == 4:
        return int(input("Enter your answer: "))
    elif question_type == 5:
        return int(input("Enter your answer to the addition problem: ")), \
               int(input("Enter your answer to the subtraction problem: ")), \
               int(input("Enter your answer to the multiplication problem: ")), \
               int(input("Enter your answer to the division problem: ")),


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
