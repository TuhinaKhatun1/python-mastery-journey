# longest_repeating_character_replacement.py

"""
Problem: Longest Repeating Character Replacement

You are given a string s and an integer k.
You can replace at most k characters.

Return the length of the longest substring containing the same letter
after performing at most k replacements.

Example:
Input: s = "AABABBA", k = 1
Output: 4

Approach (Sliding Window + Frequency Map):
- Use a hashmap to count characters
- Track the count of the most frequent character
- If window size - max_freq > k → shrink window
- Otherwise expand

Time Complexity: O(n)
Space Complexity: O(1) (since only uppercase letters)
"""

def character_replacement(s, k):
    count = {}
    left = 0
    max_freq = 0
    max_length = 0

    for right in range(len(s)):
        count[s[right]] = count.get(s[right], 0) + 1

        max_freq = max(max_freq, count[s[right]])

        # If window is invalid, shrink it
        while (right - left + 1) - max_freq > k:
            count[s[left]] -= 1
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length


# -------------------------------
# Test Cases
# -------------------------------

s1 = "AABABBA"
k1 = 1
print("Output:", character_replacement(s1, k1))  # 4

s2 = "ABAB"
k2 = 2
print("Output:", character_replacement(s2, k2))  # 4
