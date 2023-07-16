# Notes:
    # Use ETA's instead of computing relative velocities to avoid zero division
    # Another option is to just push the ETA to the stack instead of p/s
    # For each car, compute how long it will take to reach the target
        # If shorter than the top of the stack, it becomes part of a fleet
        # If longer than the top of the stack, it stays behind
    # Return the length of the stack to find the number of fleets
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        fleet = sorted(zip(position, speed), key = lambda x: -x[0])
        stack = []
        for (p, s) in fleet:
            ETA = (target - p) / s
            if not stack: stack.append(ETA)
            if ETA > stack[-1]: stack.append(ETA)
        
        return len(stack)