number = 23

running = True

while running:
    guess = int(input('Enter an integer : '))

    if guess == number:
        print('Congratulations, you guessed it.')
        again = str(input('Play again? : [y/n]'))
        if again == 'y':
            running = True
        else:
            running = False
    elif guess > number:
        print('That guess is too high')
    else:
        print('You guess too low')
else:
    print('GAME OVER')
print('done')
