# age = int(input("Enter your age:"))
# if age >=18:
#     print("You can vote")
# else:
#     print("You cannot vote")

# num1 = int(input("Enter number one:"))
# num2 = int(input("Enter number two:"))

# if num1 > num2:
#     print(f"{num1} is greater than {num2}")
# elif num1<num2:
#     print(f"{num2} is greater than {num1}")
# else:
#     print("Both are equal")

# for i in range(1,10):
#     print(i)

# name = "i am prabin thapa"
# for i in name:
#     print(i)

# length = int(input("Enter the length:"))
# breadth = int(input("Enter the breadth:"))
# perimeter = 2*(length*breadth)
# print(f"The perimeter is {perimeter}")


# print(2*3)
# print(2**3)

# string = "hello my name is prabin thapa"
# count = 1
# for i in string:
#     if i == " ":
#         count+=1

# print(count)
# s1 = 4
# s2 = 5
# s3 = 5
# semiperimeter = (s1+s2+s3)/2
# area = (semiperimeter*(semiperimeter-s1)(semiperimeter-s2)(semiperimeter-s3))**(1/2)
# print(f" Area is {area}")
# n = 5
# d = 0
# try:
#  div = n/d
#  print(div)
# except ArithmeticError:
#  print("Number cannot ne divided by zero")

# finally:
#  print(9/5) 


# list

# list = [1,'a',"prabin",4+5]
# print(list)
# print(type(list))
# list.append("hello")
# print(list)
# for l in list:
#     print(l)

# list =[]
# for i in range(1,10):
#     if i % 2 == 0:
#         list.append(i)
# print(list)

# l1 = list+ ["lict","hello","tu"]
# print(l1)


# break
# num = 0
# for i in range(10):
#     num+=1
#     if(num ==8):
#         break
#     print("The num has value",num)
# print("out of loop")

# match case
# day = int(input("Enter the day:"))
# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")
#     case _:
#         print("Invalid day")
    

# for i in range(1,50):
#     if (i % 2) != 0:
#         continue
#     print(i)

# t = (1,'c',"lumbini",9+7)
# print(t)
# print(type(t))
# l = list(t)
# print(l)
# print(type(l))

# list = [1,2,3,4,5,6]
# sum = 0
# for i in list:
#     sum +=i
# print(sum)


# list = ["prabin","sa","rabin","ab","ashok","abin"]
# l=[]

# for word in list:
#     if  len(word)>3 and word[0] == "a":
#         l.append(word)
# l.sort()
# print(l)


# list = ["prabin","sasin","ashok","abin,","haab"]
# l = []
# for word in list:
#     if len(word)<5 and word[-1]=="b":
#         l.append(word)
# l.sort()
# l.reverse()
# print(l)

# prymaid
# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end="")
#     print("\r")

# num = int(input("Enter number:"))
# # multiply
# for i in range(1,11):
#     print(f"{num} * {i} = {num*i}")

# triangle
# n = 5
# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print(" ",end="")
#     for k in range(1,2*i):
#         print("*",end="")
#     print()


# Dictonary
# d = {
#     "name":"prabin",
#     "age":21,
#     "address":"gaindakot",
#     "university":"Tu"
# }

# print(d)
# import random
# number = random.randint(1,50)
# print(random.random())
# print(number)

# number guessing game
import random
attempt = 0
randomnumber = random.randint(1,4)

while True:
    print("Number guessing game from 1-4 & (And enter 'a' to exit)")
    try:
     number = input("Guess a number:")
    except:
       print("Please enter a valid number")
    attempt+=1
    if number == 'a':
       print("Exiting the program")
       break
    if int(number) == randomnumber:
        print(f"you guess number in {attempt} attempt")
        break
    elif int(number) > randomnumber:
       print("Your guess is high")
    else:
       print("Your is too low")



