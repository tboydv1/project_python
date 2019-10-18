# Create a test file with a single sentence of 20 words. Read the file, then insert
# carriage-return characters (\n) and write the test to a new text file that will be
# composed of four lines of five words.

import string

def read_file():

    file1_obj = open("test.txt", "r")


    new_obj = open("outputTest.txt", 'w')

    for line in file1_obj:

        sentence = line.split(" ")

        for count, words in enumerate(sentence):

            print(words, file=new_obj, end=" ")

            print(words, end=" ")


            if(count % 5 == 0 and count > 1):
                print("\n", file=new_obj)
                print("\n")

    print(count)







read_file()