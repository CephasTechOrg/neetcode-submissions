class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        seen = set()
        left = 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            current_length = right - left + 1
            max_length = max(max_length, current_length)
        return max_length    

        