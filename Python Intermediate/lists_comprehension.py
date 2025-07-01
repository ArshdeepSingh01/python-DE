list = ['Arshdeep','Singh']
newList = [x for x in list]

print(newList)

a = (x for x in list if x!= 'ARSH')
print(type(a))