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

def place_number(board, num, counter):
    
    upper_check =  0
    lower_check = 0
    
    
    while True:
        
        place = input(f"Place {num} into an empty slot: ")
        if place.isdigit():
            place = int(place)
            if place < 1 or place > 10:
                print("Index out of range.")  
            elif board[place-1] != 0:
                print("You already filled that slot.")
            else:
                if counter > 0:
                    for i in range(place, len(board)):
                        if board[i] == 0:
                            continue
                        elif board[place] > board[i]:
                            print("That value is too large to be placed there.")
                            break
                        else:
                            lower_check = 1
                            break

                    for i in range(place, 0, -1):
                        if board[i] == 0:
                            continue
                        elif board[place] < board[i]:
                            print("That value is too small to be placed there.")
                            break    
                        else:
                            upper_check = 1
                            break
                    
                    
                else: 
                    board[place-1] = num
                    print("first case")
                    break
        else:
            print("Invalid input.")
        
        if lower_check == 1 and upper_check == 1:
            board[place-1] = num
            lower_check = 0
            upper_check = 0
            print("upper lower check")
            break
        
    
    print(board)
    return board
      
#def display_board(board):


def main():
    answer = "y"

    intro_prompt()
    main_board = create_board()
    
    global counter
    counter = 0
    while counter < len(main_board):
        rand_num = random_number()
        place_number(main_board, rand_num, counter)
        counter+=1
       

if __name__ == "__main__":
    main()