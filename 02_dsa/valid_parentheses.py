# valid_parentheses.py

"""
Problem: Valid Parentheses

Given a string s containing just '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

A string is valid if:
- Open brackets are closed by same type
- Open brackets are closed in correct order

Example:
Input: "()[]{}"
Output: True

Approach (Stack):
- Use stack to track opening brackets
- When closing bracket appears → check top of stack
- If mismatch → invalid

Time Complexity: O(n)
Space Complexity: O(n)
"""

def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:
            top = stack.pop() if stack else '#'

            if mapping[char] != top:
                return False
        else:
            stack.append(char)

    return not stack


# -------------------------------
# Test Cases
# -------------------------------

print(is_valid("()"))        # True
print(is_valid("()[]{}"))    # True
print(is_valid("(]"))        # False
print(is_valid("([)]"))      # False
print(is_valid("{[]}"))      # True
