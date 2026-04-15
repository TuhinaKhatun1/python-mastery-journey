# longest_substring_without_repeating.py

"""
Problem: Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring
without repeating characters.

Example:
Input: "abcabcbb"
Output: 3  ("abc")

Approach (Sliding Window + HashSet):
- Use two pointers (left, right)
- Expand window using right
- If duplicate found → shrink from left
- Track max length

Time Complexity: O(n)
Space Complexity: O(n)
"""

def length_of_longest_substring(s):
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length


# -------------------------------
# Test Cases
# -------------------------------

s1 = "abcabcbb"
print("Output:", length_of_longest_substring(s1))  # 3

s2 = "bbbbb"
print("Output:", length_of_longest_substring(s2))  # 1

s3 = "pwwkew"
print("Output:", length_of_longest_substring(s3))  # 3
