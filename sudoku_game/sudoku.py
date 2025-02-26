def input_file_reader(file_name):
    """This function is used to taking sudoku information
    from input file and convert the nested list form"""
    sudoku_list = []
    input_file = open(file_name, 'r')
    for line in input_file:
        row = line.strip().split()
        row = [int(num) for num in row]
        sudoku_list.append(row)
    input_file.close()
    return sudoku_list


def is_suitable_to_do(sudoku, row, col, num):
    """is_suitable_to_do function  inspects
     whether the current move is right or not
     in terms of grids rows and columns"""
    initial_row = 3 * (row // 3)   # // is used to scan determined index numbers of rows
    initial_col = 3 * (col // 3)   # // is used to scan determined index numbers of columns
    for i in range(initial_row, initial_row + 3):  # looking for same number on number's 3*3 grid
        for j in range(initial_col, initial_col + 3):
            if num == sudoku[i][j]:
                return False
    for i in range(9):  # looking for any same number on same column or row
        if sudoku[row][i] == num or sudoku[i][col] == num:
            return False
    return True    # if the move is a valid move, function let the move happens by returning True


def find_blank_point(sudoku):
    """This function is used to find numbers of zero if there is a still
    0 numbers in current sudoku list"""
    temp_list = [row.count(0) for row in sudoku]  # list keeps inside number of zero in every row
    number_of_zero = sum(temp_list)
    return number_of_zero


def sudoku_solver(output, sudoku, step_num):
    """sudoku_solver solves the sudoku step by step
    as long as there is still blank places to fill with a number"""
    while find_blank_point(sudoku) > 0:
        for r in range(9):  # r represent list index numbers of rows
            for c in range(9):  # c represent list index numbers of columns
                if sudoku[r][c] == 0:
                    possible_nums = []
                    for num in range(1, 10):
                        if is_suitable_to_do(sudoku, r, c, num):
                            possible_nums.append(num)
                    if len(possible_nums) == 1:  # only perform when there is one possiblity
                        sudoku[r][c] = possible_nums[0]
                        step_num += 1
                        output_func(output, sudoku, step_num, r+1, c+1, sudoku[r][c])
                        sudoku_solver(output, sudoku, step_num)  # function recurse itself to return at start of sudoku


def output_func(output, sudoku, step, row, col, num):
    """This function implement the process of forming
    output script in the way that is wanted"""
    output.write("------------------\n")
    output.write("Step {} - {} @ R{}C{}\n".format(step, num, row, col))
    output.write("------------------\n")
    current_sudoku_string = '\n'.join([' '.join(map(str, row)) for row in sudoku])
    output.write("{}\n".format(current_sudoku_string))  # to print current state of sudoku inside output file
    if find_blank_point(sudoku) == 0:
        output.write("------------------")


def main():
    """This function consist of blocks other functions and
    number of steps counter variable. It provides an ordered collection of steps """
    import sys
    step_num = 0
    sudoku_file = sys.argv[1]
    output_form = open(sys.argv[2], "w")  # opens the output file in writing mode
    sudoku = input_file_reader(sudoku_file)
    sudoku_solver(output_form, sudoku, step_num)  # solves sudoku step by step
    output_form.flush()
    output_form.close()  # to ensure that output file is closed


if __name__ == "__main__":
    main()
