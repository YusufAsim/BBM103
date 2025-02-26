def input_reader(input_file):
    """This function opens the file in reading mode and makes it into matrix"""
    with open(input_file, "r") as input_script:
        input_matrix = []
        for row in input_script:
            row = [int(i) for i in row.strip().split()]
            input_matrix.append(row)
    return input_matrix


def show_the_step(matrix):
    """Function prints the values to screen in wanted format"""
    for row in matrix:
        for i in row:
            print(i, end=' ')
        print()
    print()


def neighbours_finder(r, c, matrix, set_var):
    """This function is used to put the same value neighbours
    and neighbours' the same value neighbours to a list."""
    target_value = matrix[r][c]
    max_row_index = len(matrix)
    max_column_index = len(matrix[0])
    possible_places = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # respectively for down,up,left,right neighbour positions
    neighbors_location_list = []

    for i, j in possible_places:
        temp_r, temp_c = r + i, c + j
        is_suitable_to_limit = (0 <= temp_r < max_row_index) and (0 <= temp_c < max_column_index)
        is_locations_in = (temp_r, temp_c) in set_var  # controlling for whether position is already used

        if is_suitable_to_limit and not is_locations_in:
            if matrix[temp_r][temp_c] == target_value:
                set_var.add((temp_r, temp_c))
                neighbors_location_list.append((temp_r, temp_c))
                neighbors_location_list = neighbors_location_list + neighbours_finder(temp_r, temp_c, matrix, set_var)
                # for finding the neighbours of neighbours with same value
    return neighbors_location_list


def element_remover(r, c, location_list, matrix):
    """This function replace the number values with space character if list argument does not exist as []
    And returns the number to add score"""
    if not location_list:
        print("No movement happened, try again\n")
        result = 0  # if there is no list, there is nothing to add
    else:
        location_list.append([r, c])  # adds the original input position to list
        removed_one_number = len(location_list)
        removed_value = matrix[r][c]
        result = removed_value * removed_one_number  # to add score
        for i in location_list:
            r_idx, c_idx = i[0], i[1]
            matrix[r_idx][c_idx] = " "
    return result


def column_list_maker(matrix):
    """This function creates the matrix of columns by using the current matrix """
    column_list = [[row[i]for row in matrix] for i in  range(len(matrix[0]))]
    return column_list


def shifting_down(matrix):
    """This function shifts the values down if there is a blank value between value number on board
    and returns the shifted version of matrix."""
    column_list = column_list_maker(matrix)
    for column in column_list:
        blank_list = []
        valid_list = []
        for i in column:
            if i == ' ':
                blank_list.append(i)
            else:
                valid_list.append(i)
        column.clear()  # to start ordering
        column.extend(blank_list)  # firstly blanks to put numbers down
        column.extend(valid_list)  # then numbers
    temp_matrix = [[column[i] for column in column_list]for i in range(len(matrix))]
    return temp_matrix


def shifting_left(matrix):
    """This function shifts the values left on output board if a column's all elements consist of space characters
    and returns the shifted version of matrix."""
    column_list = column_list_maker(matrix)
    for column in column_list:
        if column == [' ' for i in range(len(column))]:
            column_list.remove(column)
    temp_matrix = [[column[i] for column in column_list] for i in range(len(matrix))]
    return temp_matrix


def is_game_over(matrix):
    """This function controls if still there is a step to move at game."""
    for row in matrix:
        r = matrix.index(row)  # row index based 0
        for i in row:
            if i != ' ':
                c = matrix[r].index(i)  # column index based 0
                a_list = neighbours_game_over(r, c, matrix)  # the list of neighbours
                values = [matrix[r][c] for r, c in a_list]
                for j in values:
                    if j == ' ':
                        values.remove(j)  # ' ' values doesn't involve in game
                if values:
                    return False
                else:
                    continue
    return True  # no element has neighbour with same value , so it returns True


def neighbours_game_over(r, c, matrix):
    """This function is used to put only the same value neighbours to a list."""
    target_value = matrix[r][c]
    max_row_index = len(matrix)
    max_column_index = len(matrix[0])
    possible_places = [(-1, 0), (0, -1), (1, 0), (0, 1)]  # respectively for down,left,up,right neighbour positions
    neighbors_location_list = []

    for i, j in possible_places:
        new_r, new_c = r + i, c + j
        is_suitable_to_limit = (0 <= new_r < max_row_index) and (0 <= new_c < max_column_index)
        if is_suitable_to_limit:
            if matrix[new_r][new_c] == target_value:  # controlling same value case
                neighbors_location_list.append((new_r, new_c))
    return neighbors_location_list


def shifting_up(matrix):
    """This function removes the row if the row consists of full of blank characters
    amd returns the removed form of matrix."""
    for row in matrix:
        temp_matrix = matrix
        if row == [' ' for i in range(len(matrix[0]))]:  # controlling if it consists of full ' '
            temp_matrix.remove(row)
    return temp_matrix


def main():
    """This function includes all instructions and functions inside."""
    import sys  # to call sys file argument
    input_file = sys.argv[1]
    matrix = input_reader(input_file)  # makes the input board matrix form
    score = 0  # points of player
    show_the_step(matrix)
    print(f"Your score is: {score}\n")
    user_input = input("Please enter a row and a column number: ")
    print()
    while True:
        try:
            row = user_input.strip().split(' ')[0]
            column = user_input.strip().split(' ')[1]
            r_idx, c_idx = int(row) - 1, int(column) - 1  # making input values integer and based 0 indexes
            if 0 <= r_idx < len(matrix) and 0 <= c_idx < len(matrix[0]):  # controlling limits of input indexes
                ready_set = {(r_idx, c_idx)}  # to keep input in set that will be with neighbours if they exist
                adding = element_remover(r_idx, c_idx, neighbours_finder(r_idx, c_idx, matrix, ready_set), matrix)
                score += adding
                matrix = shifting_down(matrix)
                matrix = shifting_left(matrix)
                matrix = shifting_up(matrix)
                if is_game_over(matrix):  # block that game terminate
                    show_the_step(matrix)
                    print(f"Your score is: {score}\n")
                    print("Game over")
                    break
                show_the_step(matrix)
                print(f"Your score is: {score}\n")
                user_input = input("Please enter a row and a column number: ")
                print()
            else:
                print("Please enter a correct size!\n")
                user_input = input("Please enter a row and a column number: ")
                print()
                continue
        except (TypeError, ValueError, IndexError):  # under the circumtances that an error occurs
            print("Please enter a correct size!\n")
            user_input = input("Please enter a row and a column number: ")
            print()
            continue  # to get back to game


if __name__ == "__main__":
    main()
