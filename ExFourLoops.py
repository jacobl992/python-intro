#while loop
i = 1
while i <= 5:
    print(i * '*')
    i += 1
print('done')

#guessing game
secret_number = 9
guess_count = 0
guess_limit = 3
correct_guess = False

while guess_count < guess_limit and not correct_guess:
    guess = int(input('Guess a number '))
    guess_count += 1
    if guess == secret_number:
        print('Correct. You win')
        correct_guess = True
    elif guess_count == guess_limit:
        print('Wrong, game over.')
    else:
        print('Wrong, try again')

