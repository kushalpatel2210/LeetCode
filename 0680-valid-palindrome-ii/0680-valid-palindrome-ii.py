class Solution:
    def validPalindrome(self, s: str) -> bool:
        start, end = 0, len(s) - 1 

        while start < end:
            if s[start] != s[end]:
                removeL, removeR = s[start + 1 : end + 1], s[start : end]
                return (removeL == removeL[::-1] or removeR == removeR[::-1])
            
            start += 1 
            end -= 1

        return True