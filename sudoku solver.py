# Program to solve sudoku
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
    # checking if the number is repeated in the row
    for i in range(0, 9):
        if sudoku[row][i] == number:
            return False

    # checking if the number is repeated in the column
    for j in range(0, 9):
        if sudoku[j][column] == number:
            return False

    # checking if the number is repeated in the box
    row0 = row//3*3
    column0 = column//3*3
    for i in range(0, 3):
        for j in range(0, 3):
            if sudoku[row0 + i][column0 + j] == number:
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
    input()
