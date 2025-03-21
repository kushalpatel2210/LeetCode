class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        res = 0
        currSum = 0

        for r in range(len(arr)):
            currSum += arr[r]

            if r - l + 1 < k:
                # print(f"r {r} arr[r] {arr[r]}")
                continue
            
            # print(f"l {l} r {r} currSum {currSum}")
            
            if currSum / k >= threshold:
                res += 1

            currSum -= arr[l]
            l += 1

        return res