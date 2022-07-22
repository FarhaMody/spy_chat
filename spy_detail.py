# importing datetime to show time and date of chat.
from datetime import datetime


# class for spy
class Spy:
    def __init__(self, name, salutation, age, rating):
        # initializing the values
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None

        # counting the number of words
        self.count = 0


# a class for chat messages
class ChatMessage:
    def __init__(self, message, sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me


# details of default user.
spy = Spy('BOND', 'Mr.', 29, 4.9)

# details of some existing friends
friend_one = Spy('Anurag, ', 'Mr.', 21, 4.8)
friend_two = Spy('Rajan, ', 'Mr.', 20, 4.6)
friend_three = Spy('Nitkarsh, ', 'Mr.', 21, 4.7)

# lists of existing friends
friends = [friend_one, friend_two, friend_three]
