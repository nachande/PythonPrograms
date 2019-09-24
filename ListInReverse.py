names=["Bhanu","Rekha","Chinna","Yethvan","Bhargavi"]

#n=len(names)

def reverse(data_list):
    length = len(data_list)
    s = length

    new_list = [None]*length

    for item in data_list:
        s = s - 1
        new_list[s] = item
    return new_list
rev_names=reverse(names)
print(rev_names)
#print(names[::-1])
    
