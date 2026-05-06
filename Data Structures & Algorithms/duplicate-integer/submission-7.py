class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen  = set()
        for n in nums:
            if n in seen:
                return True
            else:
                seen.add(n)    
        return False





        

