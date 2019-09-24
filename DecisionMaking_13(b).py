a,b,c,d,e=input("Enter 5 space seperated Numbers ").split()

if a>b and a>c and a>d and a>e:
    print(a," is bigger than",b,c,d,e)
elif b>a and b>c and b>d and b>e:
    print(b," is bigger than",a,c,d,e)
elif c>a and c>b and c>d and c>e:
    print(c," is bigger than",a,b,d,e)
elif d>a and d>b and d>c and d>e:
    print(d," is bigger than",a,b,c,e)
elif e>a and e>b and e>c and e>d:
    print(e," is bigger than",a,b,c,d)
elif a==b and b==c and c==d and d==e:
    print(a,b,c,d,e,"are equal")
elif a<b and b==c and c==d and d==e:
    print(b,"is bigger than",a)
elif b<a and a==c and c==d and d==e:
    print(a,"is bigger than",b)
elif c<b and b==a and a==d and d==e:
    print(b,"is bigger than",c)
elif d<c and c==a and a==b and b==e:
    print(c,"is bigger than",d)
elif e<d and d==c and c==b and b==a:
    print(d,"is bigger than",e)






