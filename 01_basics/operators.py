# operators.py

# -------------------------------
# 1. Arithmetic Operators
# -------------------------------

a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)        # float result
print("Floor Division:", a // b) # integer result
print("Modulus:", a % b)
print("Exponent:", a ** b)


# -------------------------------
# 2. Comparison Operators
# -------------------------------

x = 5
y = 10

print("Equal:", x == y)
print("Not Equal:", x != y)
print("Greater Than:", x > y)
print("Less Than:", x < y)
print("Greater or Equal:", x >= y)
print("Less or Equal:", x <= y)


# -------------------------------
# 3. Logical Operators
# -------------------------------

p = True
q = False

print("AND:", p and q)
print("OR:", p or q)
print("NOT p:", not p)


# -------------------------------
# 4. Assignment Operators
# -------------------------------

num = 5

num += 2   # num = num + 2
print("+= :", num)

num *= 3   # num = num * 3
print("*= :", num)

num -= 4
print("-= :", num)

num /= 2
print("/= :", num)


# -------------------------------
# 5. Identity Operators
# -------------------------------

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print("a is b:", a is b)     # True (same memory)
print("a is c:", a is c)     # False (different memory)
print("a == c:", a == c)     # True (same values)


# -------------------------------
# 6. Membership Operators
# -------------------------------

nums = [1, 2, 3, 4]

print("2 in nums:", 2 in nums)
print("5 not in nums:", 5 not in nums)


# -------------------------------
# 7. Real Example (Important)
# -------------------------------

# Check if number is even or odd

n = 7

if n % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# -------------------------------
# 8. Operator Precedence Demo
# -------------------------------

result = 10 + 2 * 3
print("Without brackets:", result)

result = (10 + 2) * 3
print("With brackets:", result)
