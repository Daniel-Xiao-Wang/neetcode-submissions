import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)
        l = 0
        minK = max(piles)
        while (l <= r) and (r > 1):
            hours = 0
            mid = (r + l) // 2
            print(r)
            print(l)
            print(mid)
            for i in piles:
                hours += math.ceil(i/mid)
            if hours <= h:
                r = mid - 1
                minK = min(mid, minK)
            else:
                l = mid + 1
        return minK