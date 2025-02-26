def input_reader(input_file):
    """This functions opens the input file and then reads the contents in it."""
    with open(input_file, 'r') as file:
        number_of_lines = len(file.readlines())
        file.seek(0)
        # takes rules in first four lines and first structure as two different variable
        using_rule_list = [[int(j) for j in file.readline().strip().split()] for _ in range(4)]
        structure_layout = [file.readline().strip().split() for _ in range(number_of_lines-4)]
    return using_rule_list, structure_layout


def neighbours(layout):
    """This function checks whether the current layout is suitable for neighbours rules"""
    neighbours_positions = tuple([(1, 0), (0, -1), (-1, 0), (0, 1)])  # possible neighbours
    for r, line in enumerate(layout):
        for c, letter in enumerate(line):
            if letter == 'H':  # checking H tiles
                for i, j in neighbours_positions:
                    if (-1 < r + i < len(layout)) and (-1 < c + j < len(layout[0])):
                        if layout[r + i][c + j] == 'H':
                            return False
            if letter == 'B':  # checking B tiles
                for i, j in neighbours_positions:
                    if (-1 < r + i < len(layout)) and (-1 < c + j < len(layout[0])):
                        if layout[r + i][c + j] == 'B':
                            return False
    return True


def numbering(number_rules, layout):
    """This function controls the numbers of H and B in every column and rows based on rules"""
    # assigning the number rules to related H and B vars
    h_tuple, b_tuple = (number_rules[0], number_rules[2]), (number_rules[1], number_rules[3])
    column_matrix = tuple([tuple(line[i] for line in layout) for i in range(len(layout[0]))])  # special matrix for cols
    for i, inner_lst in enumerate(layout):
        for letter, lst in zip(('H', 'B'), (h_tuple, h_tuple)):  # matching the rules and their letters
            if lst[0][i] == -1:  # checking is it free to put as long as desired
                continue
            else:
                if inner_lst.count(letter) != lst[0][i]:
                    return False
    for i, inner_lst in enumerate(column_matrix):
        for letter, lst in zip(('H', 'B'), (h_tuple, b_tuple)):  # matching the rules and their letters
            if lst[1][i] == -1:  # checking is it free to put as long as desired
                continue
            else:
                if inner_lst.count(letter) != lst[1][i]:
                    return False
    return True


