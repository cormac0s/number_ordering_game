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

def create_board():
    board = [0] *10
    #print(board)
    return board

def random_number():
    number = random.randint(1,100)
    return number

def place_number(board, num):
    placement_tracker = 0
    
    while True:
        
        place = input(f"Place {num} into an empty slot: ")
        if place.isdigit():
            place = int(place)
            if place < 1 or place > 10:
                print("Index out of range.")  
            elif board[place-1] != 0:
                print("You already filled that slot.")
            else:
                board[place-1] = num
                placement_tracker +=1
                break
                  
        else:
            print("Invalid input.")
    
    print(board)
    return board
      
#def display_board(board):


def main():
    answer = "y"

    intro_prompt()
    main_board = create_board()
    
    counter = 0
    while counter < 10:
        rand_num = random_number()
        place_number(main_board, rand_num)
        counter+=1
       

if __name__ == "__main__":
    main()