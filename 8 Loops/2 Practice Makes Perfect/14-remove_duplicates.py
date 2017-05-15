def remove_duplicates(list):
    
    newlist = []
    
    for i in list:
        if i not in newlist:
            newlist.append(i)
            
    return newlist