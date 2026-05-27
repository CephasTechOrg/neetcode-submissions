class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in nums:
            if i not in seen:    # first time seeing this number
                seen.add(i)
            else:                # already exists → duplicate
                return True
        return False