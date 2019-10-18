import string

file_name = input("Enter file name: ")

dict_obj = open('dictionary.txt', 'w')
bad_char = string.punctuation + string.whitespace
while True:
    try:
        file_obj = open(file_name, 'r')
        letter = ''
        count = 0

        for line in file_obj:

            for char in line:
                # if char == letter:
                count += 1
                print(char, "and ", count)
        file_obj.close()
    except FileNotFoundError:
        print("Try again")
        file_obj = open(file_name, 'r')




