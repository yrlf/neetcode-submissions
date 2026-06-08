class TimeMap:

    def __init__(self):
        self.record = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.record:
            self.record[key] = []
        self.record[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.record:
            return ""
        
        arr = self.record[key]
        target = timestamp + 1
        l, r = 0, len(arr)
        while l < r:
            mid = (l+r)>>1
            if arr[mid][1] >= target:
                r = mid
            else:
                l = mid + 1
        return arr[l - 1][0] if l - 1 >= 0 else ""
