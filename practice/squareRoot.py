import math

num = int(input("Enter a number: "))

guess = int(input("Guess its square root: "))

new_guess = 0

while new_guess < (guess + .5):
    
    quotient = num / guess
   

    print(quotient," m")
    average = (quotient + guess) / 2

    new_guess = average

    if(new_guess >= (guess + .5)):
         print(new_guess, " g" )
         break
         
   
        

    

