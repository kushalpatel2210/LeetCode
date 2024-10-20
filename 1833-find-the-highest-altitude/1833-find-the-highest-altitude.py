class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxAltitude = altitude = 0

        for elevation in gain:
            altitude += elevation
            maxAltitude = max(altitude, maxAltitude)
        
        return maxAltitude