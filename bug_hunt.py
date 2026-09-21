count = 1
total = 0
# BUG: Missing a colon ':' at the end of the line, which caused a syntax error. 
# Also, using '< 5' stopped the loop early and left out the number 5. 
# Fixed by adding the colon and changing it to '<= 5' so it counts all the way to 5.
while count <= 5:
    total = total + count
    count = count + 1
# BUG: Trying to combine a text string with an integer variable directly crashes the program. 
# Fixed by wrapping the 'total' variable inside 'str()' to convert the number into text.
print("Sum of 1 to 5 is: " + str(total))
