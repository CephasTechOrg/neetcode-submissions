class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        CountS = {}
        CountT = {}
        if len(t) != len(s):
            return False
        
        for ch in s:
            CountS[ch] = CountS.get(ch, 0) + 1
        for ch in t:
            CountT[ch] = CountT.get(ch, 0) + 1
        if CountT == CountS:
            return True 
        return False           

        
        
        