class Solution:
    def isPalindrome(self, word):
        start, end = 0, len(word) - 1

        while start < end:
            if word[start] != word[end]:
                return False
            start += 1
            end -= 1
        
        return True

    def firstPalindrome(self, words: List[str]) -> str:
        res = ''

        for word in words:
            if self.isPalindrome(word):
                res = word
                break
        
        return res