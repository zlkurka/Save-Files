from string import ascii_uppercase
from collections import Counter

def menu(options=list, menu_text=str):

    # Printing menu
    print(menu_text)
    for item_num in range(len(options)):
        try:
            print(f'{ascii_uppercase[item_num]}) {options[item_num].value.capitalize()}')
        except AttributeError:
            print(f'{ascii_uppercase[item_num]}) {str(options[item_num]).capitalize()}')
        # Will print like "A) Squid"

    # Taking input and translating to list item
    while True:

        selection = input().upper().strip()

        if selection not in list(ascii_uppercase):
            print('Invalid input! Enter only the letter corresponding to your selection.')
        
        elif list(ascii_uppercase).index(selection) > len(options) - 1:
            print('Invalid input! This letter does not correspond to an option.')
        
        else:
            return options[list(ascii_uppercase).index(selection)]