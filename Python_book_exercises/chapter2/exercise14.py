#Program generates arithmetic sequence

a_str = ''
b_int = 0
c_str = ''

for i in range(1, 10):
    c_str = str(i)
    a_str = a_str + c_str
    b_int = int(a_str)
    b_int = b_int * 8 + i
    print('{} * {} + {} = {}'.format(a_str, 8, i, b_int))

print()
a_str = ''
b_int = 0
c_str = ''
for i in range(1, 1):
    c_str = str(i)
    a_str = a_str + c_str
    b_int = int(a_str)
    b_int = b_int * 9 + i
    print('{} * {} + {} = {}'.format(a_str, 9, i, b_int))
