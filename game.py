print 'Welcome to cheza cheza game. Your going to guess a number between one and a hundred:'
guess = int(input('Guess a number:'))

numbers [] = number.guess

if guess <1 or guess >100:
    print 'Your guess is not between 1 and 100. You lose.'
else:
    print 'Your guess is correct. You win.'

def even_numbers():
    for number in numbers:
        if number % 2 == 0:
            print number
