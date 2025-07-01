file = open("geeks.txt", "w")
content = file.write("I am Arshdeep Singh")
print(content)
file.close()
file = open("geeks.txt", "r")
content = file.read()
print(content)
file.close()

with open("newfile.text","w+") as file:
    writing = file.write("Hey!!")
    file.close()

file = open("newfile.text", "r+")
content = file.read()
print(content)
file.close()
    
