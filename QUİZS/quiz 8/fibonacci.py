def input_reader(input_path):
    """This function reads the input file and make it into a list"""
    with open(input_path, 'r') as input_script:
        list = input_script.readlines()
        a_list = [int(line.strip()) for line in list]
        return a_list  # input numbers list


def naive_fibonacci_func(n, output):
    """The function writes the n. fibonacci number with wanted format to output file
    by using naive approach."""
    if n > 2:
        output.write(f"fib({n}) = fib({n - 1}) + fib({n - 2})\n")
        result = naive_fibonacci_func(n - 1, output) + naive_fibonacci_func(n - 2, output)
        return result
    elif n == 2:
        output.write("fib(2) = 1\n")
        return 1
    elif n == 1:
        output.write("fib(1) = 1\n")
        return 1
    else:
        output.write("ERROR: Fibonacci cannot be calculated for the non-positive numbers!\n")
        return None

def fibonacci_func_result(n):
    """This function only returns the result of the fibonacci functions"""
    if n > 2:
        result = fibonacci_func_result(n - 1) + fibonacci_func_result(n - 2)
        return result
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return 'nan'

def eager_fibonacci_func(n, list, output):
    """This function keeps the fibonacci numbers in a list writes the intended format for argument n to output file
     and uses the eager approach to calculate result"""
    if n > 0:
        if len(list) < n:  # in case number's correspond one is not in list
            output.write(f"fib({n}) = fib({n - 1}) + fib({n - 2})\n")
            result = eager_fibonacci_func(n - 1, list, output) + eager_fibonacci_func(n - 2, list, output)
            list.append(result)  # then it is also appended to list
            return result
        elif n == 1:
            output.write(f"fib({n}) = 1\n")
            return list[0]
        elif n == 2:
            output.write(f"fib({n}) = 1\n")
            return list[1]
        else:
            output.write(f"fib({n}) = {list[n-1]}\n")
            return list[n-1]
    else:
        output.write("ERROR: Fibonacci cannot be calculated for the non-positive numbers!\n")
        return None


def main():
    """This function bodies every step and function"""
    import sys
    input_list = input_reader(sys.argv[1])
    with open(sys.argv[2], 'a') as output:
        for i in input_list:  # every element looping
            output.write(f"--------------------------------\n")
            output.write(f"Calculating {i}. Fibonacci number:\n")
            naive_fibonacci_func(i, output)
            output.write(f"{i}. Fibonacci number is: {fibonacci_func_result(i)}\n")
        output.write(f"--------------------------------")

    default_structure = [1, 1]
    with open(sys.argv[3], 'a') as output:
        for i in input_list:  # every element looping
            output.write(f"--------------------------------\n")
            output.write(f"Calculating {i}. Fibonacci number:\n")
            eager_fibonacci_func(i, default_structure, output)
            output.write(f"{i}. Fibonacci number is: {fibonacci_func_result(i)}\n")
        output.write(f"--------------------------------\n")
        output.write(f"Structure for the eager solution:\n{default_structure}\n")
        output.write(f"--------------------------------")


if __name__ == "__main__":
    main()
