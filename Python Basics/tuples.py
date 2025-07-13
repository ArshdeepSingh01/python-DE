thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

thistuple = tuple(("Arshdeep","Singh"))

#Accessing tuples
print(thistuple[0])
print(thistuple[-1:])

if "Arshdeep" in thistuple:
    print("Arshdeep is the WINNER")

#Adding items
thistuple =list(thistuple)
thistuple.append("King")
thistuple = tuple(thistuple)
y = ("of",)
thistuple += y
thistuple = list(thistuple)
thistuple.insert(len(thistuple),"Chandigarh")
print(thistuple)
thistuple = tuple(thistuple)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry",)

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

#Looping is same
for x in fruits:
    print(x)

#Joining tuples
fruits = fruits * 2
print(fruits)

fruits = fruits + thistuple
print(thistuple)