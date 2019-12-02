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

    def __str__(self):
        return "{} is {} inches tall and {} pounds".format(self.__name, self.__height, self.__weight)

dog = Animal("Wolfee", 12, 23)
print( dog )
print(help(dir(dog)))