def recursive_backtracking_func(result, first_layout, layout, number_rules, r, c):
    """This function backtracks the possible paths to solution in the recursive way"""
    max_row, max_col = len(layout) - 1, len(layout[0]) - 1
    for tile in ('H', 'B', 'N'):  # tile starts with order of priority
        while first_layout[r][c] == 'D' or first_layout[r][c] == 'R':  # separating the ones not tile start
            if max_col >= c + 1:
                c += 1
            elif max_row >= r+1:
                r += 1
                c = 0
        a, b = r, c  # assigning the current row and col index
        if result:  # when true result is found stops the process
            pass
        else:
            if tile == 'H':
                if first_layout[r][c] == 'L':
                    m, n = layout[r][c], layout[r][c + 1]  # assigning in case there is no change
                    layout[r][c], layout[r][c+1] = 'H', 'B'  # placing tile
                    if neighbours(layout):
                        if max_col >= c+2:
                            b += 2
                            result = recursive_backtracking_func(result, first_layout, layout, number_rules, a, b)
                        elif max_row >= r+1:
                            a += 1
                            b = 0
                            result = recursive_backtracking_func(result, first_layout, layout, number_rules, a, b)
                        else:
                            if numbering(number_rules, layout):
                                return True  # found the true layout and it backtracks up to previous frame as result
                            else:
                                continue
                    else:
                        layout[r][c], layout[r][c + 1] = m, n  # assigning values back
                        continue
                elif first_layout[r][c] == 'U':
                    m, n = layout[r][c], layout[r+1][c]  # assigning in case there is no change
                    layout[r][c], layout[r+1][c] = 'H', 'B'  # placing tile
                    if neighbours(layout):
                        if max_col >= c + 1:
                            b += 1
                        else:
                            a += 1
                            b = 0
                        result = recursive_backtracking_func(result, first_layout, layout, number_rules, a, b)
                    else:
                        layout[r][c], layout[r + 1][c] = m, n  # assigning values back
                        continue
            if tile == 'B':
                if first_layout[r][c] == 'L':
                    m, n = layout[r][c], layout[r][c + 1]  # assigning in case there is no change
                    layout[r][c], layout[r][c+1] = 'B', 'H'  # placing tile
                    if neighbours(layout):
                        if max_col >= c+2:
                            b += 2
                            result = recursive_backtracking_func(result, first_layout, layout, number_rules, a, b)
                        elif max_row >= r+1:
                            a += 1
                            b = 0
                            result = recursive_backtracking_func(result, first_layout, layout, number_rules, a, b)
                        else:
                            if numbering(number_rules, layout):
                                return True  # found the true layout and it backtracks up to previous frame as result
                            else:
                                continue
                    else:
                        layout[r][c], layout[r][c + 1] = m, n  # assigning values back
                        continue
                elif first_layout[r][c] == 'U':
                    m, n = layout[r][c], layout[r + 1][c]  # assigning in case there is no change
                    layout[r][c], layout[r+1][c] = 'B', 'H'  # placing tile
                    if neighbours(layout):
                        if max_col >= c + 1:
                            b += 1
                        else:
                            a += 1
                            b = 0
                        result = recursive_backtracking_func(result, first_layout, layout, number_rules, a, b)
                    else:
                        layout[r][c], layout[r + 1][c] = m, n  # assigning values back
                        continue
            if tile == 'N':
                if first_layout[r][c] == 'L':
                    m, n = layout[r][c], layout[r][c + 1]  # assigning in case there is no change
                    layout[r][c], layout[r][c+1] = 'N', 'N'  # placing tile
                    if neighbours(layout):
                        if max_col >= c+2:
                            b += 2
                            result = recursive_backtracking_func(result, first_layout, layout, number_rules, a, b)
                        elif max_row >= r+1:
                            a += 1
                            b = 0
                            result = recursive_backtracking_func(result, first_layout, layout, number_rules, a, b)
                        else:
                            if numbering(number_rules, layout):
                                return True  # found the true layout and it backtracks up to previous frame as result
                            return False
                    else:
                        layout[r][c], layout[r][c + 1] = m, n  # assigning values back
                        return False
                elif first_layout[r][c] == 'U':
                    m, n = layout[r][c], layout[r + 1][c]  # assigning in case there is no change
                    layout[r][c], layout[r+1][c] = 'N', 'N'  # placing tile
                    if neighbours(layout):
                        if max_col >= c + 1:
                            b += 1
                        else:
                            a += 1
                            b = 0
                        result = recursive_backtracking_func(result, first_layout, layout, number_rules, a, b)
                    else:
                        layout[r][c], layout[r + 1][c] = m, n  # assigning values back
                        return False
    return result  # returning whether the is it possible to solve with given rules


def main():
    """main() consists of all entry points and fragments of program"""
    import sys
    input_file = sys.argv[1]
    number_rules, layout = input_reader(input_file)  # taking the rules and beginning layout
    first_layout = tuple([tuple([i for i in row]) for row in layout])  # layout's tuple form
    with open(sys.argv[2], 'w') as f:  # writes the resultant form to output file
        if recursive_backtracking_func(False, first_layout, layout, number_rules, 0, 0):
            for i, row in enumerate(layout):
                if i == len(layout)-1:  # when pointer comes to end of lines it does not leave a space at the end
                    f.write(' '.join(row))
                    break
                f.write(' '.join(row) + '\n')
        else:
            f.write("No solution!")  # in the case there is no possible solution


if __name__ == '__main__':
    main()
