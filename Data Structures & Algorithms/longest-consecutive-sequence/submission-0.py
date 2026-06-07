class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()

        longest = 1
        current = 1

        for i in range(1, len(nums)):
            # Duplicate number: ignore it
            if nums[i] == nums[i - 1]:
                continue

            # Consecutive number: extend current streak
            if nums[i] == nums[i - 1] + 1:
                current += 1
            else:
                # Sequence broke, start a new streak
                current = 1

            longest = max(longest, current)

        return longest