# # # 1. Write a program to print multiplication table of a given number using for loop.
num=int(input("enter the number: "))
for i in range(1,11):
    multiply=num*i
    print(multiply)
# # 2. Write a program to greet all the person names stored in a list ‘l’ and which starts
# # with S.
l = ["Harry", "Soham", "Sachin", "Rahul"]
for i in l:
    if(i[0]=="S"):
        print(f"hello {i}")
# # 3. Attempt problem 1 using while loop
a=0
num=int(input("enter the number: "))
while(a<10):
    c=num*a
    print(c)
    a=a+1
# # 4. Write a program to find whether a given number is prime or not.
import math

prime=int(input("enter any number"))
for i in range(2,int(math.sqrt(prime))+1):
    if (prime % i !=0):
        print("its  prime number")
        break
    else:
        print("its not a prime number")
# # . Write a program to find the sum of first n natural numbers using while loop.
sum=0
b=0
number=int(input("give number"))
while(b<number+1):
    sum=sum+b
    b=b+1

print(sum)
#
# # 6. Write a program to calculate the factorial of a given number using for loop
#
#
mult=1
b=1
number=int(input("give number"))
while(b<number+1):
    mult=mult*b
    b=b+1
print(mult)

# 7. Write a program to print the following star pattern.
#  *
# ***
# *****


rows=4
for i in range(1,rows):
    for j in range(rows-i):
        print(" ",end="")
    for k in range(2* i-1):
        print("*",end="")
    print()
# Write a program to print the following star pattern:
# *
# **
# *** for n = 3
row=4
for i in range(1,row):
    for j in range (i):
        print("*",end='')

    print()

# 9. Write a program to print the following star pattern.
# * * *
# *  * for n = 3
# * * *
row =3
for i in range(1,row+1):

    if(i%2!=0):
        for j in range(row):
         print('*',end=' ')
        print()
    else:
        for j in range(row-1):
            print('*', end='   ')
        print()


