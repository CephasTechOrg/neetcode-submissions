from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # First element is always unique
        write = 1

        # Start reading from the second element
        for read in range(1, len(nums)):
            # If current is different from the last kept unique element
            if nums[read] != nums[write - 1]:
                nums[write] = nums[read]  # overwrite in-place
                write += 1

        return write
