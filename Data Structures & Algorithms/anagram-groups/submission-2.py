from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tracker = defaultdict(list)
        for word in strs:
            tracker[''.join(sorted(word))].append(word)
        
        result = []
        for key, value in tracker.items():
            result.append(value)


        return result
            
        