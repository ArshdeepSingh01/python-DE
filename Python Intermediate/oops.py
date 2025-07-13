class Dog:
    species="Canine"

    def __init__(self,name,age):
        self.name= name
        self.age = age
    
    def bark(self):
            print(self.name, "is barking bhow bhow")
        
    

dog1 = Dog("shaffy",5)
print(dog1.species) #Class variable
print(dog1.name) #instance variable
dog1.bark() 

#Single inheritance
class Labrador(Dog):
     breed = "Labrador"
     def Sound(self):
          print("Labrador sounds woof woof!")

#multi level inheritance
class puppy_lab(Labrador):
     def Sound(self): #method overriding
          print("Puppy lab sounds pauu pauu")
shanty = Labrador("shanty",5)
shinzo = puppy_lab("shinzo",2)
print(shinzo.species)
print(shinzo.breed)
print(shinzo.Sound())
print(shinzo.name,shinzo.age)


class num1:
     def calculation(self,a,b=0,c=0):
          return a+b+c

n = num1() 
print(n.calculation(5,10))
print(n.calculation(5))