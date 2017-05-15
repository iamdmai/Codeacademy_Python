def count(sequence, item):
    
    count = 0
    
    for index in sequence:
        if index == item:
            count += 1
    
    return count