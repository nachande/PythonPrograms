numbers=[2,6,5,9,4,5,10,13]

def smallest_number(numbers_list):
    smallest=numbers_list[0]
    for number in numbers_list:
        if number<smallest:        
            smallest=number
    return smallest

def biggest_number(numbers_list):
    biggest=numbers_list[0]
    for number in numbers_list:
        if number>biggest:        
            biggest=number
    return biggest

print (numbers)
print ("Smallest Number in a list is = ",smallest_number(numbers))
print ("Biggest Number in a list is = ",biggest_number(numbers))
