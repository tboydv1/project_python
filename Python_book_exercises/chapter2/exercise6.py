# Write a for loop that will print “pbil” when “alphebetical” is the input

user_input = 'alphabetical'

new_str = ''
count = 2;
for i, j in enumerate(user_input):

    if i == 0:
        continue;
    if i % count == 0:
        new_str = new_str + j
        count = count + i + 1;
    if i % 8 == 0:
        new_str = new_str + j;

print(new_str)

