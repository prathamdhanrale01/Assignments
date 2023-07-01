def remove_vowels(string):
    vowels = "aeiouAEIOU"
    without_vowels = ""
    for char in string:
        if char not in vowels:
            without_vowels += char
    return without_vowels
