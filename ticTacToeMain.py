# CMPUT 175 - Lab 2: Tic Tac Toe
# Name: Pratap Kolukuluri
# Student ID: 1849597

import os
from ticTacToe import TicTacToe

def clear():
    # Clears terminal 
    # BUG (system): Removed OS-specific clearing assumptions and now safely handles all os types
    os.system("cls" if os.name == "nt" else "clear")

def getCoord():
    # Prompts user for valid row and column input
    # BUG (logic): Removed input validation loop, 
    while True:
        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
            if 0 <= row <= 2 and 0 <= col <= 2:
                return row, col
        except ValueError:
            pass

def isGameOver(game, symbol):
    # Determines whether the game has ended due to a win or a draw
    # BUG (logic): Removed draw check before win check, now win is evaluated first
    if game.isWinner(symbol):
        return True
    if game.boardFull():
        return True
    return False

def playAgain():
    # Asks the user if they want to start a new game
    answer = input("Play again? (y/n): ").lower()
    return answer == "y"

def main():
    # Controls game loop and player turns
    while True:
        clear()
        game = TicTacToe()
        currentPlayer = "X"

        # Loop for a single game session
        while True:
            clear()
            game.drawBoard()

            row, col = getCoord()

            # Attempt to place the current player symbol
            if game.update(row, col, currentPlayer):
                if isGameOver(game, currentPlayer):
                    clear()
                    game.drawBoard()
                    break

                # Switch between Player X and Player O
                # BUG (logic): Removed incorrect turn handling, now player switches correctly every move
                currentPlayer = "O" if currentPlayer == "X" else "X"

        # Ask the user if they want to play another round
        if not playAgain():
            break

if __name__ == "__main__":
    # Start the game when this file is executed directly
    main()

