
def func1 (str1, str2):
    if str1 > str2:
        result_str = str1[1:]
    else:
        result_str = str2[:-1]
    return result_str

#main program
responses1_str = input("Enter a string:")
responses2_str = input("Enter a second string:")
dir(list)

print(func1(responses1_str, responses2_str))
print(func1(responses2_str, responses1_str))

