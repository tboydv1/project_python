#read a particular line from a file. User provides bothe the line
#numbe and the file name

file_str = input("Open what file: ")
status = True
while status:
    try:
        input_file = open(file_str)
        find_line_str = input("Which line (integer): ")
        find_line_int = int(find_line_str)

        for count, line_str in enumerate(input_file):
            if count == find_line_int:
                print("Line {} of file {} is {}".format(find_line_int, file_str, line_str))
                status = False
                break
        else:
            print("Line {} of file {} not found ".format(find_line_int, file_str))
        input_file.close()

    except FileNotFoundError:
        print("File not foundf")
        file_str = input("Open what file:")

    except ValueError:
        print("Line", find_line_str, "isn't a legal line number")
        find_line_str = input("Which line (integer): ")

print("End of program")