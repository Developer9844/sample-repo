# Write a program that counts the frequency of words in a text document.


from collections import Counter
# import re

def count_word_frequency(text):
    # Remove special characters with the help of re module and convert to lowercase
    cleaned_text = text.lower()            # declear a variable to store the characters from the given file, set as lower
    
    # Split text into words
    words = cleaned_text.split()           # declear a variable which can store the split characters
    
    # Count the frequency of words
    word_count = Counter(words)            # Couter function will count the frequency of each word
    
    return word_count

# Read the text from a file
filename = 'sample-repo\index.txt'  # Replace with your file name
with open(filename, 'r') as file:
    text = file.read()

# Get the word frequency
word_frequency = count_word_frequency(text)

# Display the word frequency
for word, count in word_frequency.items():
    print(f'{word}: {count}')

#--------------------------------------------------------------

print("Second program will run now.")


def word_count(x):
    with open(x, 'r') as file:
        text = file.read()                     # all the characters of index file will store to 'text' variable
        words = text.split()                   # then we split the data and store it to 'words' variable

        total_words = len(words)               # then we count the words with the help of len function and that value will be stored in 'total_words'

    return total_words                         # return the value of the function by variable


filename = 'sample-repo\index.txt'             

my_file = word_count(filename)
print("Total word count from given file", my_file)
