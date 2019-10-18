"""Write a program that prompts for an integer—let’s call it X—and then finds the
sum of X consecutive integers starting at 1."""

value_str = input("Enter a value ")
sum = 0
count = 0
try:
    #convert input to int
    value_int = int(value_str)
    print("Consecutive sums: ")
    for i in range(1, value_int + 1):
        # for j in range(1, i + 1):
        sum += i

        print(sum)
    # sum = 0
    if sum % len(range(1, value_int + 1)) == 0:
        print("Total sum: ",sum, end=" ")
    else:
        print("Sum is not divisible by number")


        # print(i)


except ValueError:
    print("Invalid input")
