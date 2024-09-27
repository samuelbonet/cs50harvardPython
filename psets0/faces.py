import emoji

emoji_dict = {
    ":)": emoji.emojize(":slightly_smiling_face:"),
    ":(": emoji.emojize(":frowning_face:"),
    ":D": emoji.emojize(":grinning_face:"),
    ";)": emoji.emojize(":winking_face:"),
    ":P": emoji.emojize(":stuck_out_tongue:")
}

def convert(phrase):
    for face, emoj in emoji_dict.items():
        phrase = phrase.replace(face, emoj)
    return phrase

phrase = input("Introduce una frase, e.g Hello :) ")


newphrase = convert(phrase)

print(newphrase)
