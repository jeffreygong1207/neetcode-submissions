class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        stringS = sorted(s)
        stringT = sorted(t)
        for number in range(len(stringS)):
            if len(stringS) != len(stringT):
                return False
            if stringS[number] != stringT[number]:
                return False
        return True