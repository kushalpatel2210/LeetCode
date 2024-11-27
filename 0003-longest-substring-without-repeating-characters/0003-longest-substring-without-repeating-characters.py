class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_list = list()
        longestSubString = 0

        for i in range(len(s)):
            if s[i] in my_list:
                longestSubString = max(longestSubString, len(my_list))
                my_list = my_list[my_list.index(s[i]) + 1:]

            my_list.append(s[i])
        
        return max(longestSubString, len(my_list))