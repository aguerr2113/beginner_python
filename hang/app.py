from random import choice
def run_game():
    word = choice(['apple','secret','banana'])
    user=input('What is you name? ')
    print(f'Welcome to hagman, {user}')
    tries = 3
    guessed = ''
    while tries > 0:
        blanks = 0
        print('Word: ',end='')
        for char in word:
            if char in guessed:
                print(char, end='')
            else:
                print('_', end='')
                blanks += 1

        print()

        if blanks == 0:
            print('You got it!')
            break
        guess = input('Enter a letter: ')
        if guess in guessed:
            print(f'You already guessed {guess}.Please try another letter')

        else:

            guessed += guess

        if guess not in word:
            tries -= 1
            print(f'Sorry, that was wrong... ({tries} tries remaining)')

            if tries == 0:
                print('no more tries remaining')
                break
if __name__ == '__main__':
    run_game()  
    