import random

choices = ['paper', 'scissors', 'rock', 'end']
def choice_selection(choice):
    '''
    Takes a str choice of rock, paper or scissor and converts to integer
    parameter:
        choice(string) = what is chosen by the user
    return:
        count(int) = what is the int value associated with the choice
    '''
    count = 0
    if choice in choices:
        for options in choices:
            if choice == options:
                break

            else:
                count += 1
    else:
        count = 4
    return count

def int_to_choice(value):
    '''
    Converts from integers to the string equivalent
    paramter:
        value(int) = what is the integer of the selection
    returns:
        choice(str) = the string equivalent of the integer
    '''
    choice = choices[value]
    return choice


def invaild_selection():
    '''
    Function is void and only prints to tell the user they have made an invaild selection
    '''
    print('You\'ve made an invaild selection please select again')

def winner(first_selection, second_selection):
        '''
        Computes the winner of the game

        Parameters:
            first_selection(int) = what is the selection of the bot
            second_seleetion(int) = what is the selection of the player
        Returns:
            winner(str) = who won the game
        '''
        if (first_selection == 0) and (second_selection == 2):
            winner = "bot wins"
        elif (second_selection == 0) and (first_selection == 2):
            winner = "You win"
        elif first_selection > second_selection:
            winner = "bot wins"
        elif second_selection > first_selection:
            winner = 'You win'
        else:
            winner = 'tie'
        return winner

def main():
    user_choice = '0'
    while user_choice != 'end':
        comp_choice = random.randint(0,2)
        user_choice = choice_selection(input('\nType your choice or \'end\' to finish playing:').strip().lower())

        if user_choice == 4:
            invaild_selection()
            continue

        elif user_choice == 3:
            print('Thank you for playing')
            quit()
        print('')
        print(f'You chose {int_to_choice(user_choice)}, and the bot chose {int_to_choice(comp_choice)}.')
        print(winner(comp_choice, user_choice))
    
if __name__ == '__main__':
    main()

