class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        
        if len(edges) != n-1:
            return False
        
        for edge in edges:
            start = edge[0]
            end = edge[1]
            graph[start].append(end)
            graph[end].append(start)


        visited = {0}
        stack = [0]
        while stack:
            node = stack.pop()
            for children in graph[node]:
                if children not in visited:
                    stack.append(children)
                    visited.add(children)
        
        return len(visited) == n
        
        
        

        