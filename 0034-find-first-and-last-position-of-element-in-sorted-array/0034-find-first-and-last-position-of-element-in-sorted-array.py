class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1

        def findFirst(l, r):
            firstOcc = float('inf')
            while l <= r:
                mid = l + (r - l) // 2

                if nums[mid] == target:
                    firstOcc = min(firstOcc, mid)
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            
            return firstOcc
        
        def findLast(l, r):
            lastOcc = float('-inf')
            while l <= r:
                mid = l + (r - l) // 2

                if nums[mid] == target:
                    lastOcc = max(lastOcc, mid)
                    l = mid + 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return lastOcc
        
        findFirstOcc = findFirst(l, r)
        findLastOcc = findLast(l, r)

        return [-1 if findFirstOcc == float('inf') else findFirstOcc, -1 if findLastOcc == float('-inf') else findLastOcc]

            
