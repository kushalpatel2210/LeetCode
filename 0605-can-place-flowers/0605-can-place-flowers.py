class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed_length = len(flowerbed)

        for i in range(len(flowerbed)):
            if i == 0 or i == flowerbed_length - 1:
                if i == 0 and i + 1 < flowerbed_length and flowerbed[i + 1] == 0 and flowerbed[i] == 0:
                    flowerbed[i] = 1
                    n -= 1
                if i == flowerbed_length - 1 and i - 1 < flowerbed_length and flowerbed[i - 1] == 0 and flowerbed[i] == 0:
                    flowerbed[i] = 1
                    n -= 1
            else:
                if flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and flowerbed[i] == 0:
                    flowerbed[i] = 1
                    n -= 1
        
        return n <= 0