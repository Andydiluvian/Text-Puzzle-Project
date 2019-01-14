import sys
print('What is your name?')
name = input()
print('Hello, ' + name + ". I've spun a riddle. Would you like to play? Yes or no?")

answer1 = input()
while answer1 != 'yes' and answer1 != 'no':
    print('Please answer yes or no.')
    answer1 = input()
if answer1 == 'yes':
    print('Let us begin.')
if answer1 == 'no':
    print('Good bye.')
    sys.exit()

print('What are we playing right now? A ___')
riddleOneAnswer = input()
while riddleOneAnswer != 'game':
    print('Try again.')
    print('What are we playing right now? A ___')
    riddleOneAnswer = input()
if riddleOneAnswer == 'game':
    print('That is correct!')

print('If you can not go below, where do you go?')
riddleTwoAnswer = input()
while riddleTwoAnswer != 'over':
        print('Try again.')
        print('If you can not go below, where do you go?')
        riddleTwoAnswer = input()
if riddleOneAnswer == 'over':
    print('That is correct!')

print('You have solved my riddle! Game over!')

