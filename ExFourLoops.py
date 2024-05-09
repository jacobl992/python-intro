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
    # could use 'break' statement instead

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


#car game
command = ("")
car_stopped = True
car_started = False
while True:
    command = input("> ").lower()
    if command == 'start':
        if not car_started:
            print('Car started... ')
            car_started = True
            car_stopped = False
        else:
            print('Car already running')
    elif command == 'stop':
        if not car_stopped:
            print('Car stopped')
            car_stopped = True
            car_started = False
        else:
            print('Car already stopped.')
    elif command == 'help':
        print("""
start - to start the car
stop - to stop the car
help - for instructions
quit - to end game
        """)
    elif command == 'quit':
        break
    else:
        "Sorry, i don't understand that"