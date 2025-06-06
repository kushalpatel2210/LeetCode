class Solution:
    def expandString(self, left, right, s):
        while left > 0 and right < len(s) - 1 and s[left - 1] == s[right + 1]:
            left -= 1
            right += 1
        return (left, right - left + 1)

    def longestPalindrome(self, s: str) -> str:
        start = maxLength = 0 

        for center in range(len(s)):
            # odd start
            oddStart, maxOddLength = self.expandString(center, center, s)
            if maxOddLength > maxLength:
                start = oddStart
                maxLength = maxOddLength

            # even start 'cc'
            if center < len(s) - 1 and s[center] == s[center + 1]:
                evenStart, maxEvenLength = self.expandString(center, center + 1, s)
                if maxEvenLength > maxLength:
                    start = evenStart
                    maxLength = maxEvenLength

        return s[start: start + maxLength]