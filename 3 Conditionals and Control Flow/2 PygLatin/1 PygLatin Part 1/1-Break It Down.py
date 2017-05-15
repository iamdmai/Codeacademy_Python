while True:
    try: 
        word = raw_input("Enter a word")

    except ValueError:
        print "Sorry I didn't understand that word"
        continue
    
    print word(1:len(word)) + word(0) + "ay"
    