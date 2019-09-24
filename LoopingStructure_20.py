f0=0
f1=1

n=int(input("Enter range of fibonaci series "))
max_number=int(input("Enter what could be the maximum number in fibonaci series "))
print("::::Fibonaci Series:::::")

print(f0,f1, end=" ")
while(n-2>0):
    f2=f0+f1
    f0=f1
    f1=f2
    if f2 >= max_number:
        break
    print(f2,end=" ")
    n-=1

