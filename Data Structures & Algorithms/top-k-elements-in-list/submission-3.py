class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        # freq array where the index represents the frequency of the numbers
        freq = [[] for _ in range(len(nums) + 1)]

        # Count the frequencies of each number
        for num in nums:
            count[num] = 1 + count.get(num, 0)
            
        # Group numbers by their frequency
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        # Iterate from the highest possible frequency down to 0
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                # Return exactly when we've collected k elements
                if len(res) == k:
                    return res