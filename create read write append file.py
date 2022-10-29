#read a file
file1 = open("newtext.txt",mode='r')
content = file1.read()
print(content)
file1.close()

#create a file

file2 = open("newtext2.txt",mode='a') #mode can be append or write (for creating )
cont = file2.write("hello world")
file2.close()

#over wirte a file

file3 = open("mewtext3.txt", mode='w')
cont2 = file3.write("Hello I am jeeban\n")
file3.close()

#append a file
file4 = open("newtext4.txt",mode='a')
cont3 = file4.write("Hello Sir...\n")
file4.close()

#auto close a opne file
with open("newtext4.txt", mode='r') as new_file:
    c = new_file.read()
    print(c)

#Absolute path

file3 = open("C:\\Users\\Jeeban\\Desktop\\multisoft exercise\\newtext3.txt", mode='a')
cont2 = file3.write("Hello I am jeeban .. How are you ?\n")
file3.close()



#relative path
'''
The given path for opening newtext.txt file is knows as relative path
'''
file3 = open("newtext3.txt", mode='w')
cont2 = file3.write("Hello I am jeeban\n")
file3.close()


