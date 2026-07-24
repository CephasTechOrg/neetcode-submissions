from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        # Pick the left wall.
        for left in range(len(heights)):

            # Compare it with every wall after it.
            for right in range(left, len(heights)):

                # Only the two selected walls determine the water height.
                current_height = min(
                    heights[left],
                    heights[right]
                )

                width = right - left

                current_area = current_height * width

                max_area = max(max_area, current_area)

        return max_area