from generator import phrase_generator
from menu import menu

hangman_count = 0

category, message = phrase_generator() #destructuring the return statement from phrase_generator similiar to Javascript's React's destructuring

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

selected_option = menu()

def display_puzzle():
    new_message = ''

    for char in message:
        if char == '\'' or char == "\"" or char == '-' or char == " ":
            new_message += char
        else:
            new_message += '_'
    #print("\n\n")
    #print(new_message)
    return new_message

def reveal_puzzle(letter):
    puzzle = [character for character in message] #converts string to list, an item per character in the list puzzle
    secret_message = display_puzzle() #message in secret in string form
    secret_message_list = [letter for letter in secret_message] #message in secret in list form

    print(secret_message)
    print("\n")
     
    for idx, char in enumerate(message):
        if char == letter:
            #idx = message.index(char) #This always returns the index of the first intance of the character.  NOT GOOD!
            secret_message_list[idx] = puzzle[idx]
            secret_message = ''.join(secret_message_list)

            #Testing print outs
            print("The current character in message is: ", message[idx])
            print("The index is: ", idx)
            print("puzzle[idx] = ", puzzle[idx])
            print("secret_message_list[idx] = ", secret_message_list[idx])
        print("The current letter is: ", char)
        
    print(secret_message)
            



#while True:
if selected_option == "No" or selected_option == "no" or selected_option == "NO" or selected_option == "N" or selected_option == "n":
    print("Good-bye Loser!")
    #break
else:
    print("\n\nThe puzzle category is:  ", category)
    
    print("\nAvailable letters are: ", alphabet)
    print("\n\n", display_puzzle())
    
    letter = input("\n\nPlease choose a letter: ")
    print("\n")
    letter = letter.upper()
    reveal_puzzle(letter)