a = float(input("Enter the side a: "))
b = float(input("Enter the side b: "))
c = float(input("Enter the side c: "))
while a == 'q':
    break
while b == 'q':
    break
while c =='q':
    break
if a > 0 and b > 0 and c > 0:
    
    if (a + b) > c and (a + c) > b and (c + b) > a:
        print("This triangle exists")
    else:
        print("This triangle doesn't exist")
else:
        print("The side length can not be negative or equal to 0!")