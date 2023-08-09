from random import choice



def game(count_user, count_comp):
        u_choice = input('Choose wisely...\nROCK\nPAPER\nSCISSORS\n').lower()
        comp_choice = choice([rock, paper, scissors])
        print(f'{user} chose {u_choice} and the computer chose {comp_choice}')

        if u_choice == comp_choice:
            print('----------TIE----------')

        
        elif u_choice == rock and comp_choice == scissors:
            print('----------Winner!!!----------')
            count_user+=1


        elif u_choice == rock and comp_choice == paper:
            print('----------Loser!!!----------')
            count_comp += 1

        
        elif u_choice == paper and comp_choice == scissors:
            print('----------Loser!!!----------')
            count_comp += 1

        
        elif u_choice == paper and comp_choice == rock:
            print('----------Winner!!!----------')
            count_user+=1

        
        elif u_choice == scissors and comp_choice == rock:
            print('----------Loser!!!----------')
            count_comp += 1


        elif u_choice == scissors and comp_choice == paper:
            print('----------Winner!!!----------')
            count_user+=1


        else:
            print("Enter a valid choice: ")
        
        scoreboard = f'{user}:{count_user}->->->->->->COMPUTER:{count_comp}'
        print(scoreboard)

        return count_user, count_comp
print('Welcome To....\nROCK\nPAPER\nSCISSORS!!!!!!!!!')
user = input('What is you name? ')

rock = 'rock'
paper = 'paper'
scissors= 'scissors'
comp_list = [rock,paper,scissors]
count_user = 0
count_comp = 0


while True:
    count_user, count_comp = game(count_user, count_comp)
    play_again = input('Do you want to play again? (y/n): ').lower()
    if play_again != 'y':
        print('Thanks for playing! Goodbye!')
        break