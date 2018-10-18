from map import rooms
from player import *
from items import *
from gameparser import *
import string
skip_words = ['a', 'about', 'all', 'an', 'another', 'any', 'around', 'at',
              'bad', 'beautiful', 'been', 'better', 'big', 'can', 'every', 'for',
              'from', 'good', 'have', 'her', 'here', 'hers', 'his', 'how',
              'i', 'if', 'in', 'into', 'is', 'it', 'its', 'large', 'later',
              'like', 'little', 'main', 'me', 'mine', 'more', 'my', 'now',
              'of', 'off', 'oh', 'on', 'please', 'small', 'some', 'soon',
              'that', 'the', 'then', 'this', 'those', 'through', 'till', 'to',
              'towards', 'until', 'us', 'want', 'we', 'what', 'when', 'why',
              'wish', 'with', 'would']

def filter_words(words, skip_words):
    words = [word for word in words if word not in skip_words]
    return words

def remove_punct(text):
    no_punctuation = ""
    for char in text:
        if not (char in string.punctuation):
            no_punctuation = no_punctuation + char
    return no_punctuation

def normalise_input(user_input):
    no_punct = remove_punct(user_input).lower()
    normalised_input = filter_words(no_punct.split(), skip_words)
    return normalised_input

def list_of_items(items):
    list_items = ", ".join([name['name'] for name in items])
    return list_items

def print_room_items(room):
    if list_of_items(room["items"]) == "":
        print("")
    else:
        print("There is ", list_of_items(room["items"]), "here.")
        print("")
    
def print_inventory_items(items):
    list_inventory = ", ".join([name['name'] for name in items])
    print("You have", list_inventory)
    print("")
    
def print_room(room):
    print()
    print(room["name"].upper())
    print()
    # Display room description
    print(room["description"])
    print()
    print_room_items(room)
    
def exit_leads_to(exits, direction):
    return rooms[exits[direction]]["name"]

def print_exit(direction, leads_to):
    print("GO " + direction.upper() + " to " + leads_to + ".")
    
def print_menu(exits, room_items, inv_items):
    print("You can:")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))
    for items in inventory:
        print_

    print("What do you want to do?")

def is_valid_exit(exits, chosen_exit):
    return chosen_exit in exits
    

print_room_items(rooms["Admins"])
