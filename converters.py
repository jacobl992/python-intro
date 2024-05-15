def emoji_conversion(message, emojis):
    words = message.split(' ')


    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output