class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = set()

        longest = 0
        if not s:
            return 0
        if len(s) == 1:
            return 1
        l = 0
        letters.add(s[l])


        for r in range(1,len(s)):
            while s[r] in letters:
                letters.remove(s[l])
                l += 1
            letters.add(s[r])
            if (r - l + 1) > longest:
                longest = (r - l + 1)
        

        return longest

        