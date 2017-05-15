def median(list):
    
    output = 0
    
    new = sorted(list)
    
    if len(new) % 2 == 0:
        
        output = (new[(len(new)/2) -1] + new[(len(new)/2)])/2.0
    
    else:
        
        output = new[len(new)/2]
        
    return output