#!/usr/bin/env python
#the re module to match the input credit card number against a regular expression pattern that repre#The ^ and $ characters in the pattern indicate the start and end of the string, respectively
#the [] characters are used to define a character class, which matches any one of the characters
# `|` character is used as an "or" operator inside the character class
#The ? character is used to match the preceding element
#The {} characters are used to specify the number of times the preceding element must be repeated
#The \d is used to match any digit

#Enter the card number to be tested in print(validate_credit_card("card_number"))
#Replace <card_number with> with the card number to be tested
#The script will return either true, false or too many characters or invalid.

import re

def validate_credit_card(card_number):
    pattern = "^[4|5|6][0-9]{3}-?[0-9]{4}-?[0-9]{4}-?[0-9]{4}$"
    result = re.match(pattern, card_number)
    if result:
        return True
    else:
        return False

# test with valid credit card numbers
print(validate_credit_card("4253625879615786")) 

# test with invalid credit card numbers
print(validate_credit_card("42536258796157867")) 

