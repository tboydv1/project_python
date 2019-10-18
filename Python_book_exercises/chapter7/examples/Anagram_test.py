#Anagram test

def are_anagrams(word1, word2):
    """Return true if words are not anagrams"""
    word1_sorted = sorted(word1)
    word2_sorted = sorted(word2)

    return word1_sorted == word2_sorted

print("Anagram Test")
#validate user input

valid_input = False

while(not valid_input):
    try:
        two_word = input("Enter two space seperated words")
        word1, word2 = two_word.split(" ")
        valid_input = True
    except ValueError as e:
        print("Bad Input")

if are_anagrams(word1, word2):
    print("The words {} and {} are anagrams".format(word1, word2))
else:
    print("The words {} and {} are anagrams".format(word1, word2))