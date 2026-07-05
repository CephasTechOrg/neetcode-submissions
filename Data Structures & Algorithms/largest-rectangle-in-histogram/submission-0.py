class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Pseudocode:
        # create max_area = 0
        # loop through each starting index i
        #     create min_height = infinity
        #     loop through each ending index j from i to end
        #         update min_height
        #         calculate width
        #         calculate area
        #         update max_area
        # return max_area

        max_area = 0

        for i in range(len(heights)):
            min_height = float("inf")

            for j in range(i, len(heights)):
                min_height = min(min_height, heights[j])
                width = j - i + 1
                area = min_height * width
                max_area = max(max_area, area)

        return max_area