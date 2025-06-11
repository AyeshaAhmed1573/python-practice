
# 1. Write a program to create a dictionary of urdu words with values as their English translation. Provide user with an option to look it up!
translation={
    "han":"yes",
    "nahi":"no",
    "mazedaar":"tasty",
    "ghari":"clock"
}
b= input("enter in roman urdu for english translation: ")
print(translation[b])
# 2. Write a program to input eight numbers from the user and display all the unique numbers (once).
set=set()
for i in range(8):
    number=input(f"enter number {i+1} : ")
    set.add(number)
print(set)

# 3. Can we have a set with 18 (int) and '18' (str) as a value in it?
string={18,"18"}
print(string)
print(type(string))

# 4. What will be the length of following set s:
s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?
print(len(s))
print(s)
# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique
language= {}
for i in range(4):
    name= input("enter your name: ")
    lang=input("enter your language: ")
    language.update({name:lang})
print(language)
