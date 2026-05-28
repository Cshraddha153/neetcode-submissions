class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #bfs  TC=O(V+E)  sc=O(V+E)
        adj = [[] for _ in range(n)]
        visit = set()
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        def bfs(node):
            q=deque([node])
            visit.add(node)
            while q:
                cur = q.popleft()
                for nei in adj[cur]:
                    if nei not in visit:
                        visit.add(nei)
                        q.append(nei)
        res = 0
        for node in range(n):
            if node not in visit:
                bfs(node)
                res+=1
        return res

        # TC=O(V+E)  sc=O(V+E)
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
                

