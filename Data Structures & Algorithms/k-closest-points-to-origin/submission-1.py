class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        new_array = []

        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]
            distance = x**2 + y**2
            new_array.append((distance, x, y))
        
        heapq.heapify(new_array)
        answer = []
        while new_array and k > 0:
            point = heapq.heappop(new_array)
            answer.append([point[1],point[2]])
            k -= 1

        return answer