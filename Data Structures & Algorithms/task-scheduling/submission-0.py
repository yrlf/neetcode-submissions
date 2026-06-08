import heapq
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # pq = [ (freq, task), ..]
        # choose n+1 task from pq, add time
        pq = []
        cnt = Counter(tasks)
        for task_id, freq in cnt.items():
            heapq.heappush(pq, (-freq, task_id))
        
        time = 0
        while pq:
            size = len(pq)
            tmp = []
            for _ in range(n+1):
                if not pq:
                    break
                freq, task_id = heapq.heappop(pq) # freq is negative
                freq += 1
                if (freq != 0):
                    tmp.append((freq, task_id))
            if tmp:
                for freq, task_id in tmp:
                    heapq.heappush(pq, (freq, task_id))
            if pq:
                time += n+1
            else:
                time += size

            #print(pq, time)
        
        return time