#----------------------------------------------------
# Assignment 3: Assignment 3 (main game function)
#
# Author: Khanh Bui
# Collaborators/references: Discord help to understand the idea of tasks
#----------------------------------------------------
# import AbacoStack, Card from Abaco.py  
from AbacoStack import AbacoStack, Card

# Task 4: The game represent the whole assignment 3 game. Play in this py file
# Input: N/A
# Ouput: N/A 
def main(): # main represent for the whole game # Not Done
    # Variable
    game_continue = True
    stack_num = input("Enter the desired number of stack for the game: ")
    while stack_num.isnumeric() == False or int(stack_num) < 2 or int(stack_num) > 6:
        print("The input have to be an int and number of stack range within 2 to 5 only")
        stack_num = input("Enter the desired number of stack for the game: ")

    depth = input("Enter the desired depth for the game: ")
    while depth.isnumeric() == False or int(depth) < 2 or int(depth) > 4:
        print("The input have to be an int and the depth within the range from 2 to 4")
        depth = input("Enter the desired depth for the game: ")

    # generate game object, reset card and make valid move list
    game = AbacoStack(int(stack_num), int(depth))
    card = Card(int(stack_num), int(depth))
    card.reset()
    valid_move_list = []

    # main game while loop
    while game_continue == True :
        valid_command_list =  ["u","d","r","l"]
        game.show(card)
        print("[Player can print max moves of 5 * seperate with space*, Q for quit and R to reset]")
        player_input = input("Enter your move(s) : ")
        if player_input.lower() == "q":
            game_continue = False
        elif player_input.lower() == "r":
            game.reset()
        else: # player chose a move other than q and r
            split_player_input = player_input.split()
            if len(split_player_input) > 5:
                split_player_input = split_player_input[:5]  
            
            try:
                for move in split_player_input:
                    game.moveBead(move)
                    valid_move_list.append(move)
            except:
                print("ERROR: invalid move")
                    
            if game.isSolved(card) == True:
                print("@@Congrat! you won@@")
                print("Card solved")
                card.show()
                print("moves made: " + str(valid_move_list))
                player_input = input("Would you would like to get another configuration card to attempt (Y/N): ")
                if player_input.lower() == "y":
                    card.reset()
                    game.reset()
                    print(game.isSolved(card))
                elif player_input.lower() == "n":
                    game_continue = False
                else:
                    print("Unrecognized command")
                    player_input = input("Would you would like to get another configuration card to attempt (Y/N): ")

    print("----- Game ended, Thank for playing -----")
if __name__ == "__main__":  
    main()            