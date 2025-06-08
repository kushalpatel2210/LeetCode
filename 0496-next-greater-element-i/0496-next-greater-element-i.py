class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = [] # monotonically decreasing
        suffix = [-1] * len(nums2)
        numIdx = dict()
        res = []

        for i, n in enumerate(nums2):
            numIdx[n] = i
            while stack and stack[-1][0] <= n:
                num, idx = stack.pop()
                suffix[idx] = n
            stack.append((n, i))

        for n in nums1:
            res.append(suffix[numIdx[n]])

        return res
