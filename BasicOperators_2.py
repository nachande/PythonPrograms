a,b,c=input("Enter any 3 Values Seperated by a space (int,float)").split()

if(a>b and a>c):
    print (f"{a} is greater than {b},{c}")
elif(b>a and b>c):
    print (f"{b} is greater than {a},{c}")
else:
    print(f"{c} is greater than {a},{b}")
    
