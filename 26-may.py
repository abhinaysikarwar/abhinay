# Data structure.
# Data structres used to store data effeciently and make faster for operations like read and write.

# 1. List : list ()
# 2. string : str()
# 3. Dictionary : dict()
# 4. set : set()
# 5. tuple : tuple()

######### 1. List 
# 1. List is a data structure in python used to store multiple data of different types in one variable .

# 2. List ca  define by useing square [] and data inside known as element .

# 3. List can be hetrogenous and homogenuous .

# 4. List are mutable (changeable)

# 5. List support indexing , slicing and follows ordering sequence. 


# 1. Creation of list.
# 2. Updation of list.
# 3. Indexing 
# 4. Slicing 
# 5. Traversing 
# 6. In-built methods 
# 7. Test
# 8. Assignments

# marks_10th=[20,55,60,45,30]
# print("Before Update : ", marks_10th)
# marks_10th[0]=200   # mutating list element using index .
# print("After update : ",marks_10th)

# marks_10th=[20,55,60,45,30]
# print("Before Update : ", marks_10th)
# marks_10th[-1]=200
# print("After update : ",marks_10th)

# marks_10th=[20,55,60,45,30]
# print("Before Update : ", marks_10th)
# marks_10th[-2]=200
# print("After update : ",marks_10th)

# marks_10th=[20,55,60,45,30]
# print("Before Update : ", marks_10th)
# marks_10th[2]=200
# print("After update : ",marks_10th)


# marks_10th=[10,20,30,40]
# i=2-1
# print(marks_10th[3])


# slicing.

# marks=[10,20,30,40,50,60,70,80]
# #[start-0,stop-1,step-1]
# sub_list=marks[0:8:2]
# print(sub_list)



# marks=[10,20,30,40,50,60,70,80]
# #[start-0,stop-1,step-1]
# sub_list=marks[3:9:2]
# print(sub_list)


# marks=[10,20,30,40,50,60,70,80]
# #[start-0,stop-1,step-1]
# sub_list=marks[:3:-1]
# print(sub_list)



# 6. Traversing

# marks=[10,11,20,31,30,33,40,55,50,60,67]
# for i in range(len(marks)):
#     if marks[i]%2==0:
#         print(f"This elm is even : {marks[i]}")
#     else:
#         print(f"This elm is odd : {marks[i]}")

# marks=[10,11,20,31,30,33,40,55,50,60,67]
# for i in marks:
#     if i%2==0:
#         print(f"This elm is even : {i}")
#     else:
#         print(f"This elm is odd : {i}")


# marks=[10,11,20,31,30,33,40,55,50,60,67]
# total=0
# for i in marks:
#     total=total+i
# print(total)

# Wap to swap the first value of list with last value of list.
# my_list=[10,20,30,40]

# first_elm=my_list[0]
# last_elm=my_list[-1]

# my_list[-1]=first_elm
# my_list[0]=last_elm

# print(my_list)


# 1.Wap to find the sum of the all elments in the list : [10,20,30,40].
# 2.Wap to find the sum of only even elments in the list : [10,3,4,6,22,31,33,55,40].
# 3.Wap to find the sum of only odd elments in the list : [10,3,4,6,22,31,33,55,40].
# 4.Wap to find the count of how many int value and how many str in the list 
# : [70,"aman",50,10,20,"rohan","iq-india"].

