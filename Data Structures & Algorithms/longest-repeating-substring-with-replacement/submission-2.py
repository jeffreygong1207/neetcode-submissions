from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0


        l = 0
        tracker = defaultdict(int)
        for r in range(len(s)):
            #start removing 
            tracker[s[r]] += 1
            while (r - l + 1) - max(tracker.values()) > k:
                tracker[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)

            r += 1


        return longest
        