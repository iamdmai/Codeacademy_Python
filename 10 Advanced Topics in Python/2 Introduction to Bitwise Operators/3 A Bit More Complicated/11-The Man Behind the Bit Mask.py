def check_bit4(input):
    
    mask = 0b1000
    
    desired = input & mask
    
    if desired > 0: 
        return "on"
    
    if desired == 0:
        return "off"