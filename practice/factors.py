#get the input
num = int(input("Please type a number and enter: "))

#store the value
sum = 0

print("Factors are: ", end=' ')
#generate factors
for i in range(1, num):

    if(num % i == 0):
        print(i, end=' ')
    #sum the factors
        sum += i

print()
print("Sum: ",sum)
