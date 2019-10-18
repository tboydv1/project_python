#hangman game

from hangman_status import *
## Draw and entire hangman status
##with a full picture for each partial hangman status


"""Hang man game implementation"""
#First player inputs a secret word and a guess
drawing = 0
try:
    player1 = input("Enter a secret word and a hint seperated by comma: ")
    secret_word , hint = player1.split(',')
except ValueError:
    pass
    

##create a list of dashes  lenght of word and a placeholder

place_holder = list(range(len(secret_word)))

for j,i in enumerate(place_holder):
    
    place_holder[j] = "_"
    
           


## input second player guess

game_status = True

right_guess_count = 0


print("Hint: {}\n".format(hint))
while(game_status):

    guess = input("Guess a letter in the secret word ")

    """Check if guess is in secret_word"""
    if guess in place_holder:
        check = secret_word.find(guess, secret_word.find(guess) + 1)
    else:
        check = secret_word.find(guess)
    

    
    if check > -1:
        if secret_word[check] in place_holder[check]:
            print("You already guessed letter {}", secret_word[check])
            continue
        place_holder[check] = guess
        print("You guessed a letter in the secret word", "\n",place_holder ,"\n")
        right_guess_count += 1
    elif drawing <= 6:
        print("oops the leter {} is not in the secret word\n".format(guess))
        print("Hang man status is: ", full_hangman[drawing])
        drawing += 1

## final game status check
        
    if right_guess_count >= len(secret_word):
        print("Weldone you guess the word correctly")
        game_status = False
        
    elif drawing > 6:
        print("Hangman hooked, game over")
        game_status = False


