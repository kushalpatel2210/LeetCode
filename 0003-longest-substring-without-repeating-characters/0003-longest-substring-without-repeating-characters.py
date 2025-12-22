class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0 
        ele = set()
        max_window = 0

        for j in range(len(s)):
            while i < j and s[j] in ele:
                ele.remove(s[i])
                i += 1
                
            ele.add(s[j])
            max_window = max(max_window, len(ele))
        
        return max_window