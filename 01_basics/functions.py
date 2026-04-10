# functions.py

# -------------------------------
# 1. Basic Function
# -------------------------------

def greet():
    print("Hello, welcome!")

greet()


# -------------------------------
# 2. Function with Parameters
# -------------------------------

def greet_user(name):
    print("Hello,", name)

greet_user("Tuhina")


# -------------------------------
# 3. Function with Return Value
# -------------------------------

def add(a, b):
    return a + b

result = add(5, 3)
print("Sum:", result)


# -------------------------------
# 4. Default Parameters
# -------------------------------

def power(base, exponent=2):
    return base ** exponent

print(power(3))      # square
print(power(2, 3))   # cube


# -------------------------------
# 5. Keyword Arguments
# -------------------------------

def student(name, age):
    print("Name:", name, "Age:", age)

student(age=20, name="Tuhina")


# -------------------------------
# 6. Arbitrary Arguments (*args)
# -------------------------------

def total_sum(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print("Total:", total_sum(1, 2, 3, 4))


# -------------------------------
# 7. Arbitrary Keyword Arguments (**kwargs)
# -------------------------------

def user_info(**details):
    for key, value in details.items():
        print(key, ":", value)

user_info(name="Tuhina", age=21, city="Kolkata")


# -------------------------------
# 8. Lambda Function (Anonymous)
# -------------------------------

square = lambda x: x * x
print("Square:", square(5))


# -------------------------------
# 9. Recursion (Important for DSA)
# -------------------------------

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial:", factorial(5))


# -------------------------------
# 10. Real Example
# -------------------------------

# Check if a number is prime

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print("Is prime:", is_prime(7))
