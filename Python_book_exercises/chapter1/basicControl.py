user_int = int(input('Enter a positive integer: ')) #1

count = 0

while user_int > 0:
    if user_int % 2 == 1:
        user_int = user_int // 2
    else:
        user_int -= 1
    count += 1

print(count)
print(user_int)
