class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visit = set()
        def dfs(i):
            visit.add(i)
            for nei in adj[i]:
                if nei not in visit:
                    dfs(nei)
                    
        
        for node in range(n):
            if node not in visit:
                dfs(node)
                count+=1
        return count
                

