import random


allowedcharacterstoreplace = []  # If empty, replace all characters, else only replace characters in this list
brainfuckcharacters = [".", ",", "[", "]", "+", "-", "<", ">"]
replacecharacter = "#"
insertgarbage = True  # Insert garbage at the end to make it not obvious where the actual code ends


def split(word):
    return [char for char in word]


with open("helloworld.bf", "r") as brainfuck:
    brainfuck = brainfuck.read()

with open("ascii_art.txt", "r") as ascii_art:
    ascii_art = ascii_art.read()

# Makes sure to remove comments from brainfuck code
brainfuckMinimized = ""
for i in split(brainfuck):
    if i in brainfuckcharacters:
        brainfuckMinimized += i

# Removes characters it can't replace for accurate length of free space
ascii_art_filtered = ""
for i in split(ascii_art):
    if i in allowedcharacterstoreplace or len(allowedcharacterstoreplace) == 0:
        ascii_art_filtered += i

# If the brainfuck code doesn't fit in the free space ascii art has, throw error
if len(brainfuckMinimized) > len(ascii_art_filtered):
    raise ValueError("The supplied brainfuck will not fit inside the ASCII art.")

output = ""
for i in split(ascii_art):
    if i in brainfuckcharacters:  # If this ascii art character might produce unwanted results in brainfuck code
        i = replacecharacter  # Replace it with character set at the top of script
    if brainfuckMinimized != "":
        if i != " " and i != "\n":  # If ascii art character is not space or enter
            if i in allowedcharacterstoreplace or len(allowedcharacterstoreplace) == 0:  # The character is replaceable
                i = brainfuckMinimized[0]  # Replace the character with the first character of brainfuck code
                brainfuckMinimized = brainfuckMinimized[1:]  # Remove the first character from the brainfuck code
    else:  # If there's no more brainfuck code left
        if insertgarbage:
            if i != " " and i != "\n":  # Same checks as above, only replace allowed characters
                if i in allowedcharacterstoreplace or len(allowedcharacterstoreplace) == 0:
                    i = random.choice([">", "+", "-"])  # Random bf command that doesn't cause syntax or logic error
    output += i

with open("hidden.bf", "w+") as hidden:
    hidden.write(output)
