class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0 
        j = len(s) - 1
        
        while i < j:
            # Process elements
            leftChar = s[i]
            rightChar = s[j]
            if not leftChar.isalnum():
                i += 1
            elif not rightChar.isalnum():
                j -= 1
            else:
                if leftChar.lower() == rightChar.lower():
                    i += 1
                    j -= 1
                else:
                    return False

        return True