from spy_detail import (spy, Spy, ChatMessage, friends)
# from steganography.steganography import stenography
# from colors import color
from datetime import datetime
import sys
from termcolor import colored, cprint

# import colors from colors.py for output/messages.
from colors import prCyan, prRed, prYellow, prGreen, prLightPurple, prPurple , R , B , Black

# Status Message List
STATUS_MSG = ["My name is Bond", "shaken,not stirred"]
question = input('Do you want to continue as ' + spy_sal + spy_name + ' Yes/No?')
existing = input(question)
if existing != 'Yes' or existing != 'No':
    prRed('Wrong input! try again ')
    existing = input(question)

# START Function to add status in Spy-chat
    def add_status(current_status_message):

        # status in beginning
        updated_status_message = None

        # check if current status is set or not
        if current_status_message is not None:
            print('Your current status message is %s \n' % current_status_message)
        else:
            print('You don\'t have any status message currently \n')

        # Ask user for choose default status or an old status.
        default = input(colored("Do you want to select from the older status (y/n)? ", 'cyan'))

        # when spy wants to add another status rather than existing one
        # .upper() converts everything to uppercase
        if default.upper() == "N":
            new_status_message = input(colored("What status message do you want to set?: ", 'cyan'))

            # validating users input.
            if len(new_status_message) > 0:
                # adding new status to default status or older status list.
                STATUS_MESSAGES.append(new_status_message)
                # updated status
                updated_status_message = new_status_message
                print('Your updated status message is: %s' % (updated_status_message))
            else:
                print("You did not provided any status message. Try again.")

        # spy wants to choose from existing status.
        elif default.upper() == 'Y':

            # counter for serial number of messages.
            item_position = 1

            # printing all older status messages so spy can choose
            for message in STATUS_MESSAGES:
                print('%d. %s' % (item_position, message))
                item_position = item_position + 1

            # asking users choice which index of list he wants to choose
            message_selection = int(input(colored("\nChoose from the Index of status: ", 'cyan')))

            # validating users input and set status of choice if exist.
            if len(STATUS_MESSAGES) >= message_selection:
                # updating
                updated_status_message = STATUS_MESSAGES[message_selection - 1]
                print('Your updated status message is: %s' % (updated_status_message))
            # when user has wrong choice or choice that does not exist.
            else:
                print("Invalid choice. Try again.")
        # when user has diffrent choice than yes and no
        else:
            print('The option you chose is not valid! Press either y or n.')
        # updated message will be read
        return updated_status_message
# END Function to add status in spy chat

