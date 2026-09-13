class TimeMap:

    def __init__(self):
        self.timeMap = {}          # key -> list of [timestamp, value]

    def set(self, key, value, timestamp):
        if key not in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        vals = self.timeMap.get(key, [])
        l, r = 0, len(vals) - 1
        while l <= r:
            mid = (l + r) // 2
            if vals[mid][0] <= timestamp:
                res = vals[mid][1]
                l = mid + 1
            else:
                r = mid - 1
        return res
        
        
