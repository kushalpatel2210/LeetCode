class Solution:
    def expandPalindrome(self, left, right, s):
        while left > 0 and right < len(s) - 1 and s[left - 1] == s[right + 1]:
            left -= 1
            right += 1
        return (left, right - left + 1)

    def longestPalindrome(self, s: str) -> str:
        start = maxLength = 0

        for center in range(len(s)):
            # odd length 'c'
            oddStart, oddMaxLength = self.expandPalindrome(center, center, s)
            if oddMaxLength > maxLength:
                start = oddStart
                maxLength = oddMaxLength

            # even length like 'cc'
            if center < len(s) - 1 and s[center] == s[center + 1]:
                evenStart, evenMaxLength = self.expandPalindrome(center, center + 1, s)
                if evenMaxLength > maxLength:
                    maxLength = evenMaxLength
                    start = evenStart
        
        return s[start: start + maxLength]
