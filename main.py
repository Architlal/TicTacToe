# command line Tic Tac Toe


# we can use for loops to make the program short but in this case i havent used them

# importing libraries
import time
import sys

# making the board
board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

# printing Title
print("-----------------------------------------------------------TIC_TAC_TOE-----------------------------------------------------------------------", "\n", "\n")

class Game:
    def __init__(self):
        self.initialize_game()

    def initialize_game(self):
        self.current_state = [['-','-','-'],
                              ['-','-','-'],
                              ['-','-','-']]

        # Player X always plays first
        self.player_turn = 'X'

    def draw_board(self):
        for i in range(0, 3):
            for j in range(0, 3):
                print('{}|'.format(self.current_state[i][j]), end=" ")
            print()
        print()


    # Determines if the made move is a legal move
    def is_valid(self, px, py):
        if px < 0 or px > 2 or py < 0 or py > 2:
            return False
        elif self.current_state[px][py] != '-':
            return False
        else:
            return True


    # Checks if the game has ended and returns the winner in each case
    def is_end(self):
        # Vertical win
        for i in range(0, 3):
            if (self.current_state[0][i] != '-' and
                self.current_state[0][i] == self.current_state[1][i] and
                self.current_state[1][i] == self.current_state[2][i]):
                return self.current_state[0][i]

        # Horizontal win
        for i in range(0, 3):
            if (self.current_state[i] == ['X', 'X', 'X']):
                return 'X'
            elif (self.current_state[i] == ['O', 'O', 'O']):
                return 'O'

        # Main diagonal win
        if (self.current_state[0][0] != '-' and
            self.current_state[0][0] == self.current_state[1][1] and
            self.current_state[0][0] == self.current_state[2][2]):
            return self.current_state[0][0]

        # Second diagonal win
        if (self.current_state[0][2] != '-' and
            self.current_state[0][2] == self.current_state[1][1] and
            self.current_state[0][2] == self.current_state[2][0]):
            return self.current_state[0][2]

        # Is whole board full?
        for i in range(0, 3):
            for j in range(0, 3):
                # There's an empty field, we continue the game
                if (self.current_state[i][j] == '-'):
                    return None

        # It's a tie!
        return '-'


    # Player 'O' is max, in this case AI
    def max(self):

        # Possible values for maxv are:
        # -1 - loss
        # 0  - a tie
        # 1  - win

        # We're initially setting it to -2 as worse than the worst case:
        maxv = -2

        px = None
        py = None

        result = self.is_end()

        # If the game came to an end, the function needs to return
        # the evaluation function of the end. That can be:
        # -1 - loss
        # 0  - a tie
        # 1  - win
        if result == 'X':
            return (-1, 0, 0)
        elif result == 'O':
            return (1, 0, 0)
        elif result == '-':
            return (0, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_state[i][j] == '-':
                    # On the empty field player 'O' makes a move and calls Min
                    # That's one branch of the game tree.
                    self.current_state[i][j] = 'O'
                    (m, min_i, min_j) = self.min()
                    # Fixing the maxv value if needed
                    if m > maxv:
                        maxv = m
                        px = i
                        py = j
                    # Setting back the field to empty
                    self.current_state[i][j] = '-'
        return (maxv, px, py)
    # Player 'X' is min, in this case human


    def min(self):

        # Possible values for minv are:
        # -1 - win
        # 0  - a tie
        # 1  - loss

        # We're initially setting it to 2 as worse than the worst case:
        minv = 2

        qx = None
        qy = None

        result = self.is_end()

        if result == 'X':
            return (-1, 0, 0)
        elif result == 'O':
            return (1, 0, 0)
        elif result == '-':
            return (0, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_state[i][j] == '-':
                    self.current_state[i][j] = 'X'
                    (m, max_i, max_j) = self.max()
                    if m < minv:
                        minv = m
                        qx = i
                        qy = j
                    self.current_state[i][j] = '-'

        return (minv, qx, qy)


    def play(self):
        while True:
            self.draw_board()
            self.result = self.is_end()

            # Printing the appropriate message if the game has ended
            if self.result != None:
                if self.result == 'X':
                    print('The winner is X!')
                elif self.result == 'O':
                    print('The winner is O!')
                elif self.result == '.':
                    print("It's a tie!")

                self.initialize_game()
                return

            # If it's player's turn
            if self.player_turn == 'X':

                while True:

                    start = time.time()
                    (m, qx, qy) = self.min()
                    end = time.time()
                    print('Evaluation time: {}s'.format(round(end - start, 7)))
                    print('Recommended move: X = {}, Y = {}'.format(qx+1, qy+1))

                    px = int(input('Enter Row : ')) - 1
                    py = int(input('Enter column ')) - 1

                    (qx, qy) = (px, py)

                    if self.is_valid(px, py):
                        self.current_state[px][py] = 'X'
                        self.player_turn = 'O'
                        break
                    else:
                        print('The move is not valid! Try again.')

            # If it's AI's turn
            else:
                (m, px, py) = self.max()
                self.current_state[px][py] = 'O'
                self.player_turn = 'X'


# function to print board
def board_print():
    print("", board[0][0], "|", board[0][1], "|", board[0][2], "\n", board[1][0], "|", board[1][1], "|", board[1][2],
          "\n", board[2][0], "|", board[2][1], "|", board[2][2])


#function for determining what to do after someone wins
def end():
    play = input("Want to play again ? [y/n] : ")

    if play == "y":
        exec('main.py')


    elif play == "n":
        sys.exit()


    else:
        print("Invalid input")
        end()


#player1 code
def game_p1():
    board_print()
    print(player1, " its your turn ", "\n")

    # INPUT for row and column
    row = input("Enter row : ")
    column = input("Enter column : ")
    r_o_w = int(row) - 1
    colum_n = int(column) - 1

    # checking if everything entered is alright
    if r_o_w > 3 or r_o_w < 0:
        print("Enter Again !! , Invalid spot")
        game_p1()


    elif colum_n > 3 or colum_n < 0:
        print("Enter Again !! , Invalid spot")
        game_p1()


    elif board[r_o_w][colum_n] == "X" or board[r_o_w][colum_n] == "O":
        print("Enter Again !! , Invalid spot")
        game_p1()

    else:

        board[r_o_w][colum_n] = "X"  # appending the value in Array

        # checking if won
        if board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X" or board[0][0] == "X" and board[1][
            1] == "X" and board[2][2] == "X" or board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X" or \
                board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X" or board[0][2] == "X" and board[1][
            1] == "X" and board[2][0] == "X" or board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X" or \
                board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X" or board[0][2] == "X" and board[1][
            2] == "X" and board[2][2] == "X":
            print(player1, "CONGRATS!!!!!! YOU WON !!")
            time.sleep(1)
            end()


        else:
            game_p2()


#player2 code
def game_p2():
    board_print()
    print(player2, " its your turn ", "\n")

    # Input for row and column
    row = input("Enter row : ")
    column = input("Enter column : ")
    r_o_w = int(row) - 1
    colum_n = int(column) - 1

    # checking if all entered info is correct
    if r_o_w > 3 or r_o_w < 0:
        print("Enter Again !! , Invalid spot")
        game_p2()


    elif colum_n > 3 or colum_n < 0:
        print("Enter Again !! , Invalid spot")
        game_p2()

    if board[r_o_w][colum_n] == "X" or board[r_o_w][colum_n] == "O":
        print("Enter Again !! , Invalid spot")
        game_p2()

    else:

        board[r_o_w][colum_n] = "O"

        # checking if won
        if board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O" or board[0][0] == "O" and board[1][
            1] == "O" and board[2][2] == "O" or board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O" or \
                board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O" or board[0][2] == "O" and board[1][
            1] == "O" and board[2][0] == "O" or board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O" or \
                board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O" or board[0][2] == "O" and board[1][
            2] == "O" and board[2][2] == "O":
            print(player2, "CONGRATS!!!!!! YOU WON !!")
            time.sleep(1)
            end()


        else:
            game_p1()


print("WELCOME TO TIC TAC TOE BY ARCHIT LAL \n \n \n \n")

# Asking what type of game to play
type_of_game = input(" For playing multiplayer press 1 \n For playing against Ai press 2 :  ")
game_type = int(type_of_game)

if game_type == 1:
    player1 = input("Player 1 enter your name : ")
    player2 = input("Player 2 enter your name : ")
    game_p1()


elif game_type == 2:
    player1 = input("Enter your name : ")
    print("you are X")
    print("You may ignore the recommended move as it is a mere suggestion by the computer ")
    def main():
        g = Game()
        g.play()


    if __name__ == "__main__":
        main()