# conditions.py

# -------------------------------
# 1. Basic if statement
# -------------------------------

age = 18

if age >= 18:
    print("You are eligible to vote")


# -------------------------------
# 2. if-else statement
# -------------------------------

num = 7

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# -------------------------------
# 3. if-elif-else ladder
# -------------------------------

marks = 85

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Fail")


# -------------------------------
# 4. Nested if
# -------------------------------

age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Not allowed")


# -------------------------------
# 5. Logical operators in conditions
# -------------------------------

username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid credentials")


# -------------------------------
# 6. Ternary (Short if-else)
# -------------------------------

num = 10
result = "Even" if num % 2 == 0 else "Odd"

print(result)


# -------------------------------
# 7. Real Example (Important)
# -------------------------------

# Find largest of three numbers

a = 10
b = 25
c = 15

if a >= b and a >= c:
    print("Largest is:", a)
elif b >= a and b >= c:
    print("Largest is:", b)
else:
    print("Largest is:", c)


# -------------------------------
# 8. Practice Problem
# -------------------------------

# Check if a year is leap year

year = 2024

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")
