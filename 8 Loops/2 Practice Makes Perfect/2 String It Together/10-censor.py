def censor(text, word):
    
    wordlength = len(word)
    replace = "*" * wordlength
    
    wordlist = text.split()
    
    for index, item in enumerate(wordlist):
        
        if item == word:
            wordlist[index] = replace
        
    return " ".join(wordlist)