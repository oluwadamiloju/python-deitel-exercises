# 4.15 (Computer-Assisted Instruction: Reducing Student Fatigue) Varying the computer’s responses can
# help hold the student’s attention. Modify the previous exercise so that various comments are displayed
# for each answer. Possible responses to a correct answer should include 'Very good!', 'Nice work!' and
# 'Keep up the good work!' Possible responses to an incorrect answer should include
# 'No. Please try again.', 'Wrong. Try once more.' and 'No. Keep trying.' Choose a number from 1 to 3,
# then use that value to select one of the three appropriate responses to each correct or incorrect answer.


import random


def random_number_generation():
    first_number = random.randrange(1, 10)
    second_number = random.randrange(1, 10)
    return first_number, second_number


def display_question(numbers):
    first_number, second_number = numbers
    print(f'How much is {first_number} times {second_number}?')


rnd = random_number_generation()
display_question(rnd)


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


actual = correct_answer(rnd)
projected = collect_answer()
responses()

while projected != actual:
    projected = collect_answer()
    responses()


while projected == actual:
    rnd = random_number_generation()
    display_question(rnd)
    actual = correct_answer(rnd)
    projected = collect_answer()
    responses()
