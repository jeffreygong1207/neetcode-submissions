class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mapping = defaultdict(list)

        for word in strs:
            arr = [0] * 26
            for letter in word:
                arr[ord(letter) - ord('a')] += 1
            mapping[tuple(arr)].append(word)
        
        return list(mapping.values())
            
        