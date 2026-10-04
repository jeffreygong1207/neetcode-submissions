class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key = lambda x: x[0])
        prevEnd = float('-inf')
        remove = 0
        #now intervals are sorted
        for start, end in intervals:
            if start < prevEnd:

                prevEnd = min(prevEnd, end)
                #need to remove
                remove += 1
            else:
                prevEnd = end

        

        return remove
