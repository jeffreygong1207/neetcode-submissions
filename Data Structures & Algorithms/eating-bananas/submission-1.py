class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        bottom = 1
        top = max(piles)
        smallest = top

        while bottom <= top:
            middle = (bottom + top)//2
            bites = []
            for size in piles:
                if size % middle > 0:
                    bites.append((size//middle) + 1)
                else:
                    bites.append(size//middle)
            if sum(bites) <= h:
                smallest = middle
                top = middle - 1
            else:
                bottom = middle + 1
            
        
        return smallest



        