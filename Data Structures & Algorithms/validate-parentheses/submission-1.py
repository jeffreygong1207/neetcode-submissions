class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        tracker = {")":"(", "]":"[", "}":"{"}

        for c in s:
            if c in tracker:
                if not stack:
                    return False
                if stack.pop() != tracker[c]:
                    return False
            else:
                stack.append(c)
        
        if stack:
            return False
        return True
        