# move_zeroes.py

"""
Problem: Move Zeroes

Given an integer array nums, move all 0's to the end
while maintaining the relative order of non-zero elements.

You must do this in-place.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Approach (Two Pointer):
- Use one pointer for placing non-zero elements
- Traverse array and shift non-zero elements forward
- Fill remaining positions with 0

Time Complexity: O(n)
Space Complexity: O(1)
"""

def move_zeroes(nums):
    insert_pos = 0

    # Move all non-zero elements forward
    for num in nums:
        if num != 0:
            nums[insert_pos] = num
            insert_pos += 1

    # Fill remaining positions with zero
    while insert_pos < len(nums):
        nums[insert_pos] = 0
        insert_pos += 1


# -------------------------------
# Test Cases
# -------------------------------

nums1 = [0, 1, 0, 3, 12]
move_zeroes(nums1)
print("Output:", nums1)  # [1,3,12,0,0]

nums2 = [0, 0, 1]
move_zeroes(nums2)
print("Output:", nums2)  # [1,0,0]
