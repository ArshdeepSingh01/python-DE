thislist = ["apple", "banana", "cherry"]
print(thislist)
print(len(thislist))
print(type(thislist))

thislist = list(("Arshdeep","Singh"))
print(thislist)

#Accessing Lists
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-3]) #3rd last item
print(thislist[1:3]) #Printing ranges
print(thislist[-4:]) 

#Checking if exists
if "banana" in thislist:
    print("Banana is good for health and is included in the list")

#Changing the values
thislist[1] = "New Banana"
print(thislist)
thislist[1:4] = ["New Banana 2","New Cherry","New Orange"]
print(thislist)
thislist.insert(-1,"grapes") #inserting items
print(thislist)

#Adding the items
thislist.append("pomegranate")
print("Pomegranate added!\n",thislist,"\n")

#Removing items
thislist.remove("pomegranate")
print("Pomegranate removed!\n",thislist)

thislist.pop(6)
print(thislist)

#looping
for x in thislist:
    print(x)

for i in range(len(thislist)):
  print(thislist[i],i)

i=0
print("---------while loop-------")
while i<len(thislist):
   print(thislist[i])
   i = i+1

print("--------List comprehension---------")
[print(x) for x in thislist]

print("----Sorted List------")
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)


def myfunc(n):
   return abs(n-50)

thislist.sort(key = myfunc)
print("----Sorted List based on Key------")
print(thislist)

#Copy list
mylist = thislist.copy()
print(mylist)

mylist = thislist[:]
print(mylist)

#Joining lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
list1.extend(list2)
for x in list2:
  list1.append(x)