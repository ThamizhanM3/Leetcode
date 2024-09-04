class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        m = len(flowerbed)
        if m == 1 and flowerbed[0] == 0 and n < 2:
            return True
        if m == 2 and 1 not in flowerbed and n < 2:
            return True
        if flowerbed[0] == 0 and flowerbed[1] != 1:
            flowerbed[0] = 1
            n -= 1
        for i in range(1, m-1):
            if flowerbed[i] == 0 and flowerbed[i-1] != 1 and flowerbed[i+1] != 1:
                flowerbed[i] = 1
                n -= 1
        if flowerbed[-1] == 0 and flowerbed[-2] != 1:
            flowerbed[0] = 1
            n -= 1
        return True if n <= 0 else False