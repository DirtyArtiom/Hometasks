def str_len(str1):
    c = 0 
    for i in str1:
        c = c + 1 
    return c
str1= int(input("Enter a string:"))
print("The given String is:",str1)

print("Length =",str_len(str1))