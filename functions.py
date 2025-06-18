
# 1. Write a program using functions to find greatest of three numbers.
num1=int(input("give number: "))
num2=int(input("give number: "))
num3=int(input("give number: "))
def max(a,b,c):
    if (a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
maximum=max(num1,num2,num3)
print(f"the maximum number is {maximum}")

# 2. Write a python program using function to convert Celsius to Fahrenheit.
number=int(input("give number"))
def temp_conv(a):
    return (a * 9/5) + 32
fahrenheit=temp_conv(number)
print(fahrenheit)

# 4. Write a recursive function to calculate the sum of first n natural numbers.
n=3
def sum(n):
  if(n==1):
      return 1
  else:
     return n+sum(n-1)
summ= sum(n)
print(summ)
# 5. Write a python function to print first n lines of the following pattern:
# ***
# ** - for n = 3
# *
def star(n):
    for i in range(1,n+1):
        for j in range(n-i):
            print("*",end='')
        print()
star(3)
# 6. Write a python function which converts inches to cms
num=int(input("give number"))
def inch(a):
    return a*2.54
cms=inch(num)
print("the length in cms is ",cms)
# 7. Write a python function to remove a given word from a list ad strip it at the same
# time.

m=input("give name")
def func1(m):
    n = []
    for i in range(5):
        num=input("name fruits").strip()
        n.append(num)
    m=m.strip()
    if(m in n):

        n.remove(m)
        return n

    else:
         return "word not found"
func=func1(m)
print(func)

# 8. Write a python function to print multiplication table of a given number
def mult(n):
    for i in range(1,11):
        c= n*i
        print(c)
multiply=mult(5)
print(multiply)