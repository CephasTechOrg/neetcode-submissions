class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}

        for i, num in enumerate(nums):

            # If we have seen this number before,
            # check how far apart the indices are.
            if num in seen and i - seen[num] <= k:
                return True
            seen[num] = i

        return False