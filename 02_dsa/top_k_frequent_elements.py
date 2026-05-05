# top_k_frequent_elements.py

"""
Problem: Top K Frequent Elements

Given an integer array nums and an integer k,
return the k most frequent elements.

Example:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Approach (Heap):
- Count frequency using hashmap
- Use heap to get top k elements

Time Complexity: O(n log k)
Space Complexity: O(n)
"""

import heapq
from collections import Counter

def top_k_frequent(nums, k):
    count = Counter(nums)

    # Min heap
    heap = []

    for num, freq in count.items():
        heapq.heappush(heap, (freq, num))

        if len(heap) > k:
            heapq.heappop(heap)

    return [num for freq, num in heap]


# -------------------------------
# Test Cases
# -------------------------------

nums1 = [1,1,1,2,2,3]
k1 = 2
print("Output:", top_k_frequent(nums1, k1))  # [1,2]

nums2 = [1]
k2 = 1
print("Output:", top_k_frequent(nums2, k2))  # [1]
