from generator import phrase_generator
from menu import menu
from hangman import draw_man

number_of_tries = 0
category, message = phrase_generator() #destructuring the return statement from phrase_generator similiar to Javascript's React's destructuring
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
selected_option = menu()
wrong_guesses = 0
puzzle_finished = False

#Function to display puzzle on screen
def display_puzzle(partial_puzzle):
    secret_message = ''
    if partial_puzzle == '':
        for char in message:
            if char == '\'' or char == "\"" or char == '-' or char == " ":
                secret_message += char
            else:
                secret_message += '_'
        return(secret_message)
    else:
        return partial_puzzle
            
#Function to reveal letter if in puzzle
def reveal_puzzle(letter, partial_message):
    puzzle = [character for character in message] #converts string to list, an item per character in the list puzzle
    secret_message = display_puzzle(partial_message) #message in secret in string form
    secret_message_list = [letter for letter in secret_message] #message in secret in list form
     
    for idx, char in enumerate(message):
        if char == letter:
            secret_message_list[idx] = puzzle[idx]
            partial_message = ''.join(secret_message_list)  
            #print("\nGood Guess.\n")
        if letter not in message:
            global wrong_guesses
            wrong_guesses += 1
            print("Wrong Guess.\n")
            draw_man(wrong_guesses)
            break
    
    return(partial_message)

#Main program
while wrong_guesses < 9:
    if selected_option == "No" or selected_option == "no" or selected_option == "NO" or selected_option == "N" or selected_option == "n":
        print("Good-bye Loser!")
        break
    else:
        if number_of_tries == 0:
            print("\n\nThe puzzle category is:  ", category)
            partial_message = ''
        print("\nAvailable letters are: ", alphabet)
        print("\n\n", display_puzzle(partial_message))
        if partial_message == message:
            print("\n")
            print("*******************")
            print("******YOU WIN******")
            print("*******************")
            puzzle_finished = True
            break
        letter = input("\n\nPlease choose a letter: ")
        print("\n")
        letter = letter.upper()
        if letter in alphabet:
            alphabet.pop(alphabet.index(letter))
        else:
            print("You have guessed that letter already.\n")
            continue
        number_of_tries += 1
        partial_message = reveal_puzzle(letter, partial_message)
        if wrong_guesses == 9:
            print("\nYOU LOSE!!")