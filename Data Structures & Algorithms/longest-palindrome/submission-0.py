class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 0
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
            if count[c] % 2 == 0:
                res += 2
        if res < len(s):
            res += 1
        return res            
        