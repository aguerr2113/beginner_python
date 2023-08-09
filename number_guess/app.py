from random import randint

lower_num, higher_num = 1,100
random_number=int(randint(lower_num,higher_num))
print(f'Guess the number in the range from {lower_num} to {higher_num}.')

while True:
    try:
        user_guess=(int(input('Guess: ')))
    except ValueError as e:
        print('Please a valid Number.')
        continue

    if user_guess > random_number:
        print('The number is lower')
    elif user_guess < random_number:
        print('The number is higher')
    else:
        print(f'You Guessed it, the number was {random_number}!!')
        break

