"""Implementation of the find function. Prints the index where
the target is found"""

river = 'Mississippi'
target = input('Input a character to find: ')
for index, letter in enumerate(river):
    if letter == target:
        print('Letter found at index: ', index)
        
else:
    print('Letter', target, 'not found in', river)
