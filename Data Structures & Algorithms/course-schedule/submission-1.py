class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for _to, _from in prerequisites:
            graph[_from].append(_to)
        
        visited = set()
        hasCycle = False

        def dfs(i):
            nonlocal hasCycle
            if i in path:
                hasCycle = True
                return
            
            if i in visited:
                return
            visited.add(i)
            path.add(i)
            for child in graph[i]:
                
                dfs(child)
            path.remove(i)

        for i in range(numCourses):
            if i not in visited:
                path = set()
                dfs(i)
                if hasCycle == True:
                    return False
        

        return True
        