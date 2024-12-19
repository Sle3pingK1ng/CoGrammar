#Task 1 Auto-graded task 1
input("Please enter a sentence.")
str_manip = '''My name is James and I'm 34 years old'''
print (str_manip)
#calcualte string
length = len(str_manip)
print(length)
# Find the last character
Last_Char = str_manip[-1]
print(Last_Char)
# replace with @
replaceletter = Last_Char.replace("d", "@")
print(replaceletter)

#print lasr 3 letter
last3letter = replaceletter[-3]
print(last3letter[::-3])

# create a 5 letter word
firstchar = str_manip[3]
secondchar = str_manip[-2:]
combichar = firstchar + secondchar
print(combichar)

