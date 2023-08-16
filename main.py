# # How to reverse the string

# def rev_str(x_str):

#     e_str = ""  # declaring an empty string to store the reverse string

#     for i in x_str:
#         # e_str = e_str + i           #this will get a string as it is, nothing will change
#         e_str = i + e_str
#     return e_str

# d = rev_str("Hello world")

# print(d)

# def rev_list(x_list):

#     e_list = " "  # declaring an empty string to store the reverse string

#     for i in x_list:
#         # e_str = e_str + i           #this will get a string as it is, nothing will change
#         e_list = i + " " + e_list      #this " " will help to seperate the items in reverse order in the list

#     # Remove the trailing space if it exists
#     if e_list:
#         e_list = e_list[:-1]

#     return [e_list]

# c = rev_list(["apple", "banana", "pine"])

# print(c)

import random

def guess_the_number():
    print("Welcome to the Guess the Number game!")
    print("I'm thinking of a number between 1 and 3. Can you guess it?")

    computer_number =  random.randint(1, 3)
    
    while True:
        # attempt = 0
        try:
            user_number = int(input("enter the number: "))
            # attempt = attempt + 1

            if user_number > 4:
                print("higher than expected")

            elif computer_number > user_number :
                print("number is low")

            elif computer_number < user_number:
                print("number is high")
            
            else:
                print(f"{user_number} number is correct, {computer_number}")
                break

        except ValueError:
            print("invalid entry")

guess_the_number()

#----------------------------------------------

def rev_str(my_str):
    final_str = ""         # declare an empty string to store the reverse order string

    for i in my_str:
        final_str = i + final_str    

    return final_str

d = rev_str("Hello")

print(d)

# explain: we pass "Hello", so now the i index will iterate and take 'H' from string and store it to 'final_str'
# in the next iteration, i will take 'e' and because of the condition "i + final_str" [('e' + 'H')=eH]
# after all the index done, the final output will 'olleH'
#-------------------------------------------------------------------------------------------------------------

# to- do list program

my_list = []    # create an empty list to store the user inputs

while True:     # we use the while true loop for infinite iterables and give the break instruction of specific keyword.
    
    user_input = input("Enter the item: \n")

    if user_input.lower() == "exit":
        break                   # this will break the loop if user enter the exit keyword

    my_list.append(user_input)
    
print(my_list)

# ----------------------------------------------------

from collections import Counter
import re

def count_word_frequency(text):
    # Remove special characters and convert to lowercase
    cleaned_text = re.sub(r'[^\w\s]', '', text.lower())
    
    # Split text into words
    words = cleaned_text.split()
    
    # Count the frequency of words
    word_count = Counter(words)
    
    return word_count

filename = 'sample-repo\index.txt'  # Replace with your file name

# Read the text from a file
with open(filename, 'r') as file:
    text = file.read()

# Get the word frequency
word_frequency = count_word_frequency(text)


# Display the word frequency
for word, count in word_frequency.items():
    print(f'{word}: {count}')

#-----------------------------------------------------------------------------

import os
import re

def rename_files(directory_path, search_pattern, replace_pattern):

    for filename in os.listdir(directory_path):

        old_filepath = os.path.join(directory_path, filename)

        if os.path.isfile(old_filepath):
            
            new_filename = re.sub(search_pattern, replace_pattern, filename)
            
            new_filepath = os.path.join(directory_path, new_filename)
            
            os.rename(old_filepath, new_filepath)
            
            print(f"Renamed: {filename} to {new_filename}")

if __name__ == "__main__":

    directory_path = "/path/to/your/directory"       # Update this with your directory path

    search_pattern = r"old_pattern"                  # Update this with the pattern you want to search for

    replace_pattern = r"new_pattern"                 # Update this with the pattern you want to replace with

    rename_files(directory_path, search_pattern, replace_pattern)
