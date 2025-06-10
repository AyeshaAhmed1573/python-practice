# 1. Write a python program to display a user entered name followed by Good Afternoon using input () function.

name=input("enter your name: ")
print(f"Good Morning {name}")
# 2. Write a program to fill in a letter template given below with name and date.
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>'''
name1=input("enter your name: ")
date=input("enter your date: ")
print(letter.replace("<|Name|>",name1).replace("<|Date|>",date))

# 3. Write a program to detect double space in a string.
string= "ny name is  ayesha"
a=string.find("  ")
print(a)
# 4. Replace the double space from problem 3 with single spaces.
print(string.replace("  ","   "))

# 5. Write a program to format the following letter using escape sequence
# characters.
letter1 = "Dear \"Harry\",\nthis python course is nice.\nThanks!"
print(letter1)
