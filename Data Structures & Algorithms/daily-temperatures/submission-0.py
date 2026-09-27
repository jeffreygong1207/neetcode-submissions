class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = []
        for i , t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                indice = stack.pop()
                result[indice] = i - indice
            result.append(0)
            stack.append(i)

        return result
            
        