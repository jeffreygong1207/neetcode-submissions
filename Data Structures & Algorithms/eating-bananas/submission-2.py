class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        k = 0
        while l <= r:
            middle = (l+r)//2
            hours = self.hours_needed(piles, middle) 
            if hours <= h:
                k = middle
                r = middle - 1
            elif hours > h:
                l = middle + 1
            else:
                r = middle - 1

        return k
            
            
        
    
    def hours_needed(self, piles, k):
        hours = 0
        for pile in piles:
            hours += pile // k
            if pile % k > 0:
                hours += 1
        return hours

        