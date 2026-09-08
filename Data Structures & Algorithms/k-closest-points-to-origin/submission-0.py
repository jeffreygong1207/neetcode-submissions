class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #distance formula
        #(y1-y2)^2 + (x1-x2)^2

        #turn points into a heap

        minHeap = []
        for x, y in points:
            dist = (x **2) + y**2
            minHeap.append([dist,x,y])
        
        heapq.heapify(minHeap)
        res = []

        while k > 0:
            result = heapq.heappop(minHeap)
            points = [result[1], result[2]]
            res.append(points)
            k -= 1


        return res
        