##validating that user input is not a string

Raw1 = input("Enter a number ")

if(Raw1.isdigit()):
   value = int(Raw1)
   print("Number is:", value)
else:
   print("Input is not a number")

 

