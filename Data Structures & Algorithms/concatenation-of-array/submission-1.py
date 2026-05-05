class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for _ in range(2):          # repeat twice
            for num in nums:
                ans.append(num)
        return ans