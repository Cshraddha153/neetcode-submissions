class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        adj = [[] for i in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(i, par):
            if i in visited:
                return False
            visited.add(i)
            for j in adj[i]:
                if j == par:
                    continue
                if not dfs(j, i):
                    return False
            return True          
        
        return dfs(0, -1) and n==len(visited)
