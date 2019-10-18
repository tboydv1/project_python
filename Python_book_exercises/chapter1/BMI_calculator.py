#Body mass index calculator

## prompt for metrics weight and height


weight = int(input("Enter weigth in kilograms "))
height = int(input("Enter heigth in meteres "))

BMI = weight / (height**2)

print("Body mass index is: ", BMI)

