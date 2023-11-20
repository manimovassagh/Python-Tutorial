import os
# print(os.getcwd())
writer = open("mani.txt","a")
writer.write("hello world\n")
writer.close()
try:
    reader = open("mani2.txt","r")
    print(reader.read())
except FileNotFoundError:
    print("file not found")



# with open("mani.txt","r") as reader:
#     print(reader.read())




# reader = open("mani.txt","r")
# print(reader.read())
# reader.close()
