# minimum_window_substring.py

"""
Problem: Minimum Window Substring

Given two strings s and t, return the minimum window substring of s
such that every character in t (including duplicates) is included.

If no such substring exists, return "".

Example:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"

Approach (Sliding Window + HashMap):
- Count characters of t
- Expand window using right pointer
- When valid → try shrinking from left
- Track minimum window

Time Complexity: O(n)
Space Complexity: O(1)
"""

from collections import Counter

def min_window(s, t):
    if not s or not t:
        return ""

    t_count = Counter(t)
    window = {}

    have = 0
    need = len(t_count)

    res = [-1, -1]
    res_len = float("inf")

    left = 0

    for right in range(len(s)):
        char = s[right]
        window[char] = window.get(char, 0) + 1

        if char in t_count and window[char] == t_count[char]:
            have += 1

        # When window is valid → shrink it
        while have == need:
            # Update result
            if (right - left + 1) < res_len:
                res = [left, right]
                res_len = right - left + 1

            # Remove left char
            window[s[left]] -= 1
            if s[left] in t_count and window[s[left]] < t_count[s[left]]:
                have -= 1

            left += 1

    l, r = res
    return s[l:r+1] if res_len != float("inf") else ""


# -------------------------------
# Test Cases
# -------------------------------

s1 = "ADOBECODEBANC"
t1 = "ABC"
print("Output:", min_window(s1, t1))  # BANC

s2 = "a"
t2 = "a"
print("Output:", min_window(s2, t2))  # a

s3 = "a"
t3 = "aa"
print("Output:", min_window(s3, t3))  # ""
