# two_sum.py

"""
Problem: Two Sum

Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

Example:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]

Approach:
- Use a hashmap (dictionary)
- Store number → index
- Check if (target - current) exists

Time Complexity: O(n)
Space Complexity: O(n)
"""

def two_sum(nums, target):
    num_map = {}

    for i in range(len(nums)):
        complement = target - nums[i]

        if complement in num_map:
            return [num_map[complement], i]

        num_map[nums[i]] = i

    return [-1, -1]


# -------------------------------
# Test Cases
# -------------------------------

nums1 = [2, 7, 11, 15]
target1 = 9
print("Output:", two_sum(nums1, target1))  # [0, 1]

nums2 = [3, 2, 4]
target2 = 6
print("Output:", two_sum(nums2, target2))  # [1, 2]

nums3 = [3, 3]
target3 = 6
print("Output:", two_sum(nums3, target3))  # [0, 1]
