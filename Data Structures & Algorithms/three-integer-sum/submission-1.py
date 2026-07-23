from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the numbers so that we can use two pointers.
        nums.sort()

        results = []

        # Fix one number using i.
        # range(len(nums) - 2) leaves room for k and j.
        for i in range(len(nums) - 2):

            # Skip duplicate fixed values.
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # k starts immediately after i.
            k = i + 1

            # j starts at the end of the list.
            j = len(nums) - 1

            # Search all possible pairs for this fixed i.
            while k < j:
                current_sum = nums[i] + nums[k] + nums[j]

                if current_sum == 0:
                    # Save the three values, not their indexes.
                    results.append([nums[i], nums[k], nums[j]])

                    # Move both pointers after finding a valid triplet.
                    k += 1
                    j -= 1

                    # Skip duplicate values on the left.
                    while k < j and nums[k] == nums[k - 1]:
                        k += 1

                    # Skip duplicate values on the right.
                    while k < j and nums[j] == nums[j + 1]:
                        j -= 1

                elif current_sum < 0:
                    # The sum is too small, so move k right.
                    k += 1

                else:
                    # The sum is too large, so move j left.
                    j -= 1

        return results