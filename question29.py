from math import sqrt
a = int(input("enter a : "))
b = int(input("enter b : "))
c = int(input("enter c : "))
r = b**2 - (4 * a * c)
if r > 0:
    q1 = -b + sqrt(r)/(2 * a)
    q2 = -b - sqrt(r)/(2 * a)
    print(f"It has 2 roots {q1} & {q2}")
    
elif r == 0:
    q = -b / 2 * a 
    print(f"it has 1 root {q}")
    
else:    
      print("it has no roots")
          
    