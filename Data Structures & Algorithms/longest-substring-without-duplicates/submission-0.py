class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        longest = 0
        counter = set()

        while r < len(s):
            if (s[r] in counter):
                while (s[r] in counter):
                    counter.remove(s[l])
                    l += 1
            counter.add(s[r])
            length = r - l + 1
            longest = max(length, longest)
            r += 1
        

        return longest
        