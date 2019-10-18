#print all numbers divisible by 17

divisor = 17

numbers = 100

while numbers <= 999:

    if(numbers % divisor == 0):
        print(numbers, 'is divisible by 17')
    numbers += 1

        
