# Program to solve sudoku same as sudoku solver but the check function is altered a bit.
sudoku = [
    [1, 0, 0, 0, 0, 0, 0, 0, 3],
    [0, 4, 0, 0, 8, 9, 0, 2, 0],
    [0, 0, 2, 0, 0, 3, 9, 5, 0],
    [0, 0, 0, 4, 1, 0, 5, 0, 0],
    [0, 0, 0, 0, 2, 0, 0, 0, 0],
    [0, 0, 5, 0, 3, 7, 0, 0, 0],
    [0, 3, 4, 8, 0, 0, 6, 0, 0],
    [0, 2, 0, 6, 7, 0, 0, 3, 0],
    [6, 0, 0, 0, 0, 0, 0, 0, 9],
]


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - - -")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + ' ', end=" ")


print_board(sudoku)
print("\n\n solved sudoku")


def check(row, column, number):
    # checking for the numbers present in the sudoku and appending them in the lists.
    num_in_row = []
    for i in range(0, 9):
        if sudoku[row][i] != 0:
            num_in_row.append(sudoku[row][i])

    num_in_column = []
    for j in range(0, 9):
        if sudoku[j][column] != 0:
            num_in_column.append(sudoku[j][column])

    # dividing the row and column by 3 and rouding off to floor allows us to traverse through the boxes and multiplying by three gives corresponding row and column.
    row0 = row//3*3
    column0 = column//3*3

    num_in_box = []
    for i in range(0, 3):
        for j in range(0, 3):
            if sudoku[row0 + i][column0 + j] != 0:
                num_in_box.append(sudoku[row0 + i][column0 + j])

    # checking if the number is present in the row or column or the box.
    if number in num_in_row:
        return False

    if number in num_in_column:
        return False

    if number in num_in_box:
        return False

    return True


def solve():
    for i in range(0, 9):
        for j in range(0, 9):
            if sudoku[i][j] == 0:
                for number in range(1, 10):
                    if check(i, j, number):
                        sudoku[i][j] = number
                        solve()
                        sudoku[i][j] = 0
                return

    print_board(sudoku)


solve()
