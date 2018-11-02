''文件读写''
text = '123456\nThis is appended line.\n'
file = open('my_file.txt','w')  #write
file.write(text)
file.close()

file = open('my_file.txt','a')  #append在原有的基础上增加content
file.write(text)
file.close()

file = open('my_file.txt','r')
content = file.read()           #read
print(content)
file.close()

file = open('my_file.txt','r')
content = file.readline()       #一行一行的读，先读第一行，在执行一次读第二行
print(content)
file.close()

file = open('my_file.txt','r')
content = file.readlines()      #全部读完，用python_list的形式
print(content)
file.close()

file = open('my_file.txt','r')
content = file.readlines()
for i in content:
    print(i)                    #遍历list
file.close()
#执行完后，定关闭file file.close()
