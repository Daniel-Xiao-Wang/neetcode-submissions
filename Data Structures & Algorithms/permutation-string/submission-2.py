from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hmap = defaultdict(int)
        hmap_freq = defaultdict(int)
        l, r = 0, len(s1)
        if len(s1) > len(s2):
                return False

        for i in range(r):
            hmap[s2[i]] += 1
            hmap_freq[s1[i]] += 1

        if hmap == hmap_freq:
            return True

        while r < len(s2):
            hmap[s2[r]] += 1
            hmap[s2[l]] -= 1
            if hmap[s2[l]] == 0:
                del hmap[s2[l]]
            l += 1
            r += 1
        
            if hmap == hmap_freq:
                return True
    
        return False

