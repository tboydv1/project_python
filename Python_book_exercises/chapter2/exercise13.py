#Validate for and integer input

user_str = input("Input an integer: ")

status = True

while status:

    if user_str.isdigit():
        user_int = int(user_str)
        print("The integer is: {}".format(user_int) )
        status = False
    else:
        print("Error try again")
        user_str = input("Input an integer: ")

