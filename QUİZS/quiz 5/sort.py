def input_file_reader(input_file):
    """This function is used for taking input information from input file
    it gives the list of the numbers which will be sorted as return value"""
    input_form = open(input_file, 'r')
    list_of_numbers = [int(line) for i in input_form for line in i.strip().split(" ")]
    return list_of_numbers


def is_it_sorted_form(list):
    """is_it_sorted_form function is created to arrange and control
    the right timing for terminating the sorting procedure"""
    control_list = list.copy()
    for passing_nums in range(len(control_list)-1, 0, -1):
        for i in range(passing_nums):
            if control_list[i] > control_list[i+1]:  # in this if block, transferring
                temp_var = control_list[i]           # temporary element to other steps
                control_list[i] = control_list[i+1]  # is aimed
                control_list[i+1] = temp_var
    if control_list == list:
        return True
    else:
        return False


def bubble_sort_func(list, output_path):
    """This function sorts the numbers from small one to big one
     by comparing and swapping pairs of numbers"""
    if len(list) == 1:      # in case there is only one number in list.
        output_path.write("Already sorted!")
    else:
        pass_num = 0
        for passing_num in range(len(list) - 1, 0, -1):  # to provide the wide scope sorting
            for i in range(passing_num):                 # passing number is chosen big
                if list[i] > list[i + 1]:
                    temp_var = list[i]
                    list[i] = list[i + 1]
                    list[i + 1] = temp_var
            if is_it_sorted_form(list) is False:         # is_it_sorted_form() function is called
                pass_num += 1                            # to know whether list has already sorted or not
                output_sort_func(output_path, list, pass_num)
        pass_num += 1
        output_sort_func(output_path, list, pass_num)


def insertion_sort_func(list, output_path):
    """this function sorts the given list by applying insertion sorting algorithm"""
    if len(list) == 1:        # in case there is only one number in list.
        output_path.write("Already sorted!")
    else:
        pass_num = 0
        for index in range(1, len(list)):
            current_element = list[index]         # it transfers the values bigger than current one
            current_location = index                    # to the right side of list
            while current_location > 0 and list[current_location - 1] > current_element:
                list[current_location] = list[current_location - 1]
                current_location -= 1
                list[current_location] = current_element
            pass_num += 1
            output_sort_func(output_path, list, pass_num)


def output_sort_func(output_file, list, pass_num):
    """This function is used to print them outputs inside  the output file"""
    output_file.write("Pass {}: ".format(pass_num))
    for i in list:
        output_file.write("{} ".format(i))
    output_file.write("\n")


def main():
    """This function is for summing the all functions,
    calling necessary libary and some value assignments"""
    import sys
    input_file = open(sys.argv[1], "r")
    output_file1 = open(sys.argv[2], 'w')
    output_file2 = open(sys.argv[3], 'w')
    if len(input_file.read().strip().split()) == 0:
        output_file2.write("Already sorted!")
        output_file1.write("Already sorted!")
        output_file1.flush()
        output_file1.close()
        output_file2.flush()
        output_file2.close()
    else:
        numbers = input_file_reader(sys.argv[1])
        bubble_sort_func(numbers, output_file1)
        output_file1.flush()
        output_file1.close()
        insertion_sort_func(numbers, output_file2)
        output_file2.flush()
        output_file2.close()


if __name__ == "__main__":
    main()
