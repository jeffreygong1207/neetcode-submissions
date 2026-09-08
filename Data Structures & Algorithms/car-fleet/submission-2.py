class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairings = []
        for i in range(len(position)):
            pairings.append((position[i], speed[i]))
        
        pairings = sorted(pairings, reverse=True)

        stack = []
        times = []
        for i in range(len(pairings)):
            time = (target - pairings[i][0]) / pairings[i][1]
            times.append(time)
            if i > 0:
                if times[i] > stack[-1]:
                    stack.append(time)
            else:
                stack.append(time)
        

        return len(stack)