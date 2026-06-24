class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

    # Loop through every index in nums
        for i in range(len(nums)):
            # Current number we are standing on
            current = nums[i]

            # The number we need to add to current to reach target
            needed = target - current

            # If the needed number is already in the hashmap,
            # then we have found the two numbers
            if needed in seen:
                # seen[needed] gives the index of the old number
                # i gives the index of the current number
                return [seen[needed], i]

            else:
                # If the needed number is not found,
                # store the current number with its index
                seen[current] = i
            
            