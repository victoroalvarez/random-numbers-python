# modules import
from sys import argv    # import command line arguments
import string
import random

script, digits = argv
span = int(digits)      # convert digits from string to integer

"""
String generator function, takes two arguments, an integer named string_size,
which determines the generated srting length, and a string named number_characters
which includes all digits from 0 to 9 used to generate the string.
"""
def random_number_generator(string_size = 4, number_characters = string.digits):
	# returns alpha numeric string of particular string length determined by the string_size parameter
	return ''.join(random.SystemRandom().choice(number_characters) for _ in range(string_size))

"""
Calls random_string_generator function with the integer span as argument
for setting string length.
"""
if span < 1:
    print(random_number_generator(4))
else:
    print(random_number_generator(span))
