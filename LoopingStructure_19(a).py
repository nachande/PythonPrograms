print("Even Numbers In 1 to 100")
for i in range(1,101):
    if i%2!=0:
        continue
    if i==50:
        break
    if i==10 or i==20 or i==30 or i==40 or i==50:
        continue
    
    print(i)
    
