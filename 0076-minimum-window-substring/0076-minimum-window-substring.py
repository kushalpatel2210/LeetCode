from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = Counter(t)  # Frequency of characters in t
        window_count = Counter()  # Frequency of characters in the current window
        required = len(t_count)  # Number of unique characters in t
        formed = 0  # Tracks how many unique characters in the window satisfy the frequency
        i = 0  # Left pointer
        min_length = float('inf')
        result = ""

        for j in range(len(s)):
            # Expand the window
            char = s[j]
            window_count[char] += 1

            if char in t_count and window_count[char] == t_count[char]:
                formed += 1

            # Shrink window as long as the condition is met
            while formed == required:
                # Update the result if the current window is smaller
                if j - i + 1 < min_length:
                    min_length = j - i + 1
                    result = s[i:j+1]

                # Shrink the window from the left
                left_char = s[i]
                window_count[left_char] -= 1
                if left_char in t_count and window_count[left_char] < t_count[left_char]:
                    formed -= 1
                i += 1

        return result if min_length != float('inf') else ""