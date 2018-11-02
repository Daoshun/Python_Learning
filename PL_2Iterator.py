#define a Fib class 迭代器
class Fib(object):
    def __init__(self,max):
        self.max = max
        self.n,self.a,self.b = 0,0,1
    def __iter__(self):
        return self
    def __next__(self):
        if self.n < self.max:
            r = self.b
            self.a,self.b = self.b,self.a+self.b
            self.n = self.n + 1
            return r
        raise StopIteration()

#Using  Fib object
for i in Fib(45):
    print(i)
#print Fiboncci 数列 第n项等于前两项之和n>=3  1,1,2,3,5,8...
