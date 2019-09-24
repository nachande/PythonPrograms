numbers=(1,2,3,4,5,6,7,8,9,10)
letters=('a','b','c','d')

print("Printing All the elements of a Tuple")
for i in numbers:
    print(i)

print("Slicing Operations")

print("printing Elements starting with 0 index till end of the tuple")
print(numbers[:])
print("printing elements starting with 1st index ending with 4th index")
print(numbers[1:5])
print("printing elements starting with 1st index ending with 4th index using step value as 2")
print(numbers[1:5:2])
print("printing elements starting with 0 index ending with 4th index")
print(numbers[:5])
print("printing elements starting with 0 index till end with step value as 3")
print(numbers[::3])

print("Repetition with * operator")

print(numbers*3)

print("Concatenation with other Tuple")
print(numbers+letters)
