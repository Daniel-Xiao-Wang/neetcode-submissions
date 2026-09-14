class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        count = {}
        longest = 0
        while r < len(s):
            count[s[r]] = count.get(s[r], 0) + 1
            r += 1
            while (r - l) - max(count.values()) > k:
                count[s[l]] = count.get(s[l], 0) - 1
                l += 1
            longest = max(longest, r - l)
        return longest
                
