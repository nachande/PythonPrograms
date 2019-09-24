print("Even Numbers In 1 to 100")

i=1
while(i<=100):
    i+=1
    if i%2!=0:
        continue
    if i==90:
        break
    if i==60 or i==70 or i==80 or i==90:
        continue
    print(i)
    
    
