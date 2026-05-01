# next_greater_element.py

"""
Problem: Next Greater Element (NGE)

Given an array, for each element find the next greater element to its right.
If none exists, return -1.

Example:
Input: [2, 1, 2, 4, 3]
Output: [4, 2, 4, -1, -1]

Approach (Monotonic Stack):
- Traverse from right to left
- Maintain a decreasing stack
- Pop elements smaller than current
- Top of stack = next greater element

Time Complexity: O(n)
Space Complexity: O(n)
"""

def next_greater(nums):
    stack = []
    result = [-1] * len(nums)

    for i in range(len(nums) - 1, -1, -1):
        # Remove smaller elements
        while stack and stack[-1] <= nums[i]:
            stack.pop()

        # If stack not empty, top is answer
        if stack:
            result[i] = stack[-1]

        stack.append(nums[i])

    return result


# -------------------------------
# Test Cases
# -------------------------------

nums1 = [2, 1, 2, 4, 3]
print("Output:", next_greater(nums1))  # [4,2,4,-1,-1]

nums2 = [5, 4, 3, 2, 1]
print("Output:", next_greater(nums2))  # [-1,-1,-1,-1,-1]
