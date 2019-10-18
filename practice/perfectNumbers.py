num = int(input("Enter any number except 1: "))

while(num > 1):
    
    if (num % 2 != 0):
        num += 1
    elif (num % 2 == 0):
        num /= 2

    print(int(num), end=" ")
print()
print("Final value is: ", int(num))
