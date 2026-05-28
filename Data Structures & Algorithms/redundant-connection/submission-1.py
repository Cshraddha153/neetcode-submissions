class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # dfs optimal
        n = len(edges)
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visit = set()
        cycle = set()
        cycle_start = -1
        def dfs(node, par):
            nonlocal cycle_start
            if node in visit:
                cycle_start = node
                return True
            
            visit.add(node)
            for nei in adj[node]:
                if nei==par:
                    continue
                if dfs(nei, node):
                    if cycle_start != -1:
                        cycle.add(node)
                    if node ==  cycle_start:
                        cycle_start = -1
                    return True
            return False
        dfs(1, -1)
        for u, v in reversed(edges):
            if u in cycle and v in cycle:
                return [u, v]
        return []





        # dfs  tc=O(E(V+E))  sc=O(V+E)
        def dfs(node, par):
            if node in visit:
                return True # cycle hai
            visit.add(node)
            for nei in adj[node]:
                if nei == par:
                    continue
                if dfs(nei, node):
                    return True
            return False # no cycle present

        adj = [[] for _ in range(len(edges)+1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            visit =set()

            if dfs(u, -1):
                return [u, v]
        return []




        
        