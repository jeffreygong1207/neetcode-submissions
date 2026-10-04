class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals,key=lambda x: x[0])

        #now this is sorted by start
        stack = []
        for interval in sorted_intervals:
            if not stack:
                stack.append(interval)
            else:
                #interval is in stack
                if stack[-1][1] >= interval[0]:
                    #merge here
                    pstart, pend = stack.pop()
                    new_end =  max(pend, interval[1])
                    stack.append([pstart, new_end])
                else:
                    stack.append(interval)
            
            
        

        return stack