#basic function
def greet_user(name):
    print(f'Hi there, {name}!')
    print("Welcome aboard")


print("Start")
greet_user("Gimli")
greet_user("Aragorn")
print("Finish")

#can also use keyword arguments if parameters need clarigifying eg greet_user(name="Gimli)
#not needed in this case but maybe if function used multiple numerical values would could use keyword argument for clarity
#keyword argument should always be written AFTER positional arguments

#return statements
def square(number):
    return number * number


#return statment very valuable when functions are very long
result = square(3)
print(result)

#remaking emoji conversion as function

message = input(">")
emojis = {
    ":)": "😀",
    ":(": "🙁"
}
def emoji_conversion(message, emojis):
    words = message.split(' ')


    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


print(emoji_conversion(message,emojis))
