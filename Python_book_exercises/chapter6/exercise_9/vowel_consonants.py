"""Write a function that takes as input an English sentence (a string) and prints the total
number of vowels and the total number of consonants in the sentence. The function
returns nothing. Note that the sentence could have special characters like dots, dashes,
and so on"""

import string

def eliminate_bad_characters(sentence):

    bad_characters = string.whitespace + string.punctuation
    new_sentence = ""
    for i in sentence:
        if i in bad_characters:
            new_sentence += ""
        else:
            new_sentence += i
    return new_sentence

def count_vowels(sentence):
    vowels = 'aeiou'
    vowel_count = 0
    for i in sentence:
        if i in vowels:
            vowel_count += 1
    return vowel_count

def count_consonants(sentence):
    consonants = "bcdfghjklmnpqrstvwxyz"
    consonant_count = 0
    for i in sentence:
        if i in consonants:
            consonant_count += 1
    return consonant_count

def count_consonant_and_vowels():
    english_sentence = input("Enter a sentence ")

    new_sentence = eliminate_bad_characters(english_sentence)

    number_of_vowels = count_vowels(new_sentence)
    number_of_consonants = count_consonants(new_sentence)
    print("Number of vowels is: {}\nNumber of consonants is: {}\n".format(number_of_vowels, number_of_consonants))


def main():

    count_consonant_and_vowels()

if __name__ == '__main__':
    main()
