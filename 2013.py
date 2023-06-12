# Initial thoughts
    # Might be useful: diagonals uniquely determine squares and can search for other points
    # Note that dulicate points count as different ways of forming a square,
        # so need to store both points and point counts
    # Note: need to use a hash and an array b/c can't iterate over hash keys properly
class DetectSquares:

    def __init__(self):
        self.counts = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        self.counts[tuple(point)] += 1
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        x, y = point
        for xx, yy in self.points:
            if abs(x - xx) == abs(y - yy) and y != yy and x != xx:
                res += self.counts[(x, yy)] * self.counts[(xx, y)]
        return res

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)