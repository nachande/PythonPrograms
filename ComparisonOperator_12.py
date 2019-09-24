numbers=[]
num_lta=[]  # numbers lest than average
num_gta=[]  # numbers greater than average
num_eta=[]  # numbers equal to average 

n=int(input("How many numbers you need in list "))
sumOfElements=0

for i in range(n):
    number=int(input("Enter a number: ")) 
    numbers.append(number)
    
print("Your List is : ",numbers)

for j in numbers:
    sumOfElements+=j
print("Summation of All the Elements of a list ",sumOfElements)

average=sumOfElements/n
print("Average of Elements in List is:",average)

less=0
greater=0
equal=0
for i in numbers:
    if i<average:
        less+=1
        num_lta.append(i)
    elif i>average:
        greater+=1
        num_gta.append(i)
    elif i==average:
        equal+=1
        num_eta.append(i)

print("Numbers Less Than Average are",less,"They are ",num_lta)
print("Numbers Greater Than Average are ",greater,"They are ",num_gta)
print("Numbers Equal to Average are ",equal,"They are ",num_eta)
