shift_right = 0b1100
shift_left = 0b1

# Your code here!
shift_right = 0b0011
shift_left = 0b0100
#shift_right = 0b1100 >> 2 == 0b0011 (12 >> 2 = 3)
#shift_left = 0b1 << 2 == 0b000100 (1 << 2 == 4)

print bin(shift_right)
print bin(shift_left)