class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def check(x):
            rotations_top = rotations_bottom = 0

            for i in range(len(tops)):
                if tops[i] != x and bottoms[i] != x:
                    return float('inf')
                elif tops[i] != x:
                    rotations_top += 1
                elif bottoms[i] != x:
                    rotations_bottom += 1
            
            return min(rotations_top, rotations_bottom)
        
        # It is guaranteed that if the solution exists then top or col row must be formed using first elment of either one of it.
        minRotations = min(check(tops[0]), check(bottoms[0]))
        return minRotations if minRotations != float('inf') else -1
                