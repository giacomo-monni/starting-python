# Dictionaries

d=dict()

#Insert three elements in dictionary 
i=0
while i<3:
    key = input('Insert the key ')
    val = eval(input('Insert the value '))
    d[key]=val
    i=i+1

print('key/s:',d.keys())  #print all the keys
print('value/s:',d.values())

#Dictionary's ordering

k = list(d) #conversion to list
k.sort()
for element in k : print(element,d[element])
