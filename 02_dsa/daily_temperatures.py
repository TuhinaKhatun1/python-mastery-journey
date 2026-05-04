# daily_temperatures.py

"""
Problem: Daily Temperatures

Given an array temperatures, return an array answer such that:
answer[i] is the number of days you have to wait after day i
to get a warmer temperature.

If no future day exists, answer[i] = 0.

Example:
Input: [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Approach (Monotonic Stack):
- Use stack to store indices
- Maintain decreasing temperatures in stack
- When a warmer day comes → resolve previous days

Time Complexity: O(n)
Space Complexity: O(n)
"""

def daily_temperatures(temperatures):
    stack = []  # stores indices
    result = [0] * len(temperatures)

    for i in range(len(temperatures)):
        # Resolve previous colder days
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev_index = stack.pop()
            result[prev_index] = i - prev_index

        stack.append(i)

    return result


# -------------------------------
# Test Cases
# -------------------------------

temps1 = [73,74,75,71,69,72,76,73]
print("Output:", daily_temperatures(temps1))  # [1,1,4,2,1,1,0,0]

temps2 = [30,40,50,60]
print("Output:", daily_temperatures(temps2))  # [1,1,1,0]

temps3 = [30,60,90]
print("Output:", daily_temperatures(temps3))  # [1,1,0]
