morse_code_dict = {
    "a": r"*-",
    "b": r"-***",
    "c": r"-*-*",
    "d": r"-**",
    "e": r"*",
    "f": r"**-*",
    "g": r"--*",
    "h": r"****",
    "i": r"**",
    "j": r"*---",
    "k": r"-*-",
    "l": r"*-**",
    "m": r"--",
    "n": r"-*",
    "o": r"---",
    "p": r"*--*",
    "q": r"--*-",
    "r": r"*-*",
    "s": r"***",
    "t": r"-",
    "u": r"**-",
    "v": r"***-",
    "w": r"*--",
    "x": r"-**-",
    "y": r"-*--",
    "z": r"--**",

}
morse_code_phrase = []
user_phrase = input("What sentence would you like translated? ")

user_words = user_phrase.split(' ')
for word in user_words:
    for letter in word:
        morse_code_phrase.append(morse_code_dict.get(letter.lower()))
    morse_code_phrase.append('/')

morse_code_sentence = ''.join(morse_code_phrase)
#removes last trailing /
final_phrase = morse_code_sentence[:-1]

print(final_phrase)
