a=int(input("Enter value of a"))
b=int(input("Enter value of b"))


print("Binary Representation of ",a,b,"is ")
print(bin(a))
print(bin(b))

print("BitWise 'AND' of ",a,b,"is =",a&b)
print("BitWise 'OR' of ",a,b,"is =",a|b)
print("BitWise 'NOT' of ",a,"is =",~a)
print("BitWise 'XOR' of ",a,b,"is =",a^b)
print("BitWise Left Shift '<<' of ",a,"by 2 bits is =",a<<2)
print("BitWise Right Shift '>>' of ",a,"by 2 bits is =",a>>2)
