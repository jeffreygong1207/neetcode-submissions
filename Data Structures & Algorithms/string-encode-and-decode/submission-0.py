class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            n = len(word)
            result += (str(n) + "#" + word)
        return result

    def decode(self, s: str) -> List[str]:
        answer = []
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] != "#":
                j += 1

            length = int(s[i:j])
            word = s[j + 1 : j + 1 + length] 
            answer.append(word)
            
            i = j + 1 + length
        
        return answer
            
