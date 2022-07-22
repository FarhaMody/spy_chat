# start_chat() function definition.
from main_spy import add_status, add_friend, send_message, read_message, read_chat_history


def start_chat(name, age, rating, status):

    # age should be greater than 12 and less than 50.
    if not (12 < age < 50) :
        # invalid age.
        error_message = "Invalid age. Provide correct details."
        print("error_message")
    else:
        # authentication complete
        # show all the spy details
        # show a greeting message.
        welcome_message = "Authentication complete. Welcome\n\n" \
                          "Name : " + name + "\n" \
                          "Age: " + str(age) + "\n" \
                          "Rating: " + str(rating) + "\n" \
                          "Proud to have you on board\n"
        print (welcome_message)

        # displaying menu for user.
        show_menu = True
        while show_menu:
            menu_choices = "What do you want to do? \n\n " \
                           "1. Add a status update \n " \
                           "2. Add a friend \n " \
                           "3. Send a secret message \n " \
                           "4. Read a secret message \n " \
                           "5. Read Chats from a user \n " \
                           "6. Close Application \n\n"
            result = int(input(menu_choices))

            # validating users input
            if (result == 1):
                # set your current status
                current_status_message = add_status(current_status_message)
            elif (result == 2):
                # add a new friend
                number_of_friends = add_friend()
                print ('You have %d friends' % (number_of_friends))
            elif(result == 3):
                # send a secret message
                send_message()
            elif (result == 4):
                # read the secret message sent by friend
                read_message()
            elif(result == 5):
                # read the chat history
                read_chat_history()
            elif (result == 6):
                # close application
                show_menu = False

            # if user chooses other than menu choices.
            else:
                print("wrong choice try again.")
                exit()
