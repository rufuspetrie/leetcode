class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        x = len(flowerbed)
        flowers_placed = 0

        for i in range(x):
            if flowerbed[i] == 0:
                left = i == 0 or flowerbed[i-1] == 0
                right = i == x - 1 or flowerbed[i+1] == 0
                if left and right:
                    flowers_placed += 1
                    flowerbed[i] = 1
        
        return flowers_placed >= n