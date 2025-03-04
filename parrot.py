class parrot:
    species="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printinfo(self):
        print("my name is",self.name)
        print("my age is",self.age)
    def sing(self,song):
        print("{} sings a {}".format(self.name,song))
    def dance(self):
        print("{} is now dancing".format(self.name))


blu=parrot("blue",1)
woo=parrot("woo",2)
blu.printinfo()
blu.sing("happy note")
blu.dance()
woo.printinfo()
woo.sing("happy note")
woo.dance()
