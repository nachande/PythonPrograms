a,b,c,d=input("Enter 4 space seperated Numbers ").split()

if a>b and a>c and a>d:
    print(a," is bigger than",b,c,d,)
elif b>a and b>c and b>d:
    print(b," is bigger than",a,c,d)
elif c>a and c>b and c>d:
    print(c," is bigger than",a,b,d)
elif d>a and d>b and d>c:
    print(d," is bigger than",a,b,c)
elif a==b and b==c and c==d:
    print(a,b,c,d,"are equal")
elif a<b and b==c and c==d:
    print(b,"is bigger than",a)
elif b<a and a==c and a==d:
    print(a,"is bigger than",b)
elif c<b and b==a and b==d:
    print(b,"is bigger than",c)
elif d<c and c==a and c==b:
    print(c,"is bigger than",d)





