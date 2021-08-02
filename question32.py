a = int(input("enter side a: "))
b = int(input("enter side b: "))
c = int(input("enter side c: "))
all_equal = a == b and a == c and c == b
two_equal = (a == b or a == c) or (c == b or c == a)

if all_equal:
    print("it is equalateral traingle")
    
elif two_equal:
    print("it is isoceles traingle")
    
else:
    print("it is scalene traingle")