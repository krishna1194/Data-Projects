#!/usr/bin/env python
# coding: utf-8

# <!-- # Overall understanding of Problem Statement
# 
# Implement a simple tic-tac-toe game to allow two individuals to play one another. 
# 
# ## Introduction
# 
# 1. Implement a program that tracks the state of an ongoing tic-tac-toe game.
# 2. Allow each player to choose the position they want to place their pieces.
# 3. Check and end the game when either a win or a tie occurs.
# 4. MUST use the identifiers A1, A2 and so on to refer to squares on the board.
# 
# ## Basic Game Loop
# The game loop for a tic-tac-toe game is fairly simple.
# 
# 1. Initialize the board to be empty.
# 2. X starts, and chooses a position to place their marker.
# 3. O positions their marker in any empty position.
# 4. After each marker is placed, a check is made to see whether either player has won.
# 5. Placement alternates until a player wins or the board is full, at which point the game is called for a tie.
# 
# The reason you would break down the game like this isn't that you don't know tic-tac-toe, but because this gives you a fairly good idea of what you need to do to program Python to play a tic-tac-toe game. This is a common strategy for larger programs, take each problem and break it down into a sequence of sub-problems until you feel comfortable that you understand how to write code to solve each sub-problem. If our breakdown above is still too high level, keep decomposing it until to get to a point where you feel like you understand how to convert each description into a corresponding block of code.
# 
# 
# ## Interface
# Board Positions.  Because we'll be marking your programs electronically, there is a very specific way that positions on the board are labeled, and in how your program should accept the positions as input to update your tic-tac-toe board.
# 
# Positions on the board are labeled with the numbers 1, 2, and 3, used for the three rows, top to bottom, and the letters A, B, and C, used for the three columns, left to right. So, for example, the top-left position is A1, and the bottom-left position is C3. The entire board has positions labeled like this.
# 
# |  |  | |
# | --- | --- | --- |
# | A1|	B1| 	C1|
# | A2|	B2| 	C2|
# | A3|	B3| 	C3|
# 
# User Input.  When a user enters a position, they must use the above format exactly. You are required to check any position a user provides to ensure it properly defines a valid position. If it does not, you should tell the user the position is invalid, and ask them to enter a new, correct position.
# 
# Even if the position provided by the user is in the correct format, it may still be invalid (e.g., if the position is already taken). After confirming the position's format is correct, you must then check to ensure the position itself is available. If not, you would again report the issue to the user and ask them to provide a new, valid position.
# 
# Input from the keyboard can be requested using Python's input() function.
# 
# ## Wins and Ties
# At some point, one of the players will win the game, or the game will end in a tie. When this happens, your program should print the result of the game, and exit the program.
# 
# 
# 
# # Solution:
# 
# 1. Create a template of the board and write a function to call it
# 2. The first player is set as 'X'
# 3. The count is used to get the condition for Game Tie
# 4. Create a list for valid inputs and create an empty list to collect the filled position
# 5. The whole program runs inside the while loop
# 6. User gives the position and the game begins
# 7. The program does not ask to play again since that was not asked
#  -->

# In[1]:


## Creating the board
theBoard = {'A1': ' ' , 'B1': ' ' , 'C1': ' ' ,
            'A2': ' ' , 'B2': ' ' , 'C2': ' ' ,
            'A3': ' ' , 'B3': ' ' , 'C3': ' ' }
def printBoard(board):
    print( '\tA' + '\tB' + '\tC')
    print('     +------+------+------+')
    print('1    |' + board['A1'] + '     |' + board['B1'] + '     |' + board['C1']+ '     |')
    print('     +------+------+------+')
    print('2    |' + board['A2'] + '     |' + board['B2'] + '     |' + board['C2']+ '     |')
    print('     +------+------+------+')
    print('3    |' + board['A3'] + '     |' + board['B3'] + '     |' + board['C3']+ '     |')
    print('     +------+------+------+')

# Basic details needed for the program loop
player = 'X'                                                                                     # The first player is set as 'X'
count = 0                                                                                        # The count is used to get the condition for Game Tie
valid_ip = ['A1','B1','C1','A2','B2','C2','A3','B3','C3']                                        # These are the valid inputs that user can give
filled_ip =[]                                                                                    # This is an empty list used to fill the position filled

# The main loop is used to run the program
while(True):                                                                                     # This loop runs till any break statement is executed
    printBoard(theBoard)                                                                         # Print the empty board first 
    position = input( "Choose a position: " )                                                    # Read the position from the player and print it
    print( position )
    if position in valid_ip and position not in filled_ip:                                       # Condition check if given input is correct
        theBoard[position] = player                                                              # Place the position on the board
        filled_ip.append(position)                                                               # Append the position given to the empty list
        count += 1                                                                               # Increase the count by 1 if the condition satisfies
        if theBoard['A1'] == theBoard['B1'] == theBoard['C1'] != ' ':                            # Check 1: Across the top
            printBoard(theBoard)
            print(player + " won!")
            break                                                                                # Break the while loop if Check 1 is valid
        elif theBoard['A3'] == theBoard['B3'] == theBoard['C3'] != ' ':                          # Check 2: Across the bottom
            printBoard(theBoard)
            print(player + " won!")
            break                                                                                # Break the while loop if Check 2 is valid
        elif theBoard['A3'] == theBoard['A2'] == theBoard['A1'] != ' ':                          # Check 3: Down the left side
            printBoard(theBoard)
            print(player + " won!")
            break                                                                                # Break the while loop if Check 3 is valid
        elif theBoard['B3'] == theBoard['B2'] == theBoard['B1'] != ' ':                          # Check 4: Down the middle
            printBoard(theBoard)
            print(player + " won!")
            break                                                                                # Break the while loop if Check 4 is valid
        elif theBoard['C3'] == theBoard['C2'] == theBoard['C1'] != ' ':                          # Check 5: Down the right side
            printBoard(theBoard)
            print(player + " won!")
            break                                                                                # Break the while loop if Check 5 is valid
        elif theBoard['A1'] == theBoard['B2'] == theBoard['C3'] != ' ':                          # Check 6: Diagonal
            printBoard(theBoard)
            print(player + " won!")
            break                                                                                # Break the while loop if Check 6 is valid
        elif theBoard['A3'] == theBoard['B2'] == theBoard['C1'] != ' ':                          # Check 7: Diagonal
            printBoard(theBoard)
            print(player + " won!")
            break                                                                                # Break the while loop if Check 7 is valid

        if count == 9:                                                                           # If the board is filled then tie the game 
            print("Game Tie.")
            break                                                                                # Break the while loop if board is filled
    
    else:                                                                                        # If wrong position is given by the user, ask them to fill again
        print("That's a wrong/filled position. Try again.")
        continue

    if player =='X':                                                                             # This is to change the 'X' to 'O' between players
        player = 'O'
    else:
        player = 'X'

exit()

