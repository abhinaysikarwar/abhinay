# What is function in python.
# Every function has their own purpose.
# Function is block of insturction (code) which execute inside its own block.
# Fuction is reusable means define one time use manytime (DRY)
# Function has two main part first functions defination second function calling.
# In python by default function re

# How define functionin python .
# 1. Take nothing return nothing .
# def add():
#     a=21
#     b=10
#     c=a+b
#     print(c)
# add()

# Function divide into 4 category.
# 1. Take nothing return nothing .
# 2. Take nothing return something.
# 3. Take something return nothing.
# 4. Take something retrun something

# parameters (para) and arguments(args).
# Positional parameter/arguments 
# Default paramerter

# def add(a,b,d):
#     c=a+b+d
#     print(c)
# add(20,40,30)

# def add(n,e)
#     c=n+e
#     print(c)
# add(29,45)

# # by default
# def add (a=0,b=0):   
#     print(a+b)
# add(11,22)


# def table_print(n):
#     for i in range(1,11):
#         print(f"{n} X {i}= {n*i}")
# table_print(5)

# def table_print(n):
#      for i in range(1,11):
#          print(f"{n} X {i}= {n*i}")
# m=2
# table_print(m)


# menu reven work 
# 3. Take something return nothing.

# def add(a=0,b=0):
#     print("Addition:",a+b)

# def sub(a=0,b=0):
#     print("Subtraction:",a-b)

# def mul(a=0,b=0):
#     print("multipcation:",a*b)

# def div(a=0,b=0):
#     print("Division:",a/b)

# num1=int(input("Enter the number 1 :"))
# num2=int(input("Enter the number 2 :"))
# opt=input("Choose option : +, -, *, / :")

# if opt=="+":
#     add(num1,num2)
# elif opt=="-":
#     sub(num1,num2)
# elif opt=="*":
#     mul(num1,num2)
# elif opt=="/":
#     div(num1,num2)
# else:
#     print("shi se input lo")


# def add(a,b):



# def greet(a):
#     return a 
# g=greet("Namaste")

# def user_name(a):
#     retrun a


# waf to check number pass by by argument is odd or even :

# def check_number(x):
#     if x % 2  ==0:
#         print("Even number")
#     else:
#         print("Odd number")
# check_number(5)

# # waf to check which is greater and two numver by user .

# def add(a,b):
#     if a>b :
#         print("Greater A")
#     else:
#         print("Greater B")
# add(35,65)
# add(45,35)


# a=int(input("enter the number :"))
# b=int(input("enter the number :"))
# def add(a,b):
#     if a>b :
#         print("Greater A")
#     else:
#         print("Greater B")
# add(a,b)


# waf to check the charecter pass by user is vowel or consonant.

# def check_character(x):
#     if x in ("aeiou"):
#         print ("vowel")
#     else:
#         print("constant")
# b="a"
# check_character(b)

# waf to check is number completly divide by 2 and 3 and return :

# "yes number is completely divided"
# "No number is not completely divide"

# def check_number(a):
#     if a % 2==0 and a % 3==0:
#         print("yes number is completely divide")
#     else:
#         print("No number is not completely divide")
# b=30
# check_number(b)


# def check_number(a):
#     if a % 2==0 and a % 3==0:
#         return "yes number is completely divide"
#     else:
#         return "No number is not completely divide"
# b=30
# res=check_number(b)
# print(res)


# waf to return length of a string pass by user without using len().

# def len_string(s):
#     c=0
#     for i in s:
#         c=c+1
#     return c
# res=len_string("python")
# print(res)



def len_string(s):
    print(s)
    c=0
    for i in s:
        print(i)
        c=c+1
    return c
res=len_string("python")
print(res)