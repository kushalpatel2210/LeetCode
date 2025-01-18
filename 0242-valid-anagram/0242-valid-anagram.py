class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list1, list2 = list(s), list(t)
        list1.sort()
        list2.sort()
        return list1 == list2