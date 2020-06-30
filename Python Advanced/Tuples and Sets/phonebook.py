# Write a program that receives some info from the console about people and their phone numbers.
# You are free to choose the way the data is entered; each entry should have just one name and one number (both
# strings). If you receive a name that already exists in the phonebook, simply update its number.
# After filling this simple phonebook, upon receiving the command &quot;search&quot;, your program should be able to
# perform a search of a contact by name and print her details in format &quot;{name} -&gt; {number}&quot;. In case the contact
# isn&#39;t found, print &quot;Contact {name} does not exist.&quot; Examples:

phonebook = {}

command = input()

while command != 'search':
    tockens = command.split('-')
    name = tockens[0]
    phone = tockens[1]
    phonebook[name] = phone
    command = input()

command = input()
name = []
while command != 'stop':
    name = command
    if name in phonebook:
        print(f'{name} -> {phonebook[name]}')
    else:
        print(f'Contact {name} does not exist.')
    command = input()


# input

# Adam-+359888001122
# Ralf-666
# George-5559393
# Silvester-02/987665544
# search
# Silvester
# silvester
# Rolf
# Ralf
# stop


# Adam-0888080808
# search
# Mery
# Adam
# stop