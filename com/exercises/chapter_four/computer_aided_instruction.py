# 4.14 (Computer-Assisted Instruction) Computer-assisted instruction (CAI) refers to the use of computers
# in education. Write a script to help an elementary school student learn multiplication. Create a
# function that randomly generates and returns a tuple of two positive one-digit integers. Use that
# function’s result in your script to prompt the user with a question, such as
#                 How much is 6 times 7?
# For a correct answer, display the message "Very good!" and ask another multiplication question. For an
# incorrect answer, display the message "No. Please try again." and let the student try the same question
# repeatedly until the student finally gets it right.


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


actual = correct_answer(rnd)
projected = collect_answer()

if projected == actual:
    print("Very good!")
else:
    print("No. Please try again.")

while projected != actual:
    projected = collect_answer()
    if projected == actual:
        print("Very good!")
    else:
        print("No. Please try again.")
else:
    rnd = random_number_generation()
    display_question(rnd)
    actual = correct_answer(rnd)
    projected = collect_answer()
    if projected == actual:
        print("Very good!")
    else:
        print("No. Please try again.")
