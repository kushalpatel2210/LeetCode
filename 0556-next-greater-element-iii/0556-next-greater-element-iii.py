class Solution:
    def nextGreaterElement(self, n: int) -> int:
        charsList = list(str(n))
        n = len(charsList)

        # find first decreasing element
        i = n - 2
        while i >= 0 and charsList[i] >= charsList[i + 1]:
            i -= 1
        
        if i < 0:
            return -1 
        
        # find next greater element than charsList[i]
        j = n - 1
        while j >= 0 and charsList[i] >= charsList[j]:
            j -= 1
        
        # reverse the biggest permutation starting from i + 1
        charsList[i], charsList[j] = charsList[j], charsList[i]

        charsList[i + 1:] = reversed(charsList[i + 1:])
        res = int("".join(charsList))
        return res if res <= 2 **31 - 1 else -1
