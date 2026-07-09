#we are going to learn type casting  
#type casting is the process of converting a variable from one data type to another 
#str(), int(), float(), bool() are the functions used for type casting
name = "Erica"
age = 23
gpa = 3.5
is_student = True
#convert gpa to a integer, it is currently a float
gpa = int(gpa)
print(f"my gpa is {gpa}")
#lets convert age into a float, it is currently an integer
age = float(age) 
print (age)
#lets convert strings iinto boolean
#we could use this if someone actually typed there name
name = bool(name)
print (name)