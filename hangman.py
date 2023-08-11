import random

random_list = ["temple", "keyboard", "mouse", "card", "mobile"]       # this is a list which containes random items name
computer_guessed = random.choice(random_list)                         # we call the random module for randomly select the list item
word_lenth = len(computer_guessed)                                    # we count the word which was guessed by computer

guessed_letters = []                                                  # we need to create ab empty list which can store the user inputs
attempts = 5                                                          # we can give any no. of attempts to the user for guessing the letter of the word guessed word 

print("Welcome to the Gamezone") 
print("_ " * word_lenth)                                              # this will print the _ * word count. e.g. len(word)=6 then the output will "_ _ _ _ _ _"

while attempts > 0:                                                   # we are using while loop to set a condition over the attempts made by user
    user_guessed = input("guessed the letter: ")  

    if user_guessed in guessed_letters:          # if user guessed the same letter then user will get the warning message
        print("you already guess the letter")
        continue                                 # then loop will continue and further proceed
    guessed_letters.append(user_guessed)

    if user_guessed in computer_guessed:         # if user guessed the letter which is present in computer guessed word
        print("correct")                         # then the output will correct
    else:                                        # And if incorrect, it shows the incorrect message to the user and loop will further proceed
        print("incorrect")
        attempts = attempts - 1                  # also the incorrect attempt will minus and the loop will again proceed from begining
    
    # display the current letters
    display_word = ""                            
    for i in computer_guessed:                   
    # we are constructing the display_word string                      
    # by using iterating through the computer_guessed string. E.g. computer guess "temple"
    # i will corresoponds to all the letter (t e m p l e)

        if i in guessed_letters:
        # we are conditioning the loop i.e. if i is also present in guessed letters(t or e or m or p or l) 
            display_word = display_word + i + " "
        # then concatenate the letter in display word with space(" ")
        else:
            display_word = display_word + " _"
        # or displays the blank spaces(unguessed word) with " _"

    print(display_word)           # if user guesses t and m then it will shows "t _ m _ _ _"

    # check if word has been guessed
    if "_" not in display_word:
        # if all blank spaces in display_word will occupied then 
        print("you guess the correct word:", computer_guessed)
        break

    print("remaining attemps: ", attempts)
        

if attempts == 0:
    print(f"Sorry, your attempts are full. The word is '{computer_guessed}'")


