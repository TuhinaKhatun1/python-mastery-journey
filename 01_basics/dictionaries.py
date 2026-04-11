# dictionaries.py

# -------------------------------
# 1. Creating a Dictionary
# -------------------------------

student = {
    "name": "Tuhina",
    "age": 21,
    "course": "CSE"
}

print("Dictionary:", student)


# -------------------------------
# 2. Accessing Values
# -------------------------------

print("Name:", student["name"])
print("Age:", student.get("age"))


# -------------------------------
# 3. Adding / Updating Values
# -------------------------------

student["age"] = 22
student["college"] = "MAKAUT"

print("Updated:", student)


# -------------------------------
# 4. Removing Elements
# -------------------------------

student.pop("course")
print("After removal:", student)


# -------------------------------
# 5. Looping Through Dictionary
# -------------------------------

for key, value in student.items():
    print(key, ":", value)


# -------------------------------
# 6. Checking Keys
# -------------------------------

print("name" in student)
print("marks" in student)


# -------------------------------
# 7. Real Example (Important)
# -------------------------------

# Count frequency of elements

nums = [1, 2, 2, 3, 3, 3, 4]

freq = {}

for num in nums:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print("Frequency:", freq)


# -------------------------------
# 8. Find Most Frequent Element
# -------------------------------

max_count = 0
max_element = None

for key in freq:
    if freq[key] > max_count:
        max_count = freq[key]
        max_element = key

print("Most frequent:", max_element)


# -------------------------------
# 9. Dictionary Comprehension
# -------------------------------

squares = {x: x * x for x in range(1, 6)}
print("Squares:", squares)


# -------------------------------
# 10. Real Interview Pattern
# -------------------------------

# First non-repeating character

s = "aabbcde"

count = {}

for ch in s:
    count[ch] = count.get(ch, 0) + 1

for ch in s:
    if count[ch] == 1:
        print("First non-repeating:", ch)
        break
