number = 23

guess = int(input('Enter an integer : '))

if guess == number:
    print('Congratulations, you guessed correctly!')
    print('But no prizes')
    if guess % 2:
        print('number is odd')
    else:
        print('number is even')
elif guess < number:
    print('You guessed too low')
else:
    print('That guess is too high')
print('Done')
