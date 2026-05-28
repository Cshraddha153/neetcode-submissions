class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Dijkstra's Algorithm  tc=O(Elogv)   sc=O(v+e)
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v,w))
        
        minheap = [(0, k)]
        visit = set()
        t=0
        while minheap:
            w1, n1 = heapq.heappop(minheap)
            if n1 in visit:
                continue
            visit.add(n1)
            t=w1
            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minheap, (w1+w2, n2))
        
        return t if len(visit)==n else -1













        # bellman ford algorithm
        # tc = O(V*E)   sc=O(V)

        dist = [float('inf')]*n
        dist[k-1]=0
        for _ in range(n-1):
            for u, v, w in times:
                if dist[u-1] + w < dist[v-1]:
                    dist[v-1] = dist[u-1] + w
        max_dist = max(dist)
        return max_dist if max_dist < float('inf') else -1


        
        
        
        
        
        
        
        
        
        
        
        
        # dfs 
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))

        dist = {node: float('inf') for node in range(1, n+1)}

        def dfs(node, time):
            if time>=dist[node]:
                return
            dist[node] = time
            for nei, w in adj[node]:
                dfs(nei, time+w)

        dfs(k, 0)
        print(dist)
        res = max(dist.values())
        return res if res<float('inf') else -1














        