class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(string)}#{string}" for string in strs)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            digits = s[i:j]
            i = j + 1
            word = s[i:(i + int(digits))]
            result.append(word)
            i += int(digits)
        
        return result

