class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        path = set()
        hasCycle = False


        def dfs(node, parent):
            
            nonlocal hasCycle

            if hasCycle:
                return
            if node in path:
                hasCycle = True
                return
            if node in visited:
                return

            path.add(node)
            visited.add(node)
            for child in graph[node]:
                if child == parent:
                    continue
                dfs(child, node)
            path.remove(node)



        dfs(0, None)

        return not hasCycle and len(visited) == n