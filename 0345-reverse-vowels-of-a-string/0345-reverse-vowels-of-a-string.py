class Solution:
    def reverseVowels(self, s: str) -> str:
        left, right = 0, len(s) - 1
        vowelList = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        stringList = list(s)

        while left < right:
            if stringList[left] not in vowelList:
                left += 1
                continue
            if stringList[right] not in vowelList:
                right -= 1
                continue
            
            temp = stringList[left]
            stringList[left] = stringList[right]
            stringList[right] = temp
            left += 1
            right -= 1
        
        return ''.join(stringList)
