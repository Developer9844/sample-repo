# to- do list program

my_list = []    # create an empty list to store the user inputs

while True:     # we use the while true loop for infinite iterables and give the break instruction of specific keyword.
    
    user_input = input("Enter the item: \n")

    if user_input.lower() == "exit":
        break                   # this will break the loop if user enter the exit keyword

    my_list.append(user_input)
    
print(my_list)