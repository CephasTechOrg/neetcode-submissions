class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        countS = {}
        countT = {}

        for ch in s:
            countS[ch] = 1 + countS.get(ch, 0)

        for ch in t:
            countT[ch] = 1 + countT.get(ch, 0)

        if countS == countT:
            return True

        return False