class Solution:
    def isPalindrome(self, s: str) -> bool:
        c = ""
        for char in s:
            if char.isalnum():
                c += char.lower()
        left = 0
        right = len(c)-1

        while left < right:
            if c[left] != c[right]:
                return False
            left += 1
            right -= 1

        return True              
        