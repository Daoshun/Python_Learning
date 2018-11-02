a_tuple = (1,2,3,9,8,7)   #tuple 数组，一旦初始化就不能更改
a_list = [1,2,3,9,8,7]    #list有序集合，可以随时添加和删除元素
for i in a_tuple:
    print(i)
for j in a_list:
    print(j)

for m in range(len(a_tuple)):
    print('m=',m,'number in tuple=',a_tuple[m])

for n in range(len(a_list)):
    print('n=',n,'number in list=',a_list[n])
