# 01.) Write a Program to match a string that contains only upper and lowercase letters, numbers, and underscores.

import re

def is_valid_string(input_string) :
    pattern = r'^[a-zA-Z0-9_]+$'

    if re.match(pattern, input_string) :
        return True
    else :
        return False
    
input_string = input("Enter a string to validate : ")
if is_valid_string(input_string) :
    print("Valid String!")
else :
    print("Invalid String. String should only contain letters, numbers and underscores.")


print()






# 02.) Write a Program that matches a string that has an a followed by zero or more b's

import re

def match_pattern(input_string) :
    pattern = r'^ab*$'

    if re.match(pattern, input_string) :
        return True
    else :
        return False
    
input_string = input("Enter a string to match a followed by zero or more b's : ")
if match_pattern(input_string) :
    print("The string matches the pattern!")
else :
    print("The string doesn't match the pattern.")


print()







# 3. Write a Program that matches a string that has an a followed by one or more b's

import re

def match_pattern(input_string) :
    pattern = r'^ab+$'

    if re.match(pattern, input_string) :
        return True
    else :
        return False
    
input_string = input("Enter a string to match a followed by one or more b's : ")
if match_pattern(input_string) :
    print("The string matches the pattern!")
else :
    print("The string doesn't match the pattern.")


print()






# 4. Write a Program that matches a string that has an a followed by three 'b'

import re

def match_pattern(input_string) :
    pattern = r'^ab{3}$'

    if re.match(pattern, input_string) :
        return True
    else :
        return False
    
input_string = input("Enter a string to match a followed by three b's : ")
if match_pattern(input_string) :
    print("The string matches the pattern!")
else :
    print("The string doesn't match the pattern.")


print()







# 5. Write a Program to find the sequences of one upper case letter followed by lower case letters

import re 

def find_sequences(input_string) :
    pattern = r'[A-Z][a-z]+'
    sequences = re.findall(pattern, input_string)
    return sequences

input_string = input("Enter a string to find sequences of one uppercase letter followed by lowercase letters: ")

result = find_sequences(input_string)

if result :
    print("Sequences found : ")
    for sequence in result :
        print(sequence)
else :
    print("No sequences found.")


print()







# 6. Write a Program that matches a word at the beginning of a string

import re

def match_at_beginning(word, input_string) :
    pattern = r'^' + re.escape(word)
    match = re.search(pattern, input_string)
    return match is not None

word = input("Enter a string to match a word at the beginning of the string : ")

input_string = input("Enter the string : ")

if match_at_beginning(word, input_string) :
    print(f"The word '{word}' matches at the beginning of the string.")
else :
    print(f"The word '{word}' does not match at the beginning of the string.")

print()







# 7. Write a Program to search some literals strings in a string.

import re 

def search_literals(literal_strings, input_string) :
    pattern = re.compile('|'.join(map(re.escape, literal_strings)))

    matches = pattern.findall(input_string)

    return matches


strings = input('Enter a list of literal values : ')
literal_strings = strings.split()

input_string = input("Enter a string to search for the literal strings : ")

found_matches = search_literals(literal_strings, input_string)

if found_matches :
    print("Found the following literal strings : ")
    for match in found_matches :
        print(match)
else :
    print("No matches found for the literal strings.")

print()






# 8. Write a Program to replace whitespaces with an underscore and vice versa.

import re

def replacing(text) :
    text_with_underscores = re.sub(r'\s', '_', text)

    text_with_spaces = re.sub(r'_', ' ', text)

    return text_with_underscores, text_with_spaces

input_text = input("Enter the text to replace it with either underscore or spaces : ")
underscored_text, spaced_text = replacing(input_text)

print("Text with underscore instead of spaces : ", underscored_text)
print("Text with spaces instead of underscores : ", spaced_text)

print()






# 9. Write a Program to remove all whitespaces from a string.

import re 

def remove_whitespaces(text) :
    text_without_spaces = re.sub(r'\s', '', text)

    return text_without_spaces

text = input("Enter text : ")

result = remove_whitespaces(text)
print(result)


print()







# 10. Write a Program to validate a 10-digit mobile number

import re 

def validate_mobile_number(mobile_number) :
    pattern = r'^[7-9]\d{9}$'

    if re.match(pattern, mobile_number) :
        return True
    else :
        return False
    
mobile_number = input("Enter the mobile number : ")

if validate_mobile_number(mobile_number) :
    print("Valid Mobile Number.")
else :
    print("Invald Mobile Number.")