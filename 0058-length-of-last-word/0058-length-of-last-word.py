class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sList = s.split()
        
        return len(sList[-1])