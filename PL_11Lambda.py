#lambda可以定义一个简单的函数，实现简化代码的功能
fun = lambda x,y:x+y
x = int(input('x='))
y = int(input('y='))
print(fun(x,y))
#map是把函数和参数绑定在一起,可以实现多个参数同时进行运算
fun1 = lambda x,y:x*y
a = list(map(fun1,[1,2],[2,3]))
print(a)
