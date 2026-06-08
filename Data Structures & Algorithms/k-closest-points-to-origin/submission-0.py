import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        n = len(points)
        pq = []

        for point in points:
            dist = (point[0]**2 + point[1]**2)**0.5
            heapq.heappush(pq, (dist, point[0], point[1]))
        
        res = []
        while len(res) != k:
            dist, x, y = heapq.heappop(pq)
            res.append([x, y])
        
        return res