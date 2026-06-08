class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for i in range(numCourses):
            indegree[i] = 0
    
        for _to, _from in prerequisites:
            graph[_from].append(_to)
            indegree[_to] += 1

        q = deque()

        for node, degree in indegree.items():
            if degree == 0:
                q.append(node)
        
        visited = set()
        record = []
        while q:
            curr = q.popleft()
            visited.add(curr)
            record.append(curr)
            for child in graph[curr]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    q.append(child)

        if len(record) != numCourses:
            return []
        else:
            return record