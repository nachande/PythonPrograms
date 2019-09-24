string="aabbccddaazzbbccaaaaaabbbbbbbbbbbbbbbb"

n=len(string)
dictionary={}
for i in range(n):
    count=0
    for j in range(n):
        if(string[i]==string[j]):
            count+=1
        dictionary.update({string[i]:count})
print("Dictionary with character and its count of a given String")
print(dictionary)

highvalue=max(list(dictionary.values()))

def findkey(highval):
    for key,value in dictionary.items():
        if(value==highval):
            return key
key=findkey(highvalue)
print("Longest Repeated character in \""+string+ "\" is %s:%d"%(key,highvalue))



        
    

