# remove_duplicates_sorted_array.py

"""
Problem: Remove Duplicates from Sorted Array

Given a sorted array nums, remove duplicates in-place
such that each element appears only once.

Return the number of unique elements (k).

Example:
Input: [1,1,2]
Output: 2, nums = [1,2,_]

Approach (Two Pointer):
- Use one pointer (i) to track unique elements
- Traverse using another pointer (j)
- When a new element is found → place it at i+1

Time Complexity: O(n)
Space Complexity: O(1)
"""

def remove_duplicates(nums):
    if not nums:
        return 0

    i = 0  # pointer for unique elements

    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    return i + 1


# -------------------------------
# Test Cases
# -------------------------------

nums1 = [1, 1, 2]
k1 = remove_duplicates(nums1)
print("k:", k1, "Array:", nums1[:k1])  # [1,2]

nums2 = [0,0,1,1,1,2,2,3,3,4]
k2 = remove_duplicates(nums2)
print("k:", k2, "Array:", nums2[:k2])  # [0,1,2,3,4]
