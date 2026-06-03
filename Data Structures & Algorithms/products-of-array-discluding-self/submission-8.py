class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Create a result array the same size as nums.
        # We fill it with 1 because 1 does not affect multiplication.
        res = [1] * len(nums)

        # prefix stores the product of all values before nums[i].
        # For index 0, there is nothing before it, so we start with 1.
        prefix = 1

        for i in range(len(nums)):
            # prefix already contains the product of everything
            # before nums[i], so we can store it directly in res[i].
            res[i] = prefix

            # Update prefix so the next index can use the work
            # we have already done instead of multiplying from
            # the beginning all over again.
            prefix *= nums[i]

        # postfix stores the product of all values after nums[i].
        # For the last index, there is nothing after it, so start with 1.
        postfix = 1

        for i in range(len(nums) - 1, -1, -1):
            # res[i] already contains the product of everything
            # to the left of nums[i].
            #
            # postfix contains the product of everything to the
            # right of nums[i].
            #
            # Multiplying them together gives the product of
            # all values except nums[i].
            res[i] *= postfix

            # Update postfix so the next index on the left can
            # reuse this work instead of multiplying from the
            # end all over again.
            postfix *= nums[i]

        return res

        