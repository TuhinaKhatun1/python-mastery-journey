# kth_largest_element.py

"""
Problem: Kth Largest Element in an Array

Given an integer array nums and an integer k,
return the kth largest element in the array.

Example:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Approach (Min Heap):
- Maintain a heap of size k
- Push elements
- Remove smallest if size exceeds k
- Top of heap = kth largest

Time Complexity: O(n log k)
Space Complexity: O(k)
"""

import heapq

def find_kth_largest(nums, k):
    heap = []

    for num in nums:
        heapq.heappush(heap, num)

        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]


# -------------------------------
# Test Cases
# -------------------------------

nums1 = [3,2,1,5,6,4]
k1 = 2
print("Output:", find_kth_largest(nums1, k1))  # 5

nums2 = [3,2,3,1,2,4,5,5,6]
k2 = 4
print("Output:", find_kth_largest(nums2, k2))  # 4
