# loops.py

# -------------------------------
# 1. for loop (basic)
# -------------------------------

for i in range(5):
    print("Iteration:", i)


# -------------------------------
# 2. for loop with range(start, end, step)
# -------------------------------

for i in range(1, 10, 2):
    print("Odd number:", i)


# -------------------------------
# 3. while loop
# -------------------------------

count = 0

while count < 5:
    print("Count:", count)
    count += 1


# -------------------------------
# 4. break statement
# -------------------------------

for i in range(10):
    if i == 5:
        break
    print("Break at:", i)


# -------------------------------
# 5. continue statement
# -------------------------------

for i in range(5):
    if i == 2:
        continue
    print("Skip 2:", i)


# -------------------------------
# 6. pass statement
# -------------------------------

for i in range(3):
    pass  # placeholder (does nothing)


# -------------------------------
# 7. Loop with else
# -------------------------------

for i in range(3):
    print("Loop:", i)
else:
    print("Loop finished")


# -------------------------------
# 8. Nested loops
# -------------------------------

for i in range(3):
    for j in range(2):
        print("i:", i, "j:", j)


# -------------------------------
# 9. Real Example (Important)
# -------------------------------

# Print multiplication table of a number

num = 5

for i in range(1, 11):
    print(num, "x", i, "=", num * i)


# -------------------------------
# 10. Pattern Printing (Very Important)
# -------------------------------

# *
# **
# ***
# ****

for i in range(1, 5):
    for j in range(i):
        print("*", end=" ")
    print()


# -------------------------------
# 11. Sum of numbers using loop
# -------------------------------

n = 5
total = 0

for i in range(1, n + 1):
    total += i

print("Sum:", total)


# -------------------------------
# 12. Reverse a number using while loop
# -------------------------------

num = 1234
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

print("Reversed number:", reverse)
