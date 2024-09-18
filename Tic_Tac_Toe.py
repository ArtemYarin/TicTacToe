# Creating a board
board_data = [["-" for i in range(3)] for j in range(3)]

# Active player
now_sign = "o"


def pr_board(board):
    # Output game board
    print(f"  0 1 2 \n0 {board[0][0]} {board[0][1]} {board[0][2]} \n1 {board[1][0]} {board[1][1]} {board[1][2]} \n2 {board[2][0]} {board[2][1]} {board[2][2]}")


def change(sign):
    # Square change
    global board_data
    print(f"Player {sign} turn")
    line = input("Choose a line: ")
    column = input("Choose a column: ")
    if line not in ["0", "1", "2"] or column not in ["0", "1", "2"]:
        print("Incorrect format")
        return change(sign)
    elif board_data[int(line)][int(column)] != "-":
        print("Selected square is already occupied, please choose another one")
        return change(sign)
    else:
        board_data[int(line)][int(column)] = sign


def game_end(board, sign):
    # Winner check
    for i in board:
        if i.count(sign) == 3:
            return 1
    if all([board[0][0] == sign, board[1][1] == sign, board[2][2] == sign]) or all([board[0][2] == sign, board[1][1] == sign, board[2][0] == sign]):
        return 1
    for i in range(len(board)):
        if all([board[0][i] == sign, board[1][i] == sign, board[2][i] == sign]):
            return 1
    y = False
    for i in board:
        if "-" in i:
            y = True
    if not y:
        return 2


# Start
pr_board(board_data)

while True:
    # Player´s turn
    change(now_sign)
    pr_board(board_data)

    # Check for winner
    x = game_end(board_data, now_sign)
    if x == 1:
        print(f"The winner is: {now_sign}")
        break
    elif x == 2:
        print("Draw")
        break

    # Changing sign
    # Next player´s turn
    if now_sign == "o":
        now_sign = "x"
    else:
        now_sign = "o"
