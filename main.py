print("I like tofu")
print ("i love the benifits of tofu")
#this is my first python program, this is an example of a comment
#Variable = a container of value (string, integer, float, boolean)
#a variable behaves as if it is the value that it contains
#a variable can be used to store data that can be used later in the program
#a variable can be used to store data that can be used later in the program
#this are strings
first_name = "Bonable"
food = "tofu"
email = "bonable@example.com"
#string uses double quotes or single quotes``
#a string is a sequence of characters, it can be letters, numbers, or symbols
print(f"Hello, {first_name}!")
print(f"i like eating {food}")
print(f"my email is {email}")
#when printing variables 
#you do not need to use quotes it will print the actual name of the variable rather than the value
#an f string is a string that is prefixed with the letter f
#it allows you to embed expressions inside string literals, using curly braces {}
# integer
age = 25
quantity = 10
num_of_students = 30
#an integer is a whole number, it can be positive or negative
#do not use quotes when assigning an integer it will become a string 
print(f'I am {age} years old')
print (f'I have bought {quantity} pieces of tofu for the week')
print(f"there are {num_of_students} students in the class, they can share the {quantity} of tofu equally")
# float 
#float are integer numbers with decimal points
price = 10.99
gpa = 2.3
print(f"the price of tofu is {price} per kilogram")
print(f"my gpa is {gpa}")
#boolean
#boolean is a data type that can only have two values: True or False
iam_student = True
forsale = False

print (f"are you a student? {iam_student}")
#boolean are usually used for conditonal statements like ff statements and loops
#like this one
if iam_student:
    print("you are a student")
#and this one
if forsale:
    print("the tofu is for sale") 
else:
    print("the tofu is not for sale")






