from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            current_number = nums[i]
            needed = target - current_number

            if needed in seen:
                return [seen[needed], i]

            seen[current_number] = i