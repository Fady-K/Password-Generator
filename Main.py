# Program Name: Password Generator
# Author: Fady Kamal Ibrahim
# Program Description: This Program will Help To Generate A Password of a Particular Length, In Addition To Giving The user Ability To Determine the Types Of Letters To Be Included In The Password
# Last Modification Date: 4/13/2022
# Purpose: Trying To Help People Struggling With Franco Letters
################################################################
import random
import string

################################################################
# program initial status
choice = None              # choice represents the user choice (1 to generate password, 2 to exit)
password_length = None     # represents the length of generated password, also will help to determine N_of_loops
program_running = True     # initial status of program
big_letters = None         # this will store value taken from user (Y/N) To know if user wants big letters in Generated Password or not
small_letters = None       # this will store value taken from user (Y/N) To know if user wants small letters in Generated Password or not
special_char = None        # this will store value taken from user (Y/N) To know if user wants Special letters in Generated Password or not
Nums = None                # this will store value taken from user (Y/N) To know if user wants Nums in Generated Password or not
password = ""              # this will get Concatenated with the desired letters
abc_upper = list(string.ascii_uppercase)       # ABC Letters in Upper Case
abc_lower = list(string.ascii_lowercase)       # ABC Letters in Lower Case
special_char_list = list("!@#$%^&*()_+-=/<>")  # Special Letters
Nums_list = list("0123456789")                 # Numbers List

############################
# display Function
def Display(isFirstTime):   # Display 2 Options to user (Generate Password, Exit) then return his choice
    global choice           # Update choice from user
    if (isFirstTime):       # isFirstTime Holds bool Value, True If it's the first open to program(just to print Welcome Message)
        print(f"!! Welcome To Password Generator !!")
    print(f"1- Generate A password\n2- Exit")
    choice = input("What Do You Want To Do?: ".title())
    return choice

######################
# take_input_and_check (to take input and check the input taken from the user)
def take_input_and_check(input_, isLetters, isLen, letters_to_determine):
    if isLen:           # isLen Holds bool value True to take int value to store it in Password_Length
        input_ = input("Enter the password Length: ".title())
        while not input_.isdigit():       # this will check whether user entered int or not
            print('#'*20)
            print(f"!! Invalid !! >> try again".title())
            print('#'*20)
            input_ = input("Enter the password Length (Restricted To Be int): ".title())

    elif isLetters:     # isLetter Holds bool value True to take input from user (Y/N), Depending on
        # letters_to_determine Holds A letter, this letter will Determine Which Message to Display
        if letters_to_determine == 'b':
            input_ = input("do you want password to include Big_letters? (Y/N): ".title()).upper()
        elif letters_to_determine == 's':
            input_ = input("do you want password to include small_letters? (Y/N): ".title()).upper()
        elif letters_to_determine == "sp":
            input_ = input("do you want password to include special_letters? (Y/N): ".title()).upper()
        elif letters_to_determine == "num":
            input_ = input("do you want password to include Nums? (Y/N): ".title()).upper()
        while input_ not in ["Y", "N"]:   # this loop while Keep iterating (Printing Invalid) As long As input != Y or N
            print('#'*20)
            print(f"!! Invalid !! >> try again".title())
            print('#'*20)
            if letters_to_determine == 'b':
                input_ = input("do you want password to include Big_letters? (Y/N): ".title()).upper()
            elif letters_to_determine == 's':
                input_ = input("do you want password to include small_letters? (Y/N): ".title()).upper()
            elif letters_to_determine == "sp":
                input_ = input("do you want password to include special_letters? (Y/N): ".title()).upper()
            elif letters_to_determine == "num":
                input_ = input("do you want password to include Nums? (Y/N): ".title()).upper()
    return input_       # return A valid input_

######################
# Take_input Function
def Take_input():
    global big_letters, small_letters, special_char, Nums, password_length
    password_length = take_input_and_check(password_length, False, True, None)
    big_letters = take_input_and_check(big_letters, True, False, 'b')
    small_letters = take_input_and_check(small_letters, True, False, 's')
    special_char = take_input_and_check(special_char, True, False, "sp")
    Nums = take_input_and_check(Nums, True, False, "num")

#####################
# shuffle Function (This Function Will Shuffle The Generated Password To Get Rid of Any Patterns)
def shuffle_(password):
    return random.shuffle(list(password))

###################
# password Generator
def Password_generator(abc_upper, abc_lower, special_char_list, Nums_list):
    global password, big_letters, small_letters, special_char, Nums, password_length  # to modify them directly
    for i in range(int(password_length)):
        # this will check if (B|S|special_Letters|Nums) included and len_of_generated is smaller than the desired len
        if big_letters == "Y" and (len(password) < int(password_length)):
            password += random.choice(abc_upper)      # concatenate Password with A random letter from big_letters (ABC)
        if small_letters == "Y" and (len(password) < int(password_length)):
            password += random.choice(abc_lower)      # concatenate Password with A random letter from big_letters (ABC)
        if special_char == "Y" and (len(password) < int(password_length)):
            password += random.choice(special_char_list)    # concatenate Password with A random Special char
        if Nums == "Y" and (len(password) < int(password_length)):
            password += random.choice(Nums_list)      # concatenate Password with A random Number from Nums_list

    shuffle_(password)
    print('#' * 20)
    print(f"Generated Password: {password}")
    print('#' * 20)
    password = ""       # Clear The Password Incase User Didn't Terminate Program

############################
# The Main Program
Display(True)
while program_running:
    if choice == "1":
        Take_input()
        Password_generator(abc_upper, abc_lower, special_char_list, Nums_list)
    elif choice == "2":
        program_running = False
        break
    else:
        print('#' * 20)
        print(f"!! invalid !!".upper())
        print('#' * 20)
    Display(False)
