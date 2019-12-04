class Dog:
    breed = "Dog"

    # constructor
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # def __del_(self):
    #     pass

    # ToString style method
    def __str__(self):
        return f"name: {self.__name}, age: {self.__age}"

    # def __repr__(self):
    #     pass

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_breed(self):
        return self.breed

    def print_test(self):
        print("Dog Test")


class LabradorRetriever(Dog):
    def __init__(self, name, age):
        super(LabradorRetriever, self).__init__(name, age)

    # def get_breed(self):
    #     return "Lab"


cole = LabradorRetriever(name="Cole", age=6)

print(f"cole's name: {cole.get_name()}")

print(f"cole's breed: {cole.get_breed()}")


# cole = Dog(name="Cole", age=6)

# print(f"{id(cole)}, {cole.get_name()}, {cole.get_age()}")
# print(cole)
# print(cole.breed)

# athena = Dog(name="Athena", age=8)

# print(f"{id(athena)}, {athena.get_name()}, {athena.get_age()}")
# print(athena)
