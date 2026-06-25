#------------------ File handling
#File handling in pyhton means reading from and writing to files/folder stored 
#disk using python.

#Your python code can open a file , pull out data of it , put data into it and 
#also close it properly.

#------------- What is file
# files are srore of data and information on the specifi  path of device.

#Types of file
# 1. Text file (.txt,.csv,.json)
# 2. Binary file (images, videos, audio)

#Types of file path .
# 1. Absoulte path : The compete path from the root of the filesystem.
# 2. Relative path : The path realative to wherw your current folder (current woking dir)

# dile mode
# 1. a : append
# 2. w : write  , w+ = write and read
# 3. r : read   , r+ = read and write
# 4. x : strictly create file

# python file handling methods.
# 1. open (file_name,mode) : opens file
# 2. close() : close file
# 3. flush() : memory cleanup
# 4. read() : file read
# 5. readlines() : file read line by line
# 6. write() : writes data in file only take string
# 7. writelines() : write data in file of any data types.
# 8. tail() : cursor move 
# 9. seek() : specific position set of cursor 

# in-bulit modules
# os libary
# random libary
# shutil libary
# subprocess libary
# string libary



#---------------------------------------------------------------------------------
# create a file in strict mode
# try:
#     file=open("demo.txt","x")
#     print("File Created")
# except Exception as e :
#     print("Error:",e)


# 2. Write mode file creation
# file=open("new_demo.txt","w")
# file.write("This is file conten using file handling")
# print("file cteated in write mode..")

# import os 
# print(os.getcwd())
# path=r"C:\Users\abhinaysikarwar\OneDrive\Desktop\pythonfordevops"
# os.chdir(path)
# print(os.getcwd())

# context manager
# with open("demo.txt","r") as file:
#     r=file.read()
#     print(r)

# with open("demo.txt","r") as file:
#     file.write("this is new content of file")
#     file.write("this is updated content")
#     print("file")


# ectact all number from paragraph
para="""
Lorem Ipsum is simply dummy text of the
printing and typesetting industry.
Lorem Ipsum has been the industry's standard
dummy text ever since 1966, when designers 
at Letraset and James Mosley, the librarian at 
St Bride Printing Library in London, took a 1914 
Cicero translation and scrambled it to make dummy 
text for Letraset's Body Type sheets.
"""
# only_digit.txt

count_digits=0
total_char=0
for i in para:
    if i in "0123456789":
        count_digits+=1
    else:
        total_char+=1
with open('stats.txt', "w") as file:
    file.write(f"Total Digits in file : {count_digits}")
    file.write("\n")
    file.write(f"Total chars in file : {total_char}")