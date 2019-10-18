"""This program checks for palindrom"""
import string

original_str = input("Enter string to check: ").lower()

#change original case to lower case
# modified_str = original_str.lower()

bad_chars = string.whitespace + string.punctuation

modified_str = ''
#check and store good characters
for char in original_str:

    if char in bad_chars:
        continue;
    else:
        modified_str = modified_str + char
        
#check if palindrome
if modified_str == modified_str[::-1]:
    print(\
'The original string is: {:<30s}\n\
the modifies string is: {:<30s}\n\
the reversal is:        {:37s}\n\
String is a palindrome'.format(original_str, modified_str, modified_str[::-1]))
else:
    print(\
'The original string is: {:<30s}\n\
the modifies string is: {:<30s}\n\
the reversal is:        {:37s}\n\
String is not a palindrome'.format(original_str, modified_str, modified_str[::-1]))
    

        
