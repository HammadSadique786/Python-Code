#Python supports a wide variety of functions or methods like: int(), float(), str(), ord(), hex(), oct(), tuple(), set(), list(), dict(), etc. for the type casting in python.
a = "1" # string type of data
b = "2" # string type of data

print (int (a)) # to convert String into int we use int () function. this is called type casting
print (int (b))

# Add a and b
print (int (a) + int (b) )

# Two Types of Typecasting:

#     Explicit Conversion (Explicit type casting in python)
#     Implicit Conversion (Implicit type casting in python).

#     Explicit Conversion (The conversion of one data type into another data type, done via developer or programmer's intervention or manually as per the requirement, is known as explicit type conversion.)
string = "15"
number = 7
# we use int() function to convert string value into integer
string_number = int(string) #throws an error if the string is not a valid integer
sum= number + string_number
print("The Sum of both the numbers is: ", sum)

#     Implicit Conversion( one data type is converted into other by the Python interpreter itself (automatically). This is called, implicit typecasting in python.)
# Python automatically converts
# a to int
a = 7
print(type(a))
 
# Python automatically converts b to float
b = 3.0
print(type(b))
 
# Python automatically converts c to float as it is a float addition
c = a + b
print(c)
print(type(c))

