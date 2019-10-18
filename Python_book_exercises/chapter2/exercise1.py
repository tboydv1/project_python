##Program to find how many numbers are divisible by three

print("Three digit numbers divisible by 17 are: ")
for i , j in enumerate(range(102, 999, 17)):
    if(j % 17 == 0):
       print( j , end = " ");

    if(i % 5 == 0):
        print("\n")