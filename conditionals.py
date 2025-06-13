# # 1. Write a program to find the greatest of four numbers entered by the user
#
#
# # WITHOUT CONDITION
a=[]
for i in range(4):
    number= int(input("enter number : "))
    a.append(number)
a.sort()
print(a[3])
# # WITH CONDITION
number1= int(input("enter number : "))
number2= int(input("enter number : "))
number3= int(input("enter number : "))
number4= int(input("enter number : "))

if(number1>number2 and number1>number3 and number1>number4):
     print(f"{number1} is greater")
elif(number2>number3 and number2>number4 and number2>number1):
     print(f"{number2} is greater")
elif(number3>number2 and number3>number1 and number3>number4):
     print(f"{number3} is greater")
else:
    print(f"{number4} is greater")

# 2. Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.

a=300
b=100
total=0
for i in range(3):
    marks= int(input("enter marks : "))
    percentage2 = (marks / b) * 100
    if (percentage2 > 33):
        print(f"you passed this subject with {marks}")
    else:
        print(f"you failed this subject with {marks}")

    total = marks+total

percentage=(total/a)*100
if (percentage>40):
    print(f"you passed with {percentage}%")
else:
    print(f"you failed with {percentage}%")

# 3. A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams.

email = input("enter your email: ")
email= email.lower()
a=email.find("make a lot of money")
b=email.find( "buy now")
c=email.find ("subscribe this")
d=email.find( "click this")
print(a,b,c,d)
if(a==-1 and b==-1 and c==-1 and d==-1):
    print("email is not a spam")
else:
    print("email is spam")

            # OR

email = input("enter your email: ")
email= email.lower()
if("make a lot of money" in email or "buy now" in email or "subscribe this" in email or "click this" in email):
    print("email is  a spam")
else:
    print("email is not spam")

# 4. Write a program to find whether a given username contains less than 10
# characters or not.
name=input("enter your name: ")
a=len(name)
if(a<10):
    print("the username is less than 10 characters")
else:
    print("the username is not less than 10 characters")

# 5. Write a program which finds out whether a given name is present in a list or not.

a=['hafsa','ayesha','sara','sofia','khola']
c=input("give name")
if(c in a):
    print("the name is present")
else:
    print("the name is not present")