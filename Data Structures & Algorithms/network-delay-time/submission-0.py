class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        dist = [float('inf') for _ in range(n)]
        dist[k-1] = 0

        graph = defaultdict(list)
        for _from, _to, weight in times:
            graph[_from -1].append((_to-1, weight))
        
        q = [(0, k-1)]

        while q:
            currDist, currNode = heapq.heappop(q)

            if dist[currNode] < currDist:
                continue

            for childNode, weight in graph[currNode]:
                newDist = currDist + weight
                if newDist < dist[childNode]:
                    dist[childNode] = newDist
                    heapq.heappush(q, (newDist, childNode))
        

        res = max(dist)
        if res == float('inf'):
            return -1
        else:
            return res