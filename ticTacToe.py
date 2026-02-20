# CMPUT 175 - Lab 2: Tic Tac Toe
#Name: Pratap Kolukuluri
#Student ID: 1849597

class TicTacToe:
    def __init__(self):
        # Initialize a 3x3 board filled with empty spaces
        # BUG (functional): Removed shared-row list, same list
        self.board = [[" " for _ in range(3)] for _ in range(3)]

    def drawBoard(self):
        # Print the current state of the board in a readable grid format
        # BUG (functional): Removed multiple board prints
        print("   0 1 2")
        for i in range(3):
            print(f"{i} ", end="")
            for j in range(3):
                print(f"|{self.board[i][j]}", end="")
            print("|")
            if i < 2:
                print("  -----------")

    def squareIsEmpty(self, row, col):
        # Check if a specific square has not been played yet
        # BUG (unit): Removed None check and empty squares are represented by a space character
        return self.board[row][col] == " "

    def update(self, row, col, symbol):
        # Attempt to place a symbol on the board
        if self.squareIsEmpty(row, col):
            self.board[row][col] = symbol
            return True
        return False

    def boardFull(self):
        # Check whether all squares on the board are filled
        # BUG (logic): Removed early True return and now function checks all cells before concluding board is full
        for row in self.board:
            for cell in row:
                if cell == " ":
                    return False
        return True

    def isWinner(self, symbol):
        # See if a player has won the game
        # rows
        for row in self.board:
            if row[0] == row[1] == row[2] == symbol:
                return True

        # columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] == symbol:
                return True

        # diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == symbol:
            return True

        if self.board[0][2] == self.board[1][1] == self.board[2][0] == symbol:
            return True

        return False


def main():
    # Run a sequence of test cases to verify class behavior
    game = TicTacToe()

    print("Contents of board attribute when object first created:")
    print(game.board)

    game.drawBoard()

    game.update(1, 2, "X")
    game.drawBoard()

    print(game.isWinner("X"))
    print(game.isWinner("O"))
    print(game.boardFull())

    game.update(0, 0, "O")
    game.update(1, 1, "O")
    game.update(2, 2, "O")

    game.drawBoard()
    print(game.isWinner("O"))

    game.update(0, 1, "O")
    game.update(0, 2, "X")
    game.update(1, 0, "X")
    game.update(1, 2, "X")
    game.update(2, 0, "O")
    game.update(2, 1, "X")

    game.drawBoard()
    print("True Player 1")
    print("False Player 2")
    print(game.boardFull())


if __name__ == "__main__":
    main()