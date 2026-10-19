class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        for pos, sp in sorted(zip(position, speed), reverse=True):
            if not stack:
                stack.append((pos,sp))
            else:
                #check if we will catch up
                prev_pos, prev_speed = stack.pop()
                print("FUCK")
                print(prev_pos)
                time1 = (target - prev_pos)/prev_speed
                time2 = (target- pos)/sp
                stack.append((prev_pos, prev_speed))
                if time2 > time1:
                    #we wont catch up 
                    stack.append((pos, sp))

        return len(stack)
        