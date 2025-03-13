class computer:
    def __init__(self):
        self.__maxprice=1000
    def sell(self):
        print(f"selling price is {self.__maxprice}")
    def setmaxprice(self,price):
        self.__maxprice=price
c=computer()
c.sell()
c.__maxprice=900
c.sell()          
c.setmaxprice(900)
c.sell()  