# This dictionary is linked to an spdict.json file I created 
# difflib with get_close_matches works to compare similar word types  

import json
import difflib
from difflib import get_close_matches

"""
Security+ Study Dictionary
@apiratemoo https://www.piratemoo.com
Sections are divided by chapter materials 
"""

print("Welcome to the Security+ Study Dictionary")
print("https://www.piratemoo.com\n")
print("Directions: Provide a word/term used in your Sec+ modules and receive a definition\n")

data = json.load(open("spdict.json"))

# Checks the value of the input received to see if it's within the dictionary
def translate(word):
    # word = word.lower() Messing with lower/upper case inputs here
    word = word.upper()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter y for yes, n for no: " % get_close_matches(word, data.keys())[0])
        if yn == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "n":
            return "This word isn't in the Sec+ dictionary. Please double check it."
        else:
            return "The program didn't understand the entry."
    else:
        return "This word isn't in the Sec+ dictionary. Please double check it."

# Variables for user input and translation
word = input("Please provide a term: ")
output = translate(word)

# Prints the output of the spdictionary without keeping list features
if type(output) == list:
    for item in output:
        print(item)
      
# print(translate(word))


