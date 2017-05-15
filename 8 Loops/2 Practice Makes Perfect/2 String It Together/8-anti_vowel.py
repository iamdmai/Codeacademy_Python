def anti_vowel(text):
    
    list = []
    vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
    
    for char in text:
        if char not in vowels:
            list.append(char)
    return "".join(list)