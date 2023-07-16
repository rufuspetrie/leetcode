# Initial thoughts
    # Seems like can just use hash with another hash as the value
    # Note: timestamps are inserted in increasing order, so can use binary search
    # Hash will be of the form d[key][time] = value, and we need to perform binary search
        # on the d[key].items() to efficiently find the value at a given timestamp
    # Using single hash with list of tuples makes more sense because the d.items()
        # object is not very amenable to binary search
class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d.keys():
            self.d[key] = []
        self.d[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d.keys(): return ""
        output = ""
        l = 0
        r = len(self.d[key]) - 1
        while l <= r:
            mid = (l + r)//2
            if self.d[key][mid][0] == timestamp:
                return self.d[key][mid][1]
            elif self.d[key][mid][0] < timestamp:
                output = self.d[key][mid][1]
                l = mid + 1
            else:
                r = mid - 1

        return output

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)