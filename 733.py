class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        old_color = image[sr][sc]
        if old_color == color: return image

        def dfs(r, c):
            if image[r][c] == old_color:
                image[r][c] = color
                if r > 0: dfs(r-1, c)
                if r < len(image) - 1: dfs(r+1, c)
                if c > 0: dfs(r, c-1)
                if c < len(image[0]) - 1: dfs(r, c+1)

        dfs(sr, sc)
        return image