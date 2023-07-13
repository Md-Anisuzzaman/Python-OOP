from abc import ABC, abstractmethod
class Capsule(ABC):
    def __init__(self, name, age, gender):
        self.name = name
        self.__age = age
        self.gender = gender
    @abstractmethod
    def print(self):
        print(
            f'my name {self.name}, age is {self.__age} and gender {self.gender}')

class Tablet(Capsule):
    def helloMsg(self):
        print("I am called")

    def print(self):
        print("hey na na na, I am eating banana")

 

# hello = Capsule("Ethian", "55", "male")
# hello.name = "Rong"
# hello.print()

comp = Tablet("Rony",55,"male")
# comp._Capsule__age = 89
# print(comp._Capsule__age)
comp.print()

