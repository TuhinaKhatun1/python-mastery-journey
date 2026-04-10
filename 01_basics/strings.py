# strings.py

# -------------------------------
# 1. Creating Strings
# -------------------------------

s = "hello"
print("String:", s)


# -------------------------------
# 2. Accessing Characters
# -------------------------------

print("First char:", s[0])
print("Last char:", s[-1])


# -------------------------------
# 3. String Slicing
# -------------------------------

print("First 3 chars:", s[:3])
print("Last 2 chars:", s[-2:])


# -------------------------------
# 4. String Methods
# -------------------------------

text = "  Python Programming  "

print(text.lower())
print(text.upper())
print(text.strip())
print(text.replace("Python", "Java"))


# -------------------------------
# 5. Looping Through String
# -------------------------------

for ch in s:
    print(ch)


# -------------------------------
# 6. Reverse a String
# -------------------------------

s = "hello"

# Method 1 (slicing)
print("Reversed:", s[::-1])

# Method 2 (loop)
rev = ""
for ch in s:
    rev = ch + rev
print("Reversed (loop):", rev)


# -------------------------------
# 7. Check Palindrome (IMPORTANT)
# -------------------------------

def is_palindrome(s):
    return s == s[::-1]

print("Palindrome:", is_palindrome("madam"))


# -------------------------------
# 8. Count Characters
# -------------------------------

s = "programming"
count = {}

for ch in s:
    if ch in count:
        count[ch] += 1
    else:
        count[ch] = 1

print("Character count:", count)


# -------------------------------
# 9. Remove Duplicates from String
# -------------------------------

s = "banana"
result = ""

for ch in s:
    if ch not in result:
        result += ch

print("Without duplicates:", result)


# -------------------------------
# 10. Anagram Check (IMPORTANT)
# -------------------------------

def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

print("Anagram:", is_anagram("listen", "silent"))


# -------------------------------
# 11. Find First Non-Repeating Character
# -------------------------------

s = "aabbcde"

for ch in s:
    if s.count(ch) == 1:
        print("First non-repeating:", ch)
        break


# -------------------------------
# 12. Real Interview Example
# -------------------------------

# Count vowels and consonants

s = "hello world"

vowels = "aeiou"
v_count = 0
c_count = 0

for ch in s:
    if ch.isalpha():
        if ch in vowels:
            v_count += 1
        else:
            c_count += 1

print("Vowels:", v_count)
print("Consonants:", c_count)
