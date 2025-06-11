# 1. Write a program to store seven fruits in a list entered by the user.
fruits=[]
for i in range(7):
    fruit= input("enter fruit number : ")
    fruits.append(fruit)
print(fruits)

# 2. Write a program to accept marks of 6 students and display them in a sorted manner.
marks=[]
for i in range(6):
    mark=input("enter mark : ")
    marks.append(mark)
marks.sort()
print(marks)

# 3.Write a program to sum a list with 4 numbers.
numbers=[]
total=0
for i in range(4):
   number=int(input("enter number : "))
   numbers.append(number)
   total=total+number
# total=sum(numbers) with function
print(total)

# 5. Write a program to count the number of zeros in the following tuple:
a = (7, 0, 8, 0, 0, 9)
print(a.count(0))

