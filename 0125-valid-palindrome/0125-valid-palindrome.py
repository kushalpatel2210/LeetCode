class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1

        while start < end:
            if not s[start].isalnum():
                start += 1
                continue

            if not s[end].isalnum():
                end -= 1
                continue
            
            if s[start].lower() != s[end].lower():
                return False

            start += 1
            end -= 1
            
        return True