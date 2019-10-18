##Standard BMI Calculator

weight_in_pounds = float(input("Enter weigth in pounds "))
height_in_inches = float(input("Enter heigth in inches "))

weight_in_kil = weight_in_pounds / 2.20462
height_in_met = height_in_inches / 39.37

BMI = weight_in_kil/(height_in_met**2)

print("Body mass index is: ", BMI)
