
#This is our main function. Everything below this is essentially pulled into this in order to run the game.
def main():
    player = next_player("")
    board = create_board()

    # This while is to say that while these two things are not true, keep playing.
    # This will loop throug until there is a draw or there is a winner.
    while not (has_winner(board) or is_a_draw(board)):
        display_board(board)
        make_move(player, board)
        player = next_player(player)
    display_board(board)
    print("Good game. Thanks for playing!") 

#This function is creating the board and the array of numbers in the square spaces.
def create_board():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board

# This function prints our the board with the numbers.
def display_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()

# This function determins a draw.
# So if it keeps returning the board with a number in it the game will continue until there are no numbers let.
# Once that happens and it realizes that there are all "x" and "o" it will say draw.
def is_a_draw(board):
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True 

# This function allows the player to win and includes all the outcomes in order to win. 
# If it matches one of these outcomes it will know there is a winner.
def has_winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

# This function determins what numerical selection the player made (1-9) and then 
def make_move(player, board):
    # It asks you which number you would like to choose. It takes that value and inputs your "x" or "o" where you said.
    square = int(input(f"{player}'s turn to choose a square (1-9): "))
    # You have to minus 1 to account for the way an array works.
    board[square - 1] = player

# This function tells which player is next to choose.
def next_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"

# Run the main function
if __name__ == "__main__":
    main()
