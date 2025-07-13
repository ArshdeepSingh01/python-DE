class test1:
    def __init__(self,name,breed, age):
        self.name = name
        self._breed = breed
        self.__age = age

        def get_info(self):
            print(self.name," is a ",self._breed," dog and his/her age is ",self.__age," years old")

        def get_age(self):
            return self.__age
        def set_age(self,age):
            if age>0:
                self.__age = age
            else:
                print("Invalid age")
        

