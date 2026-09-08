class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tracker = defaultdict(list)

        for word in strs:

            tracker["".join(sorted(word))].append(word)
        


        return list(tracker.values())