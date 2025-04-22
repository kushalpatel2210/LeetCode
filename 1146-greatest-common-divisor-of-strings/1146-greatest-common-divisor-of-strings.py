import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)
        gcd = math.gcd(len1, len2)
        res = ''
        if str1[0] == str2[0]:
            res = str1[:gcd]
        return res