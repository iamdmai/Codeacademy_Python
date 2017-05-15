def purify(list):
    newlist = []
    
    for num in list:
        if num % 2 == 0:
            newlist.append(num)
    return newlist