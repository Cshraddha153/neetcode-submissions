class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # dfs   tc=sc=O(E*V)
        adj = {src: [] for src, dst in tickets}
        tickets.sort()
        for src, dst in tickets:
            adj[src].append(dst)
        res = ["JFK"]
        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in adj:
                return False
            temp = list(adj[src])
            for i, v in enumerate(temp):
                adj[src].pop(i)
                res.append(v)
                if dfs(v): return True
                adj[src].insert(i, v)
                res.pop()
            return False



        dfs("JFK")
        return res












        # tc=O(ElogE)  sc=O(E) Hierholzer's Algorithm

        adj = defaultdict(list)
        for u, v in sorted(tickets, reverse=True):  # Sort neighbors in reverse lexical order
            adj[u].append(v) 
        itinerary = []

        def dfs(departure):
            while adj[departure]:
                arrival = adj[departure].pop()
                dfs(arrival)
            itinerary.append(departure)

        dfs("JFK")
        return itinerary[::-1]


###%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    






















