# temp_file = open('input.txt', 'r')

# for line in temp_file:
#     print(line, end='')


input_object = open('input.txt', 'r')
output_object = open('output.txt', 'w')

for line_str in input_object:
    new_str = ''
    line_str = line_str.strip()
    for char in line_str:
        new_str = char + new_str
    print(new_str, file=output_object)

#line reversed is
    print("Line: {:12s} reversed is : {:s}".format(line_str, new_str))

input_object.close()
output_object.close()
