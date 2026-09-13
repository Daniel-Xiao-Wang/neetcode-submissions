class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mySet = set()
        longest = 0
        l, r = 0, 0
        while r < len(s):
            if s[r] not in mySet:
                mySet.add(s[r])
                r += 1
                longest = max(longest, r - l)
            else:
                mySet.remove(s[l])
                l += 1
        return longest       
        