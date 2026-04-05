"""
Topic: Variables in Python

Definition:
A variable is used to store data in memory. Python is dynamically typed,
so you don't need to declare the data type explicitly.
"""

# -------------------------------
# 1. Basic Variable Assignment
# -------------------------------

a = 10              # Integer
b = 3.14            # Float
c = "Hello Python"  # String
d = True            # Boolean

print("Integer:", a)
print("Float:", b)
print("String:", c)
print("Boolean:", d)


# -------------------------------
# 2. Multiple Assignment
# -------------------------------

x, y, z = 1, 2, 3
print("\nMultiple Assignment:", x, y, z)


# -------------------------------
# 3. Dynamic Typing
# -------------------------------

var = 10
print("\nBefore:", var, type(var))

var = "Now I'm a string"
print("After:", var, type(var))


# -------------------------------
# 4. Type Checking
# -------------------------------

num = 100
print("\nType of num:", type(num))


# -------------------------------
# 5. Type Casting
# -------------------------------

num_str = "50"
num_int = int(num_str)

print("\nConverted String to Int:", num_int, type(num_int))


# -------------------------------
# 6. Constants (Convention)
# -------------------------------

PI = 3.14159  # Constants are written in uppercase by convention
print("\nConstant PI:", PI)


# -------------------------------
# 7. Small Practical Example
# -------------------------------

name = "Tuhina"
age = 21

print(f"\nMy name is {name} and I am {age} years old.")
