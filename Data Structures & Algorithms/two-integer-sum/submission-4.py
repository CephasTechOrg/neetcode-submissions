from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        hashmap = {}

        for i in range(len(nums)):
            difference = target - nums[i]

            if difference in hashmap:
                return [hashmap[difference], i]
            
            hashmap[nums[i]] = i










