# Traversing :
# name="python"
# size=len(name)
# for i in range(size):
#     print(name[i])

# Without range :


# var1="this is devops batch"
# for i in var1:
#     if i in "aeiou":
#         print(i)


# var1="this is devops batch"
# for i in var1:
#     if i in "aeiou":
#         print(i)
     

# name="Abhinay"
# rev=""
# for i in name:
#     rev=i+rev
#     print(rev)
    # ""=A+""
    # "A"=b+"A"
    # "bA"=h+"bA"
    # "hbA"=i+"hbA"
    # "ihbA"=n+"ihbA"
    # "nihbA"=a+"nihbA"
    # "anihbA"=y+"anihbA"
    # "yanihbA"
# print(rev)

# name="python"
# size=len(name)
# for i in range(size):
#     print(name , name , i, i)

# name="python"
# size=len(name)
# for i in range(size):
#     print(name[i], name, i)

# wap to sum of the indices of a string : "pyhton"

# name="python"
# size=len(name)
# total=0
# for i in range(size):
#     if i in range(0,6):
#         total=total+i
#     print(i)
# print("total=", total)


# wap to print the factorial from 1 to 8:

# num=int(input("Enter the number:"))
# factorial=1
# for i in range(1,num+1):
#     factorial=factorial * i
#     print("factorial=",factorial)



# wap to print only prime number from 1 to 15:


# for num in range(1,15):
#     if num > 1:
#         for i in range(1,num):
#             if num %  i == 0:
#                 print(num,end=" ")


#  c=0
# a="this is python"
# for i in a:
#     if i==" ":
#         c+=1
# print(c)

# c=0
# str1="How are you"
# for i in str1:
#     if i=="o":
#        continue
#     else:
#         c+=1  
# print(c)    

# c=0
# address="D-1 267/268 Mayur-Vihar-phase-3 110096"
# number="01234556789"
# for i in address:
#     if i in number:
#         c+=1       
# print(c)

# c=0
# address="D-1 267/268 Mayur-Vihar-phase-3 110096"
# number="01234556789"
# for i in address:
#     if i not in number:
#         c+=1       
# print(c)

total=0
for i in range(1,6):
    total=total+i
    print("total=",total)