# Function to add new friends.
    def add_friend():
        # using class spy
        new_friend = Spy(" ", " ", 0, 0.0)

        # ask user for name and salutation of friend
        new_friend.name = input("Please add your friend's name: ")
        pattern_n = '^[a-zA-Z\s]+$'
        # user validation.
        if len(new_friend.name) > 0 and re.match(pattern_n, new_friend.name) is not None:
            if len(new_friend.name) > 20:
                print("Your name is too big.")
        else:
            print("Name should be alphabetic")
            return add_friend()

        new_friend.salutation = input("What to call Mr. or Ms.?: ")
        pattern_s = '^[a-zA-Z\s]+$'
        # user validation
        if len(new_friend.salutation) > 0 and re.match(pattern_s, new_friend.salutation) is not None:
            if len(new_friend.salutation) > 5:
                print("Your salutation is too big.")
        else:
            print("Salutation should be alphabetic")
            return add_friend()

        # concatenation for full name
        new_friend.name = new_friend.salutation + " " + new_friend.name

        # ask for age of friend
        new_friend.age = (input("Age? "))
        new_friend.age = int(new_friend.age)
        # pattern_a = '^[0-9]+$'
        # user validation
        # if(re.match(pattern_a,new_friend.age)!=None):
        if 12 < new_friend.age < 50:
            True
        else:
            print("Age should be in between 12 to 50")
        # else:
        #     print ("Age should be Numeric.")
        # return add_friend()

        # ask for rating of friend, float represents type casting in float
        new_friend.rating = (input("Spy rating? "))
        new_friend.rating = float(new_friend.rating)
        # user validation.
        # pattern_r = '^[0-9]+\.[0-9]+$'
        # if(re.match(pattern_r,new_friend.rating)!= None):
        if new_friend.rating > 0.0:
            True
        else:
            print("Ratting should be more than 0.0")
        # else:
        #     print ("Ratting should be Numeric or Decimal.")
        # return add_friend()

        # add friend if conditions satisfies
        friends.append(new_friend)
        print('Friend Added!')

        # returning total no of friends.
        return len(friends)
    # END Function to add friend in spy chat

    # START function to select friend in spy chat
    def select_a_friend():
        item_number = 0
        for friend in friends:
            print(' %d.%s %s aged %d with rating of %.2f is online.' % (
                item_number + 1, friend.spy_name, friend.spy_age, friend.spy_ratings))
            item_number = item_number + 1
            friend_choice = input("Choose from your friends")
            friend_choice_position = int(friend_choice - 1)
            return friend_choice_position
    # END Function to select friend in spy chat

    # START Function to send message in Spy-chat
    def send_message():
        friend_choice = select_a_friend()
        # validation for not entering message
        while True:
            text = input("What do you want to say? ")
            words = text.split()
            length = sum(len(word) for word in words)
            #       if text !=("") and length <= 100
            #           steganography.encode(original_image, output_path, text)
            #           break
            #       prRed("ERROR !!! Either empty or 100 words exceeded")
            new_chat = ChatMessage(text, True)
            friends[friend_choice].chats.append(new_chat)
            print("Your secret message image is ready! ")
    # END Function to send message in Spy-chat

    # START Function to read message in SpyChat
    def read_message():
        sender = select_a_friend()
        #     output_path = input("What is the name of the file?")
        #     secret_text = Steganography.decode(output_path)
        new_chat = ChatMessage(secret_text, False)
        friends[sender].chats.append(new_chat)
        print(secret_text)
    # END Function to read message in SpyChat

    # START Function to read chat history in spy chat
    def read_chat_history():
        read_for = select_a_friend()
        print('\n')
        for chat in friends[read_for].chats:
            if chat.send_by_me:
                print('[%s]%s: %s' % (B + chat.time.strfttime('%d %B %y'), R + 'You said:', Black + chat.message))
            else:
                print('[%s] %s said: %s' % (
                    B + chat.time.strftime('%d %B %y'), R + friends[read_for].name, Black + chat.message))
    # END Function to read chat history in spy chat


# START Function to start spy chat
def start_chat(spy):
    spy.spy_name = spy.spy_sal + " " + spy.spy_name
    if 12 < spy.age < 50:
        print("Authentication complete. Welcome " + spy.spy_name + " age: " + str(spy.age) + " and rating of: " + str(
            spy.rating) + " Proud to have you onboard")
        show_menu = True
        # To Display SpyChat Menu
        while show_menu:
            menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n"
            menu_choice = input(menu_choices)
            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)
                if menu_choice == 1:
                    spy.current_status_message = add_status()
                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    prGreen('You have %d friends' % number_of_friends)
                elif menu_choice == 3:
                    send_message()
                elif menu_choice == 4:
                    read_message()
                elif menu_choice == 5:
                    read_chat_history()
                else:
                    show_menu = False
    else:
        print('Sorry you are not of the correct age to be a spy')


if existing.upper() == "Y":
    start_chat(spy)
else:
    spy = Spy('', '', 0, 0.0)
    # Validation for spy name
    while True:
        spy.name = input("Welcome to spy chat, you must tell me your spy name first: ")
        if spy.name.replace(" ", "").isalpha():
            break
        # Calling Color Red to print error message
        prRed("ERROR !!! Invalid Name")
    if len(spy.name) > 0:
        # Validation for spy salutation
        while True:
            spy.salutation = input("Should I call you Mr or Ms ?:")
            if spy.salutation.replace(".", "").isalpha():
                break
            # Calling Color Red to print error message
            prRed("ERROR !!! Invalid Salutation")
        # Validation for spy age
        while True:
            spy.age = input("What is your age? ")
            if spy.age.replace("", "").isdigit():
                spy.age = int(spy.age)
                break
            # Calling Color Red to print error message
            prRed("ERROR !!! Age should be in NUMBERS")
        # Validation for spy rating
        while True:
            spy.rating = input("What is your spy rating? ")
            if spy.rating.replace(".", "").isdigit():
                spy.rating = float(spy.rating)
                break
            prRed("ERROR !!! Rating should be in Numbers and Precise")
            # Condition to print spy_rating level
        if spy.rating > 0:
            if spy.rating >= 3.5 <= 5.0:
                prLightPurple("Expert Level")
            elif spy.rating >= 2.5 <= 3.4:
                prPurple("Amateur Level")
            else:
                prYellow("Beginner Level")
        start_chat(spy)
    else:
        print('Please add a valid spy name')
# END Function to start spy chat
