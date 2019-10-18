file_object = open("my_file.txt", "w")

print('Jacob', file=file_object)
print("Dami", file=file_object)
print("Tobi", file=file_object)

file_object.close()


input_file = open("input.txt", 'r')
output_file = open("output.txt", 'w')

for line_str in input_file:
    new_str = ''
    line_str = line_str.strip()
    for char in line_str:
        new_str = char +     new_str
    print(new_str, file=output_file)

    print('Line: {:12s} reversed is: {:s}'.format(line_str, new_str))

input_file.close()
output_file.close()
