def is_prime(x):
    if x < 2:
        return False
    
    if x == 2:
        return True
    
    if x == 3:
        return True
    
    else:
        for num in range(2, x-1):
            if x % num == 0:
                return False
        return True