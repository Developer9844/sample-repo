def letter_frequency(text):
    frequency = {}

    for char in text:
        if char.isalpha():  # Check if the character is a letter
            char = char.lower()  # Convert to lowercase to treat letters case-insensitively
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1

    for char, count in frequency.items():
        print(f"{char}: {count}")



# with open("sample-repo\index.txt", 'r') as file:
#     text = file.read()

text = "Convert to lowercase to treat letters case-insensitively"
letter_frequency(text)

#---------------------------------------------------------------------------------------------------------------------------

phonebook = {}

def add_contact(name, phone_number):
    phonebook[name] = phone_number

def lookup_contact(name):
    if name in phonebook:
        return phonebook[name]
    else:
        return "Contact not found"

while True:
    print("1. Add Contact")
    print("2. Lookup Contact")
    print("3. Quit")
    choice = input("Select an option: ")

    if choice == "1":
        name = input("Enter name: ")
        phone_number = int(input("Enter phone number: "))
        add_contact(name, phone_number)
    elif choice == "2":
        name = input("Enter name to lookup: ")
        print(lookup_contact(name))
    elif choice == "3":
        break

print(phonebook)