class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #probably insert then merge??

        answer = []

        start = newInterval[0]
        end = newInterval[1]

        placed = False
        for interval in intervals:
            istart = interval[0]
            iend = interval[1]
            if iend < start:
                #no touching, just append
                answer.append(interval)
            elif end < istart:
                if not placed:
                    answer.append([start,end])
                    placed = True
                answer.append(interval)
            else:
                #case of merging and check 
                start = min(start,istart)
                end = max(iend,end)
        if not placed:
            answer.append([start, end])


        return answer

        