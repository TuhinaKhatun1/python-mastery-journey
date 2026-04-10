# lists.py

# -------------------------------
# 1. Creating a List
# -------------------------------

nums = [1, 2, 3, 4, 5]
print("List:", nums)


# -------------------------------
# 2. Accessing Elements
# -------------------------------

print("First element:", nums[0])
print("Last element:", nums[-1])


# -------------------------------
# 3. Modifying List
# -------------------------------

nums[1] = 10
print("Updated list:", nums)


# -------------------------------
# 4. Adding Elements
# -------------------------------

nums.append(6)        # add at end
nums.insert(1, 99)    # insert at index

print("After adding:", nums)


# -------------------------------
# 5. Removing Elements
# -------------------------------

nums.remove(99)   # remove value
nums.pop()        # remove last

print("After removal:", nums)


# -------------------------------
# 6. List Slicing
# -------------------------------

print("First 3:", nums[:3])
print("Last 2:", nums[-2:])


# -------------------------------
# 7. Looping Through List
# -------------------------------

for num in nums:
    print("Element:", num)


# -------------------------------
# 8. List Comprehension (Important)
# -------------------------------

squares = [x * x for x in range(1, 6)]
print("Squares:", squares)


# -------------------------------
# 9. Common List Functions
# -------------------------------

numbers = [4, 2, 8, 1]

print("Length:", len(numbers))
print("Max:", max(numbers))
print("Min:", min(numbers))
print("Sorted:", sorted(numbers))


# -------------------------------
# 10. Real Example (Important)
# -------------------------------

# Find largest number in list

nums = [10, 45, 23, 89, 12]

largest = nums[0]

for num in nums:
    if num > largest:
        largest = num

print("Largest:", largest)


# -------------------------------
# 11. Remove duplicates
# -------------------------------

nums = [1, 2, 2, 3, 4, 4, 5]

unique = []

for num in nums:
    if num not in unique:
        unique.append(num)

print("Unique list:", unique)


# -------------------------------
# 12. Reverse list
# -------------------------------

nums = [1, 2, 3, 4]

nums.reverse()
print("Reversed:", nums)
