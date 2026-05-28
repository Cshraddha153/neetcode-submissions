class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {c:[] for c in range(numCourses)}
        for u, v in prerequisites:
            adj[u].append(v)


        stack = []
        visit = set()
        cycle = set()
        def dfs(i):
            if i in cycle:
                return False
            if i in visit:
                return True
            cycle.add(i)
            stack.append(i)
            for nei in adj[i]:
                if dfs(nei)==False:
                    return False
            cycle.remove(i)
            visit.add(i)
            stack.append(i)
            return True                    

        for node in range(numCourses):
            if dfs(node) ==  False:
                return []
                
        return stack