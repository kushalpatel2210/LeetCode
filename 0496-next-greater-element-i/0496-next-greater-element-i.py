class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = [] # monotonically decreasing
        suffix = [-1] * len(nums2)
        res = []

        for i, n in enumerate(nums2):
            while stack and stack[-1][0] <= n:
                num, idx = stack.pop()
                suffix[idx] = n
            stack.append((n, i))

        for n in nums1:
            idxOfCurrNumInNums2 = nums2.index(n)
            res.append(suffix[idxOfCurrNumInNums2])

        return res
