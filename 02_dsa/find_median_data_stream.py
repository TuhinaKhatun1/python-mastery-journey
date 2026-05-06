# find_median_data_stream.py

"""
Problem: Find Median from Data Stream

Design a data structure that supports:
1. add_num(num)
2. find_median()

Median:
- Middle value in sorted order
- If even count → average of middle two

Approach (Two Heaps):
- Max heap → stores smaller half
- Min heap → stores larger half
- Balance heaps after insertion

Time Complexity:
- add_num(): O(log n)
- find_median(): O(1)

Space Complexity: O(n)
"""

import heapq

class MedianFinder:

    def __init__(self):
        # Max heap (store negative values)
        self.small = []

        # Min heap
        self.large = []

    def add_num(self, num):

        # Add to max heap
        heapq.heappush(self.small, -num)

        # Ensure ordering property
        if self.small and self.large and (-self.small[0] > self.large[0]):
            value = -heapq.heappop(self.small)
            heapq.heappush(self.large, value)

        # Balance heap sizes
        if len(self.small) > len(self.large) + 1:
            value = -heapq.heappop(self.small)
            heapq.heappush(self.large, value)

        if len(self.large) > len(self.small):
            value = heapq.heappop(self.large)
            heapq.heappush(self.small, -value)

    def find_median(self):

        if len(self.small) > len(self.large):
            return -self.small[0]

        return (-self.small[0] + self.large[0]) / 2


# -------------------------------
# Test Cases
# -------------------------------

mf = MedianFinder()

mf.add_num(1)
mf.add_num(2)

print("Median:", mf.find_median())  # 1.5

mf.add_num(3)

print("Median:", mf.find_median())  # 2
