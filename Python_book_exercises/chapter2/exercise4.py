#Body mass Index Calculator

user_option = (input("Enter 1 To calculate BMI in (Kiligrams / metres) or 2 for BMI in (pounds / inches)"))

if user_option:
    print("Invalid input")
else:
    user_option = int(user_option)

    weight_float, height_float = float(input("Enter weight in kilograms \ "
                                            "and height in metres"))

    if(user_option == 1):
        BMI = weight_float / height_float

    elif(user_option == 2):
        weight_in_kil = weight_float / 2.20462
        height_in_met = height_float / 39.37
        BMI = weight_in_kil / (height_in_met ** 2)

    print("Body Mass Index is: ", BMI)

