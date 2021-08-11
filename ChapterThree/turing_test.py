"""turing test for medical diagnosis"""

first_statement = input('What is your problem?')
second_statement = input('Have you had this problem before (yes or no)?')

if second_statement == 'yes':
    print('Well, you have it again.')
elif second_statement == 'no':
    print('Well, you have it now.')
else:
    print('Simple question, yes or no?')
