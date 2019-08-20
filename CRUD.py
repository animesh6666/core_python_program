#f = open("My New File.txt","x")

# if f:
    # print("File is successfully creat.")

import os

f = open("My New File.txt","a+")
if f:
    print("File is succesfully open.")

#print(f.read())
f.write("this is python.\n")
f.writelines("hello.\n My file is made in python \n")

#print(f.read())


os.remove("My New File.txt")
