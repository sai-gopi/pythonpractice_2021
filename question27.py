a = int(input("enter a: "))

b = int(input("enter b: "))

c = int(input("enter c: "))

is_greather_than = (a > b) and (a > c)

if is_greather_than :
    
    print("a is greater")
    
else:
    if b>c :
        print("b is greater")
        
    else:
        print("c is greater")
