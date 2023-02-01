# Program to solve sudoku same as sudoku solver but the check function is altered a bit.

sudoku = [[], [], [], [], [], [], [], [], [], ]

rows = []


def input_num():
    print("If there is a blank enter 0")
    for i in range(1, 10):
        run = True
        while run:
            row_i = input("Enter the element of " + str(i) +
                          " row.")
            if row_i.lower() >= 'a' and row_i <= 'z':
                print("You can not enter alphabets")

            elif len(row_i) == 9:
                rows.append(row_i)
                run = False

            else:
                print("You did not enter correct amount of values(It must be 9 numbers)")


def put_num():
    for i in range(0, 9):
        for j in range(0, 9):
            sudoku[i].append(int(rows[i][j]))


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


def check(row, column, number):
    # checking for the numbers present in the sudoku and appending them in the lists.
    num_in_row = []
    for i in range(0, 9):
        if sudoku[row][i] != 0:
            num_in_row.append(sudoku[row][i])

    if number in num_in_row:
        return False

    num_in_column = []
    for j in range(0, 9):
        if sudoku[j][column] != 0:
            num_in_column.append(sudoku[j][column])

    if number in num_in_column:
        return False

    # dividing the row and column by 3 and rouding off to floor allows us to traverse through the boxes and multiplying by three gives corresponding row and column.
    row0 = row//3*3
    column0 = column//3*3

    num_in_box = []
    for i in range(0, 3):
        for j in range(0, 3):
            if sudoku[row0 + i][column0 + j] != 0:
                num_in_box.append(sudoku[row0 + i][column0 + j])

    # checking if the number is present in the row or column or the box.

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
    res = input('more').lower()
    if res == "yes":
        solve()


input_num()
put_num()

print_board(sudoku)
print("\n\n solved sudoku\n")

solve()
