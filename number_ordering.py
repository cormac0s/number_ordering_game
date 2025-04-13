import pandas as pd
import random
import math
import numpy as np
import sys

def intro_prompt():
    print("""Hello, welcome to my number ordering game!\n")
    Here are the rules: \n
    1. You will start with 10 empty slots that you have to fill with randomly generated numbers in descending order.
    2. You will not be able to place numbers in the wrong order.
    3. You must fill all the slots to win. 
    4. Have fun!""")

def create_board(size = 10):
    return [" "] * size

def display_board(board):
    counter = 0
    for i in board:
        print(f"{counter+1}. {board[counter]}")
        counter+=1

def draw_number(number_list):
    if number_list == 0:  #initially check if there is anything left inside the number list
        return None
    
    number = random.choice(number_list) #gives us the random number
    number_list.remove(number) #removes the used number from the list

    return number

def place_number(board, num):

    while True:
        print(f"Place the number {num}")
        user_input = input("Enter index or quit to exit: ")
        
        if user_input.lower() == "quit": #checking if they want to quit
            print("Thanks for playing!")
            sys.exit()

        try:
            index = int(input(user_input))

            if 0 < index < len(board): #checkingfor valid range 
                board[index-1] = num
                return board
            else:
                print("Index out of range.")
        except ValueError:
            print("Invalid input.")

    
    '''try:
        index = int(input("Enter index: "))
        print(f"this is the intex I'm seeing {index}")
        if 0 <= index < len(board):
            if board[index] == " ":
                board[index] = num
            else:
                print("That spot is already taken.")
        else:
            print("Index is out of range.")

    except ValueError:
        if index == "quit":
            sys.exit()
        
        print("Not a number. Try again.")'''
    
    #return board



      


def main():
    numbers = list(range(1,101))
    game_board = create_board()
    
    intro_prompt()
    
    counter = 0
    while True:
        num = draw_number(numbers)
        display_board(game_board)
        game_board = place_number(game_board, num)
        

if __name__ == "__main__":
    main()