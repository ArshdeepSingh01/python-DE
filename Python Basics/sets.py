thisisset = {"Arshdeep","Singh",24}
print(thisisset)
newset = {"apple", "banana", "cherry", True, 1, 2}
print(newset)
print(len(newset))

#Set using constructor
newset1 = set(("ARSH","DEEP","SINGH"))
print(newset1)

#Accessing set
for x in thisisset:
    print(x)

print("Arshdeep" in thisisset) #Returns true or false

#Adding items
thisisset.add("Orange")
print(thisisset)

thisisset.update(newset1)
print(thisisset)

#Removing items
thisisset.pop()
print(thisisset)

thisisset.discard("Orange") #Does not throw error if item is not there
print(thisisset)

thisisset.remove(24)
print(thisisset)

#Joining sets

set1 = {"a", "b", "c",2}
set2 = {1, 2, 3}

#UNION
set3 = set1.union(set2)
print(set3)

del set3
set3 = set1 | set2
print(set3)

#INTERSECT
del set3
set3 = set1.intersection(set2)
print(set3)

del set3
set3  = set1 & set2
print(set3)

#DIFFERENCE
del set3
set3 = set1.difference(set2)
print(set3)

set1.difference_update(set2)
print(set1)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)