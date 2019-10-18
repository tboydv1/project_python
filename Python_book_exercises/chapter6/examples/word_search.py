# read through file one line at a time

def clean_word(word):
    return word.strip().lower()

def get_vowel_in_word(words):
    vowel = "aeiou"
    vowel_in_word = ''

    for char in words:

        if char in vowel:
            vowel_in_word += char
    return vowel_in_word

# main program

# def main():
file_obj = open("dictionary.txt", "r")

word = ""
vowel_word = ""
vowels = "aeiou"

for line in file_obj:
    word = clean_word(line)
    if len(word) <= 6:
        continue

    vowel_word = get_vowel_in_word(word)


    if vowel_word == vowels:
        print(word)







