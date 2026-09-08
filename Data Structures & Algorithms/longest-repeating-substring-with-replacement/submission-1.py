class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        largest = 0
        tracker = defaultdict(int)
        mostFrequent = 0
        while r < len(s):
            tracker[s[r]] += 1
            mostFrequent = max(mostFrequent, tracker[s[r]])
            difference = (r - l + 1) - mostFrequent
            if difference <= k:
                largest = max((r-l+1), largest) 
            else:
                tracker[s[l]] -= 1
                l += 1
            r += 1

        return largest
        