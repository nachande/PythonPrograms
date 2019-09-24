n= int(input("Enter a number (for upper limit of prime numbers range)"))

prime_list=[]
for number in range(1,n+1):
    counter=0
    for i in range(1,number+1): 
        if number%i==0:
            counter+=1
    if  counter ==2:
        prime_list.append(number)

print(prime_list)
        
