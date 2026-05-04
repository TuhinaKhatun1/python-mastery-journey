# largest_rectangle_histogram.py

"""
Problem: Largest Rectangle in Histogram

Given an array heights representing bar heights,
find the area of the largest rectangle.

Example:
Input: [2,1,5,6,2,3]
Output: 10

Approach (Monotonic Stack):
- Use stack to store indices
- Maintain increasing heights
- When current height < stack top → calculate area

Time Complexity: O(n)
Space Complexity: O(n)
"""

def largest_rectangle_area(heights):
    stack = []  # stores indices
    max_area = 0

    for i in range(len(heights)):
        while stack and heights[i] < heights[stack[-1]]:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)

        stack.append(i)

    # Remaining elements in stack
    while stack:
        height = heights[stack.pop()]
        width = len(heights) if not stack else len(heights) - stack[-1] - 1
        max_area = max(max_area, height * width)

    return max_area


# -------------------------------
# Test Cases
# -------------------------------

h1 = [2,1,5,6,2,3]
print("Output:", largest_rectangle_area(h1))  # 10

h2 = [2,4]
print("Output:", largest_rectangle_area(h2))  # 4
