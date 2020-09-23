def valid_sudoku(puzzle):
    # check the columns
    for i in range(len(puzzle)):
        column_digit_set = set()
        for j in range(len(puzzle[i])):
            digit = puzzle[i][j]
            if digit in column_digit_set:
                return False
            if digit != ".":
                column_digit_set.add(digit)

    # check the rows
    for j in range(len(puzzle[0])):
        row_digit_set = set()
        for i in range(len(puzzle)):
            digit = puzzle[i][j]
            if digit in row_digit_set:
                return False
            if digit != ".":
                row_digit_set.add(digit)

    # check the grids
    j = 0
    i = 0
    offset_x = 0
    offset_y = 0
    for offset_x in [0, 3, 6]:
        grid_digit_set = set()
        for offset_y in [0, 3, 6]:
            grid_digit_set = set()
            for i in range(3):
                for j in range(3):
                    digit = puzzle[i + offset_x][j + offset_y]
                    if digit in grid_digit_set:
                        return False
                    if digit != ".":
                        grid_digit_set.add(digit)
    return True
