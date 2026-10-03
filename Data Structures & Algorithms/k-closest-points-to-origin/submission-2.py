import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        
        for point in points:
            distance = math.sqrt(point[0]**2 + point[1]**2)
            print(point[0])
            print(point[1])
            print(distance)
            distances.append((distance, point))
        
        heapq.heapify(distances)
        print(distances)
        closest = heapq.nsmallest(k,distances)
    
        return [x[1] for x in closest]