#progam takes an input and check if its a perfect square

num_str = input("Enter a number ")

#convert num_str to an integer
try:
    num_int = int(num_str)

#check for if a perfect square

    for i in  range(1, num_int // 2):

        if i**2 == num_int:
            print("{} is a perfect square".format(num_int))
            break
    else:
        print("{} is not a perfect square".format(num_int))

except ValueError as e:
    print("Invalid input")
