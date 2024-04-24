import itertools
import string
import sys

# Define the characters to be used
characters = string.ascii_lowercase + string.ascii_uppercase + string.digits

# Define the length of combinations

length = int(input("Enter your value: ") )
print(length) 

# Generate combinations
combinations = itertools.product(characters, repeat=length)

# Define the file name
file_name = "combinations.txt"

# Open the file in write mode
with open(file_name, 'w') as file:
    # Write combinations to the file
    for combo in combinations:
        print(''.join(combo))
        file.write(''.join(combo) + '\n')

print(f"Combinations saved to {file_name}")