class Iphone():
    def __init__(self,name,price,hight,width,weight):
        self.name = name
        self.price = price
        self.hight = hight
        self.weigtht = weight
    def add(self,x,y):
        print(self.name,'sum=',x+y)
    def minus(self,x,y):
        print(self.name,'difference=',x-y)
