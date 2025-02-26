def input_reader_function(input):
    try:
        f = open(input, 'r')
        lines = f.readlines()
        f.close()
        return lines
    except FileNotFoundError:
        print(f"ERROR: There is either no such a file namely {input}", end='')
        print(" or this program does not have permission to read it!")
        print("Program is going to terminate it!")
        return None


def calculator(operand_1, operator, operand_2):
    if operator == '+':
        return float(operand_1) + float(operand_2)
    elif operator == '-':
        return float(operand_1) - float(operand_2)
    elif operator == '*':
        return float(operand_1) * float(operand_2)
    elif operator == '/':
        return float(operand_1) / float(operand_2)
    else:
        return "ERROR: There is no such an operator!"


def main():
    import sys
    if len(sys.argv) != 3:
        print("ERROR: This program needs two command line arguments to run,", end='')
        print(" where first one is the input file and the second one is the output file!")
        print("Sample run command is as follows: python3 calculator.py input.txt output.txt")
        print("Program is going to terminate!")
        sys.exit()

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    input_lines = input_reader_function(input_path)
    if input_lines is None:
        return None

    with open(output_path, 'w') as output_file:
        line_counter = 0
        for line in input_lines:
            line = line.strip()
            if not line:
                line_counter += 1
                continue

            elements = line.split()
            if len(elements) != 3:
                output_file.write(f"{line}\n")
                output_file.write("ERROR: Line format is erroneous!\n")
                line_counter += 1
                continue

            operand_1, operator, operand_2 = elements

            if not is_suitable(operand_1):
                output_file.write(f"{line}\n")
                output_file.write("ERROR: First operand is not a number!\n")
                line_counter += 1
                continue
            if not is_suitable(operand_2):
                output_file.write(f"{line}\n")
                output_file.write("ERROR: Second operand is not a number!\n")
                line_counter += 1
                continue

            if operator not in ['+', '-', '*', '/']:
                output_file.write(f"{line}\n")
                output_file.write("ERROR: There is no such an operator!\n")
                line_counter += 1
                continue

            result = calculator(operand_1, operator, operand_2)

            if find_floating_part_digits(result) > 2:
                result = round(result, 2)
            result = format(result, '.2f')
            line_counter += 1
            if line_counter == len(input_lines):
                output_file.write(f"{line}\n={result}")
            else:
                output_file.write(f"{line}\n={result}\n")
    output_file.close()


def find_floating_part_digits(number):
    int_part = round(number)
    float_part = number - int_part
    str_form = str(float_part)
    result = len(str_form) - 2
    return result


def is_suitable(var):
    try:
        var = float(var)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    main()
