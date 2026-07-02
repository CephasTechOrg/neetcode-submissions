from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Put all numbers into a set.
        # A set removes duplicates and lets us check if a number exists in O(1) average time.
        numSet = set(nums)

        # This will store the longest consecutive sequence length we have found so far.
        longest = 0

        # Loop through each unique number in the set.
        for num in numSet:

            # A number is the start of a sequence only if the number before it does NOT exist.
            # Example: if num = 2, then 1 should not be in the set.
            # If 1 is not there, then 2 can start a sequence like 2, 3, 4, 5.
            if (num - 1) not in numSet:

                # Since num itself exists, the sequence length starts at 1.
                length = 1

                # Keep checking if the next number exists.
                # Example: if num = 2:
                # Check 2 + 1 = 3
                # Check 2 + 2 = 4
                # Check 2 + 3 = 5
                # Stop when the next number does not exist.
                while (num + length) in numSet:
                    length += 1

                # After counting this sequence, update longest if this sequence is bigger.
                longest = max(longest, length)

        # Return the longest consecutive sequence length found.
        return longest