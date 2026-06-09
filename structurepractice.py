#  for list practice :

# nums =[1,2,3,4,5]
# print(nums)

# nums=[1,2,3,4,5]
# i=3
# print(nums[i])

# fruits=["Apple","Orange","Banana","Mango"]
# print(fruits)


# fruits=["Apple","Orange","Banana","Mango"]
# print("Before update :", fruits)
# fruits[-2]
# print("After update :", fruits[-2])

# fruits=["Apple","Orange","Banana","Mango"]
# fruits.remove("Orange")     # remove this in list hata deta hai
# print(fruits)


# fruits=["Apple","Orange","Banana","Mango"]
# fruits.append("Orange")       # append add one new in list
# print(fruits)


# items=[1,2,3,4,5]
# print(len(items))


# list ke saare elements for loop se print karo.

# colors=["Red", "blue", "Green"]
# for i in colors :
#     print(i)

# list ka total sum nikalo.

# nums=[2,5,8,5,25]
# total=0
# for i in nums:     # "+="  this is total of sum 
#     total+=i
# print("Total=",total)

# list me sabse bada number print karo :

# nums=[34,23,43,12,23]
# largest=nums[0]
# for i in nums:
#     if i > largest:
#         largest = i
# print(largest)
    

# nums=[2,6,9,15,60]
# largest=nums[0]
# for i in nums:
#     if i > largest:
#         largest = i
# print(largest)

# nums=[56,78,100,54,67]
# largest=nums[0]
# for i in nums:
#     if  i > largest :
#         largest = i
# print(largest)

# List me sirf even numbers print karo :

# nums=[23,56,34,78,10]
# smallest=nums[0]
# for i in nums:
#     if i < smallest:
#         smallest = i
# print(smallest)

# nums=[56,78,23,43,34]
# smallest=nums[0]
# for i in nums:
#     if i < smallest :
#         smallest = i
# print(smallest)

# list me sirf enen numbers print karo :

# nums=[1,2,3,4,5,6,7,8,9]
# for i in nums:
#     if i % 2 == 0:
#         print(i,end=" ")

# nums=[1,2,3,4,5,6,7,8,9]
# for i in nums:
#     if i % 2 != 0:
#         print(i,end=" ")


# diffrent type of list questions :
# Nested list :

# data=[[1,2],[3,4],[5,6]]
# for i in data :
#     for j in i :    # this is wrong code 
#         print(j)


# wap to swap the first value of lisit with last value of list.

# my_list=[10,11,20,31,30,33,40,44,50,55,60,70,80]

# first_elm=my_list[0]
# last_elm=my_list[-1]

# my_list[0]=last_elm
# my_list[-1]=first_elm
# print(my_list)

# wap to find the sum of the all elments in the list:[10,20,30,40]

# wap to find the sum of only even elments in the list ;[10,3,4,6,22,,31,33,,55,40]

# # wap to find the sum of only odd elments in the list ;[10,3,4,6,22,,31,33,,55,40]

# wap to find the count of how many int value and how many str in the list
# : [70,"aman",50,10,20,"rohan","iq-india"]

# 1. Question :
# element=[10,20,30,40]
# total=0
# num=1
# for i in element:
#     total=total+i
# print(total)

# 2. Question :

# even_sum=[10,3,4,6,22,31,33,55,40]
# total=0
# for i in even_sum:
#     if i % 2==0:
#         total=total+i
# print(total)

# 3. Question :

# odd_sum=[10,3,4,6,22,31,33,55,40]
# total=0
# for i in odd_sum:
#     if i % 2!=0:
#         total=total+i
# print(total)


# 4. Question :

# int_str=[70,"aman",50,10,20,"rohan","iq-india"]
# int_count=0
# str_count=0
# for i in int_str:
#     if type (i)==int:
#         int_count=int_count+1
#     elif type (i)==str:
#         str_count=str_count+1
# print(f"total int count=",int_count)
# print(f"toatl str count=",str_count)