# funktion för att skriva ut sjävla brädan

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # kolla rader och kolumner
    for row in board:
        if row[0]== row[1] == row[2] == player:
            return True
    for col in range(3):
        if board[0][col] == row[1] == row[2] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def get_move(board):
    while True:
        try:
            move = int(input("Enter your move: "))
            row, col = divmod(move, 3)
            if board[row][col] == " ":
                return row, col
            else:
                return row, col
        except (ValueError, IndexError):
            print("Invalid move, try again")
            
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    while True:
        print_board(board)
        row, col = get_move(board)
        board[row][col] = current_player
        
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        if is_board_full(board):
            print_board(board)
            print("It's a draw, lol")
            break
        
    current_player = "O" if current_player == "X" else "X"
    
play_game()
            