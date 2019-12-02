class Animal:
    # PRIVATE VARIABLES
    __height = 0   # "__" indicates a private variable
    __weight = 0
    __name = None   # could also use __name = ""

    # CONSTRUCTORS
    def __init__(self, name, height, weight):
        self.__name = name
        self.__height = height
        self.__weight = weight

    # SETTER-GETTERS
    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setHeight(self, height):
        self.__height= height

    def getHeight(self):
        return self.__height

    def setWeight(self, weight):
        self.__weight= weight

    def getWeight(self):
        return self.__weight

    def getType(self):
        print("Animal")

    def toString(self):
        return "{} is {} inches tall and {} pounds".format(self.__name, self.__height, self.__weight)

dog = Animal("Wolfee", 12, 23)
print(dog.toString())


#INHERITANCE
class Cat(Animal):
    __fur = None

    def __init__(self, name, height, weight, fur):
        self.__fur = ""
        super( Cat, self).__init__(name, height, weight)

    def toString(self):
        return "{} is {} inches tall and {} pounds and is {}".format( self.getName(), self.getHeight(), self.getWeight(), self.__fur)
        #return "{} is {} inches tall and {} pounds and is {}".format( self.__name(), self.__height(),
        #                                                             self.__weight(), self.__fur)

cat = Cat("Meowee", 13, 24, "short haired")
print(cat.toString())