num_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],

 ]

for item in num_list:
    for col in item:
        print(col)


def translate(phrase):
    translation = ""
    vowel = "aeiou"
    for letter in phrase:
        if letter in vowel:
            translation += "g"
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter your word here: ").lower()))
