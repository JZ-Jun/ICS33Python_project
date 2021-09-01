'''
Tic tac toe is a very popular game.  Only two players can play at a time. 

Game Rules
Traditionally the first player plays with "X". So you can decide who wants to go with "X" and who wants to go with "O".
Only one player can play at a time.
If any of the players have filled a square then the other player and the same player cannot override that square.
There are only two conditions that may match will be a draw or may win.
The player that succeeds in placing three respective marks (X or O) in a horizontal, vertical, or diagonal row wins the game.
 
Winning condition
Whoever places three respective marks (X or O) horizontally, vertically, or diagonally will be the winner.
Submit your code and screenshots of your code in action. 
Hints :
Have a function that draws the board 
Have a function that checks position if empty or not
Have a function that checks player or won or not 
'''

import re  # With the re module you can use ideas  of match or search.


def win(panels, sign):
    # Used to determine if the user has won
    # Determine if the symbols are the same for each column, each row, and the two diagonal lines.
    # 'sign' is 'O' or 'X'
    return ((panels[1] == panels[2] == panels[3] == sign)
            or (panels[1] == panels[4] == panels[7] == sign)
            or (panels[1] == panels[5] == panels[9] == sign)
            or (panels[2] == panels[5] == panels[8] == sign)
            or (panels[3] == panels[6] == panels[9] == sign)
            or (panels[3] == panels[5] == panels[7] == sign)
            or (panels[4] == panels[5] == panels[6] == sign)
            or (panels[7] == panels[8] == panels[9] == sign))


def isGameFinished(sign):
    # Determine whether player1 or player2 wins
    if sign == 'O' and win(panels, sign):
        print("Player 2 Won")
        quit()
    elif sign == 'X' and win(panels, sign):
        print("Player 1 Won")
        quit()

    # If the number of steps (count) is greater than 8 and no player wins, the game is tied.
    elif count == 8:
        print("Tied")
        quit()


def PrintGameBoard():
    # Print the game board.
    print(f'{panels[1]} | {panels[2]} | {panels[3]}')
    print(f'{panels[4]} | {panels[5]} | {panels[6]}')
    print(f'{panels[7]} | {panels[8]} | {panels[9]}')
    print(f'  |   |  ')


def IsDigit():
    # To verify if the input is digit and collect the number player entered.
    user_in = input("Enter the position between [1-9] where you want to mark : ")
    result = value.match(user_in)
    if result:
        user_in = int(user_in)
        CheckEmpty(user_in)
       
    else:
        # Run when the player did not enter a number and ask the player to input the number again.
        print("⚠mPlz enter a number between 1-9!⚠")
        IsDigit()


def CheckEmpty(judge):
    # To check if the gameboard already have position or not.
    while panels[judge] != " ":
        # Happened when this position already had a chess and ask the user to input the other number.
        print("⚠This position is already has something!⚠")
        PrintGameBoard()
        IsDigit()
        return
    global choice
    choice = judge


# main function
if __name__ == '__main__':
    choice = 0
    value = re.compile(r'^[1-9]$')  # Compile the 9 digits.
    count = 0
    panels = [' '] * 10
    sign = ''
    print("Please Wait...")  # Have an initial game board.
    PrintGameBoard()
    while True:
        if count % 2 == 0:
            # When player1 is play the game.
            sign = 'X'
            # Use X to represent player2's choice.
            print("Player 1's chance")
            IsDigit()
            panels[choice] = 'X'
            PrintGameBoard()  # Update the game board.
            isGameFinished("X")  # Check if the player1 is win.
            count += 1
        else:
            # When player2 is play the game.
            sign = 'O'
            # Use O to represent player1's choice.
            print("Player 2's chance")
            IsDigit()
            panels[choice] = 'O'
            PrintGameBoard()  # Update the game board.
            isGameFinished("O")  # Check if the player2 is win.
            count += 1
