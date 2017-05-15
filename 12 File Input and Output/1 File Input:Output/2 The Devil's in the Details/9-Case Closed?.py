with open("text.txt", "w") as my_file:
    my_file.write("This will print")
    
if my_file.closed != True:
    my.file.close()

print my_file.closed