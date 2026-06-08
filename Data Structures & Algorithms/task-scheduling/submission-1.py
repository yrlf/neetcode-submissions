class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        cnt = Counter(tasks)
        q = []

        for task, freq in cnt.items():
            heapq.heappush(q, (-freq, task))
        
        # O(K logK)

        ans = 0
        
        while q:
            size = len(q)
            tmp = []

            for _ in range(n+1):
                if not q:
                    break
                freq, task = heapq.heappop(q)
                freq += 1
                if (freq != 0):
                    tmp.append((freq, task))
            
            if tmp:
                for freq, task in tmp:
                    heapq.heappush(q, (freq, task))
            # 如果剩下还有任务,这一轮时间是n+1            
            if q:
                ans += n+1
            else:
                ans += size

        return ans