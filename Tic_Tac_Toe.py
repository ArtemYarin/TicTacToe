# Creating a board
boardData = [["-" for i in range(3)] for j in range(3)]

# Active player
nowSign = "o"


def prBoard(board):
    # Output game board
    print(f"  0 1 2 \n0 {board[0][0]} {board[0][1]} {board[0][2]} \n1 {board[1][0]} {board[1][1]} {board[1][2]} \n2 {board[2][0]} {board[2][1]} {board[2][2]}")


def change(sign):
    # Square change
    global boardData
    print(f"Player {sign} turn")
    line = input("Choose a line: ")
    column = input("Choose a column: ")
    if line not in ["0", "1", "2"] or column not in ["0", "1", "2"]:
        print("Incorrect format")
        return change(sign)
    elif boardData[int(line)][int(column)] != "-":
        print("Selected square is already occupied, please choose another one")
        return change(sign)
    else:
        boardData[int(line)][int(column)] = sign


def gameEnd(board, sign):
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
prBoard(boardData)

while True:
    # Player´s turn
    change(nowSign)
    prBoard(boardData)

    # Check for winner
    x = gameEnd(boardData, nowSign)
    if x == 1:
        print(f"The winner is: {nowSign}")
        break
    elif x == 2:
        print("Draw")
        break

    # Changing sign
    # Next player´s turn
    if nowSign == "o":
        nowSign = "x"
    else:
        nowSign = "o"
