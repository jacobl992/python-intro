import math
#simple variable definitions
exercise_title = 'Basic Intro to Variables'
desired_age = 25
real_age = 31
name = 'Jake'

print(name + " wants to be " + str(desired_age) + " years old.")

#simple if statement
if desired_age < real_age:
    print(name + " is " + str(real_age) + ". He wishes he was younger so he could learn Python earlier.")
elif desired_age > real_age:
    print(name + " is " + str(real_age) + ". He wishes he was older. He wants those cheaper cinema tickets.")
else:
    print(name + " is " + str(real_age) + ". He is exactly the age he wants to be. Go him!")

#index a string
print('What is the second letter in the name?')
print(name[1])
print('What is the last letter in the name?')
print(name[-1])
print('What are the middle two letters in the name?')
print(name[1:3])

#formatted string
msg = f'{name} [{real_age}] wants to be {desired_age}.'
print(msg)

#string methods
print(len(exercise_title))
print(exercise_title.upper())
print(exercise_title.lower())
print(exercise_title.title())
print(exercise_title.find('V'))
print(exercise_title.replace('Variables', 'Variables for Beginners'))
print('Variables' in exercise_title)

#maths methods
x = 2.9
print(round(x))
print(abs(-x))
print(math.ceil(x))
print(math.floor(x))
    #check math documentation for more methods

#tuples
    #immutable variables, cannot be modified, assign using parentheses '()'
tuple_numbers = (1, 2, 3)

#unpacking
    #simplifying assigning variables
coordinates = (1, 2, 3)
x, y, z = coordinates
    #unpacking allows simplified assignment of variables x, y and z to coordinates[0], coordinates[1], coordinates[2]
print(x)
    #coordinates currently set as tuple, but could also be a list!!

#Dictionaries
    #storing key-value pairs
customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
    #each key must be unique
print(customer["name"])
customer["name"] = "David Blurg"
    #change data stored in dictionary

#challenge - convert number digits to words
number_spelling = {
    0: "Zero",
    1: "One",
    2: 'Two',
    3: 'Three',
    4: 'Four',
    5: 'Five',
    6: 'Six',
    7: 'Seven',
    8: 'Eight',
    9: 'Nine'
}

phone_number = "07342859142"
output = ""
output2 = ""

for digit in phone_number:
    output += number_spelling[int(digit)] + " "
    output2 += number_spelling.get(int(digit), "not found") + " "
    #can either use the .get method which allows a default case for it digit not found in dictionary
print(output)
print(output2)

#challenge emoji converter

message = input(">")
words = message.split(' ')
emojis = {
    ":)": "😀",
    ":(": "🙁"
}

output = ""
for word in words:
    output += emojis.get(word, word) + " "
    #this is saying look up word in emojis library, if not there, just use the word
print(output)