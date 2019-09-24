empid=[308567,308568,308569,308570,308571,308572,308573,308574,308575,308576]
empname=["Bhanu","Nitin","sushanta","DathRaj","Manoj","Mallik","santosh","Archana","Sunil","Sanath"]

print("Reading Index from the user and printing corresponding name from both the lists")
n=int(input("Enter index number you want to print from empid,empname lists "))

print(empid[n])
print(empname[n])

print("Printing names from 4th to 9th position")
print(empname[4:9])

print("printing names from 3rd position to till the end of the list")
print(empname[3:])

print("Repeating list elements by specified number of times")
r=int(input("Enter how many times you want list elements to be repeated ?"))

print(empname*r)

print("Concatinating two lists")
print(empid+empname)

print("Printing elements of two lists side by side")
print(empid[0],empname[0])
print(empid[1],empname[1])
print(empid[2],empname[2])
print(empid[3],empname[3])
print(empid[4],empname[4])
print(empid[5],empname[5])
print(empid[6],empname[6])
print(empid[7],empname[7])
print(empid[8],empname[8])
print(empid[9],empname[9])
