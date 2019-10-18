#classify a range of numbers with respect to perfect, abundant or deficient

top_num = int(input("What is the upper number for the range: "))

number = 2

while number <= top_num:
    
    #sum the divisors of the number
    divisor = 1

    sum_of_divisors = 0

    while divisor < number:
        
        if number % divisor == 0:
            sum_of_divisors += divisor
            
        divisor += 1
    #classify the number based on it divisor sum
    if sum_of_divisors == number:
        print(number, "is perfect")
    if sum_of_divisors > number:
        print(number, 'is abundant')
    if sum_of_divisors < number:
        print(number, 'is deficient')    

    number += 1


    
