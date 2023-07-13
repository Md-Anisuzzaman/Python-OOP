class Computer:

    def __init__(self,ram,cpu):
        self.ram = ram
        self.cpu = cpu

    def config(self):
        print(f'my computer {self.ram} ram and {self.cpu} brand')
    
    def compare(self, other):
        if self.cpu == other.cpu:
            return True
        else:
            return False

com1 = Computer("2 GHz","intel")
com1.cpu = "Ryzen"
com2 = Computer("2 GHz","intel")

if com1.compare(com2):
    print("Yes")
else: print("No")


com1.config()
com2.config()

