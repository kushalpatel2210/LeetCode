class Solution:
    def nextGreaterElement(self, n: int) -> int:
        charsList = list(str(n))
        n = len(charsList)

        # Find the first decreasing element from the end
        i = n - 2
        while i >= 0 and charsList[i] >= charsList[i + 1]:
            i -= 1
        
        if i < 0:
            return - 1
        
        # find the smallest digit greater than charsList[i]
        j = n - 1
        while charsList[j] <= charsList[i]:
            j -= 1

        charsList[i], charsList[j] = charsList[j], charsList[i]

        # Step 4: Reverse the suffix (i+1 to end)
        charsList[i+1:] = reversed(charsList[i+1:])

        nextGreater = int("".join(charsList))
        
        return nextGreater if nextGreater <= 2**31 - 1 else -1