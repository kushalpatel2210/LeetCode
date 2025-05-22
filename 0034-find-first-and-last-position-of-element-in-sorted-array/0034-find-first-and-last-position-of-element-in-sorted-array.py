class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def leftMostTarget():
            leftMost = float('inf')
            l, r = 0, len(nums) - 1

            while l <= r:
                m = l + (r - l) // 2
                
                if nums[m] == target:
                    leftMost = min(leftMost, m)
                    r = m - 1
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            
            return leftMost if leftMost != float('inf') else -1
        
        def rightMostTarget():
            rightMost = float('-inf')
            l, r = 0, len(nums) - 1

            while l <= r:
                m = l + (r - l) // 2

                if nums[m] == target:
                    rightMost = max(rightMost, m)
                    l = m + 1
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            
            return rightMost if rightMost != float('-inf') else -1

        return [leftMostTarget(), rightMostTarget()]