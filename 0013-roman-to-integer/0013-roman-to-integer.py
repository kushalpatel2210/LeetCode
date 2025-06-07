class Solution:
    def romanToInt(self, s: str) -> int:
        hashMap = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        num = 0

        for i in range(len(s)):
            if i > 0:
                if hashMap[s[i - 1]] < hashMap[s[i]]:
                    num += hashMap[s[i]] - 2 * hashMap[s[i - 1]]
                else:
                    num += hashMap[s[i]]
            else:
                num += hashMap[s[i]]
                    
        return num