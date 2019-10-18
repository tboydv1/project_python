#Gettysburg address analuysis
# count words, unique words
import string

char = string.punctuation
print(char)

def make_words_list(a_file):
    """Create a list of words from a file"""
    word_list = [] #list of speech words

    for line_str in a_file:
        line_list = line_str.split()

        for word in line_list:
            if word != char:
                word_list.append(word)

    return word_list

def get_unique_words(word_list):
    """fuction gets list of unuique words in the list"""

    unique_words = []
    for word in word_list:
        if word not in unique_words:
            unique_words.append(word)

    return unique_words

###############################################
#open file for reading
try:
    gba_file = open("/home/oluwatobi/Documents/Pdf books/gettysburg.txt", "r")
except FileNotFoundError:
    print("Error processing file")

speech_list = make_words_list(gba_file)

print(speech_list)
print("Length: ", len(speech_list))
print("Unique words length", len(get_unique_words(speech_list)))