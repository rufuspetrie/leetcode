class Solution:
    def average(self, salary: List[int]) -> float:
        x = max(salary)
        y = min(salary)
        return sum([i for i in salary if i !=x and i != y])/(len(salary)-2)