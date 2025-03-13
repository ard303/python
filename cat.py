class cat:
    def __init__(self,name,age):
        self.name=name 
        self.age=age
    def info(self):
        print(f"i am a cat my name is {self.name}, my age is {self.age}")
    def sound(self):
        print("meow") 


class dog:
    def __init__(self,name,age):
        self.name=name 
        self.age=age
    def info(self):
        print(f"i am a dog my name is {self.name}, my age is {self.age}")
    def sound(self):
        print("bark")        


cat1=cat("muffin",2.3)
dog1=dog("tom",2)

for i in (cat1,dog1):
    i.info()
    i.sound()