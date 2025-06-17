thisdict = {
    "brand": "Toyota",
    "model": "Hilux",
    "year": 2025
}

print(thisdict['year'])

newdict = dict(name="Arshdeep",caste="Singh")
print(newdict)

print(newdict.items())
print(newdict.keys())
print(newdict.values())

#updating or changing the values
newdict['name']="Arshhdeep"
print(newdict)
newdict.update({'name':"Arshdeep"})
print(newdict)

#adding values
newdict['Age']=24
print(newdict)

#dropping values
newdict.pop('Age')
print(newdict)

newdict.popitem()
print(newdict)

newdict.clear()
del newdict

newdict = thisdict.copy()
print(newdict)

