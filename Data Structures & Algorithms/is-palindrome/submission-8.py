class Solution:
    def isPalindrome(self, s: str) -> bool:
        c = ""
        for char in s:
            if char.isalnum():
                c += char.lower()
        right = len(c)-1
        left = 0
        while right > left:
            if c[left] != c[right]:
                return False
            right -=1
            left +=1
        return True                             
            
        
        
        