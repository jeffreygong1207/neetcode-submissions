from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            course = q.popleft()
            numCourses -= 1
            unlocked = graph[course]
            for i in unlocked:
                indegree[i] -= 1
                if indegree[i] == 0 :
                    q.append(i)
        
        if numCourses == 0:
            return True
        else:
            return False


        