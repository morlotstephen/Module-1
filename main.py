# TODO: Create an integer variable named 'age' with your age
# TODO: Create a float variable named 'height' with your height in meters
# TODO: Create a string variable named 'name' with your name
# TODO: Create a boolean variable named 'is_student' and set it to True

# Print all variables and their types
# Example: print(f"Age: {age}, Type: {type(age)}")

age = 23
height = 1.86
name = "morlot stephen"
is_student = True

print(age, height, name, is_student)
print(f"age: {age}, Type: {type(age)}")
print(f"height: {height}, Type: {type(height)}")
print(f"name: {name}, Type: {type(name)}")
print(f"is_student: {is_student}, Type: {type(is_student)}")


# TODO: Create two variables 'a' and 'b' with numeric values
# TODO: Perform addition, subtraction, multiplication, and division of a and b
# Print the results of each operation
# TODO: Calculate the remainder of a divided by b using the modulo operator
# TODO: Calculate a to the power of b using the exponentiation operator

a = 4
b = 10

print(a + b)
print(a - b)
print(a * b)
print(a / b)


# TODO: Create two string variables 'first_name' and 'last_name'
# TODO: Concatenate the two names to create a 'full_name' variable
# TODO: Print the full name in uppercase
# TODO: Print the length of the full name
# TODO: Create a string with multiple words and split it into a list

first_name = "MORLOT"
last_name = "Stephen"
full_name = first_name+" "+last_name
print(full_name)


# TODO: Convert a string containing a number to an integer
# TODO: Convert a float to an integer
# TODO: Convert an integer to a float
# TODO: Convert a number (integer or float) to a string
# Print all converted values and their new types

string = "1"
variable = int(string)
print(type(variable))

nombre_float = 12.9
nombre_int = int(nombre_float)
print(type(nombre_int))

nbr_int = 4
nbr_float = float(nbr_int)
print(type(nbr_float))

n_int = 42
s_int = str(n_int)
print(s_int)       
print(type(s_int))

# TODO: Perform AND, OR, and NOT operations on these variables
# Print the results

# TODO: Create two numeric variables and use comparison operators
# (>, <, >=, <=, ==, !=) to compare them
# Print the results of these comparisons


is_student = True
is_women = False
print(is_student, is_women)
print(not is_student)
print(is_student and is_women)
print(is_student or is_women)

x = 5
y = 10
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
print(x == y)
print(x != y)
